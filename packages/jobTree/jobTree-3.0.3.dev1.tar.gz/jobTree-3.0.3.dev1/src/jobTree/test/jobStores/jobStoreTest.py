from Queue import Queue
from abc import abstractmethod, ABCMeta
import hashlib
import logging
import os
import tempfile
from threading import Thread
import uuid
from xml.etree.cElementTree import Element

from jobTree.jobStores.abstractJobStore import (NoSuchJobException, NoSuchFileException, AbstractJobStore)
from jobTree.jobStores.awsJobStore import AWSJobStore
from jobTree.jobStores.fileJobStore import FileJobStore
from jobTree.test import JobTreeTest


logger = logging.getLogger( __name__ )

# TODO: AWSJobStore does not check the existence of jobs before associating files with them

class hidden:
    """
    Hide abstract base class from unittest's test case loader

    http://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class#answer-25695512
    """
    class AbstractJobStoreTest( JobTreeTest ):
        __metaclass__ = ABCMeta

        # FIXME: This switch is currently used to alter test behaviour in order to cover both the
        # FIXME: ... file and the AWS job store implementation. Consolidate both implementation and
        # FIXME: ... eliminate this switch.

        firstJobShouldExistAfterCreation = True

        # FIXME: This switch is currently used to alter test behaviour in order to cover both the
        # FIXME: ... file and the AWS job store implementation. Consolidate both implementation and
        # FIXME: ... eliminate this switch.

        jobStoreKeepsChildrenAttributeConsistent = True

        default_try_count = 1

        maxDiff = None

        def _dummyConfig( self ):
            config = Element( "config" )
            config.attrib[ "try_count" ] = str( self.default_try_count )
            return config

        @abstractmethod
        def createJobStore( self, config=None ):
            """
            :rtype: AbstractJobStore
            """
            raise NotImplementedError( )

        def setUp( self ):
            super( hidden.AbstractJobStoreTest, self ).setUp( )
            self.namePrefix = str( uuid.uuid4( ) )
            config = self._dummyConfig( )
            self.master = self.createJobStore( config )

        def tearDown( self ):
            self.master.deleteJobStore( )
            super( hidden.AbstractJobStoreTest, self ).tearDown( )

        def test( self ):
            """
            This is a front-to-back test of the "happy" path in a job store, i.e. covering things
            that occur in the dat to day life of a job store. The purist might insist that this be
            split up into several cases and I agree wholeheartedly.
            """
            master = self.master

            # Test initial state
            #
            self.assertFalse( master.loadJobTreeState( ).started )
            self.assertFalse( master.exists( "foo" ) )

            # Create parent job and verify its existence
            #
            jobOnMaster = master.createFirstJob( "master1", 12, 34 )
            self.assertTrue( master.loadJobTreeState( ).started )
            if self.firstJobShouldExistAfterCreation:
                self.assertTrue( master.exists( jobOnMaster.jobStoreID ) )
            else:
                master.store( jobOnMaster )
            self.assertEquals( jobOnMaster.followOnCommands, [ ('master1', 12, 34, 0) ] )

            # Create a second instance of the job store, simulating a worker ...
            #
            worker = self.createJobStore( )
            self.assertTrue( worker.loadJobTreeState( ).started )
            # ... and load the parent job there.
            jobOnWorker = worker.load( jobOnMaster.jobStoreID )
            self.assertEquals( jobOnMaster, jobOnWorker )

            # Add two children on the worker
            #
            childSpecs = { ("child1", 23, 45), ("child2", 34, 56) }
            worker.addChildren( jobOnWorker, childSpecs )
            self.assertNotEquals( jobOnWorker, jobOnMaster )
            self.assertEquals( len( jobOnWorker.children ), 2 )
            # Reload parent job on master
            jobOnMaster = master.load( jobOnMaster.jobStoreID )
            self.assertEquals( jobOnWorker, jobOnMaster )
            # Load children
            childJobs = { worker.load( childCommand[ 0 ] ) for childCommand in jobOnMaster.children }

            # Now load the job tree state reflecting all jobs
            #
            state = master.loadJobTreeState( )
            self.assertTrue( state.started )
            self.assertEquals( state.shellJobs, set( ) )
            self.assertEquals( state.updatedJobs, childJobs )
            # The parent should have two children
            self.assertEquals( state.childCounts, { self._prepareJobForComparison( jobOnMaster ): 2 } )
            self.assertEquals( len( state.childJobStoreIdToParentJob ), 2 )
            # Ensure consistency between children as referred to by the parent and by the jobTree state
            for child in jobOnMaster.children:
                childJobStoreId = child[ 0 ]
                self.assertEquals( state.childJobStoreIdToParentJob[ childJobStoreId ],
                                   self._prepareJobForComparison( jobOnMaster ) )
                childJob = worker.load( childJobStoreId )
                self.assertTrue( childJob in childJobs )
                self.assertEquals( childJob.jobStoreID, childJobStoreId )
                self.assertEquals( childJob.children, [ ] )
                # This would throw if the child command wasn't present
                childSpecs.remove( childJob.followOnCommands[ 0 ][ 0:3 ] )
            # Make sure every child command is accounted for
            self.assertEquals( childSpecs, set( ) )

            # Test changing and persisting job state
            #
            for childJob in childJobs:
                childJob.followOnCommands.append( ("command4", 45, 67, 0) )
                childJob.logJobStoreFileID = str( uuid.uuid4( ) )
                childJob.remainingRetryCount = 66
                self.assertNotEquals( childJob, master.load( childJob.jobStoreID ) )
            for childJob in childJobs:
                worker.store( childJob )
            for childJob in childJobs:
                self.assertEquals( master.load( childJob.jobStoreID ), childJob )

            # Test emptying out the container-like attributes. This test is especially relevant in
            # the AWS job store since the underlying SimpleDB API can't represent attributes that are
            # None or [] in a straight-forward manner.
            #
            childJob = next( iter( childJobs ) )
            self.assertTrue( len( childJob.followOnCommands ) > 0 )
            childJob.followOnCommands = [ ]
            self.assertEquals( len( childJob.followOnCommands ), 0 )
            master.store( childJob )
            childJobOnWorker = worker.load( childJob.jobStoreID )
            self.assertEquals( len( childJob.followOnCommands ), 0 )
            self.assertEquals( childJobOnWorker, childJob )
            # Now that one child is without follow-ons, it should omitted from the parent
            jobOnMaster = master.load( jobOnMaster.jobStoreID )
            if self.jobStoreKeepsChildrenAttributeConsistent:
                self.assertEquals( len( jobOnMaster.children ), 1 )

            # Test job deletions
            #
            for childJob in childJobs:
                master.delete( childJob )
            jobOnMaster = master.load( jobOnMaster.jobStoreID )
            if self.jobStoreKeepsChildrenAttributeConsistent:
                self.assertEquals( len( jobOnMaster.children ), 0 )
            for childJob in childJobs:
                self.assertFalse( worker.exists( childJob.jobStoreID ) )
                self.assertRaises( NoSuchJobException, worker.load, childJob.jobStoreID )
            # delete should be idempotent
            for childJob in childJobs:
                master.delete( childJob )
            jobOnWorker = worker.load( jobOnMaster.jobStoreID )
            self.assertEquals( jobOnMaster, jobOnWorker )

            # Test shared files: Write shared file on master, ...
            #
            with master.writeSharedFileStream( "foo" ) as f:
                f.write( "bar" )
            # ... read that file on worker, ...
            with worker.readSharedFileStream( "foo" ) as f:
                self.assertEquals( "bar", f.read( ) )
            # ... and read it again on master.
            with master.readSharedFileStream( "foo" ) as f:
                self.assertEquals( "bar", f.read( ) )

            # Test per-job files: Create empty file on master, ...
            #
            fileOne = worker.getEmptyFileStoreID( jobOnMaster.jobStoreID )
            # ... write to the file on worker, ...
            with worker.updateFileStream( fileOne ) as f:
                f.write( "one" )
            # ... read the file as a stream on the master, ....
            with master.readFileStream( fileOne ) as f:
                self.assertEquals( f.read( ), "one" )
            # ... and copy it to a temporary physical file on the master.
            fh, path = tempfile.mkstemp( )
            try:
                os.close( fh )
                master.readFile( fileOne, path )
                with open( path, 'r+' ) as f:
                    self.assertEquals( f.read( ), "one" )
                    # Write a different string to the local file ...
                    f.seek( 0 )
                    f.truncate( 0 )
                    f.write( "two" )
                # ... and create a second file from the local file.
                fileTwo = master.writeFile( jobOnMaster.jobStoreID, path )
                with worker.readFileStream( fileTwo ) as f:
                    self.assertEquals( f.read( ), "two" )
                # Now update the first file from the local file ...
                master.updateFile( fileOne, path )
                with worker.readFileStream( fileOne ) as f:
                    self.assertEquals( f.read( ), "two" )
            finally:
                os.unlink( path )
            # Create a third file to test the last remaining method.
            with worker.writeFileStream( jobOnMaster.jobStoreID ) as ( f, fileThree ):
                f.write( "three" )
            with master.readFileStream( fileThree ) as f:
                self.assertEquals( f.read( ), "three" )
            # Delete a file explicitly but leave files for the implicit deletion through the parent
            worker.deleteFile( fileOne )

            # Delete parent and its associated files
            #
            master.delete( jobOnMaster )
            self.assertFalse( master.exists( jobOnMaster.jobStoreID ) )
            # Files should be gone as well. NB: the fooStream() methods return context managers
            self.assertRaises( NoSuchFileException, worker.readFileStream( fileTwo ).__enter__ )
            self.assertRaises( NoSuchFileException, worker.readFileStream( fileThree ).__enter__ )

            # TODO: Who deletes the shared files?

            # TODO: Test stats methods

        def testMultipartUploads( self ):
            """
            This test is meant to cover multi-part uploads in the AWSJobStore but it doesn't hurt
            running it against the other job stores as well.
            """
            # Should not block. On Linux, /dev/random blocks when its running low on entropy
            random_device = '/dev/urandom'
            # http://unix.stackexchange.com/questions/11946/how-big-is-the-pipe-buffer
            bufSize = 65536
            partSize = AWSJobStore._s3_part_size
            self.assertEquals( partSize % bufSize, 0 )
            job = self.master.createFirstJob( "1", 2, 3 )

            # Test file/stream ending on part boundary and within a part
            #
            for partsPerFile in ( 1, 2.33 ):
                checksum = hashlib.md5( )
                checksumQueue = Queue( 2 )

                # FIXME: Having a separate thread is probably overkill here

                def checksumThreadFn( ):
                    while True:
                        _buf = checksumQueue.get( )
                        if _buf is None: break
                        checksum.update( _buf )

                # Multipart upload from stream
                #
                checksumThread = Thread( target=checksumThreadFn )
                checksumThread.start( )
                try:
                    with open(random_device) as readable:
                        with self.master.writeFileStream( job.jobStoreID ) as ( writable, fileId ):
                            for i in range( int( partSize * partsPerFile / bufSize ) ):
                                buf = readable.read( bufSize )
                                checksumQueue.put( buf )
                                writable.write( buf )
                finally:
                    checksumQueue.put( None )
                    checksumThread.join( )
                before = checksum.hexdigest( )

                # Verify
                #
                checksum = hashlib.md5( )
                with self.master.readFileStream( fileId ) as readable:
                    while True:
                        buf = readable.read( bufSize )
                        if not buf: break
                        checksum.update( buf )
                after = checksum.hexdigest( )
                self.assertEquals( before, after )

                # Multi-part upload from file
                #
                checksum = hashlib.md5( )
                fh, path = tempfile.mkstemp( )
                try:
                    with os.fdopen( fh, 'r+' ) as writable:
                        with open(random_device) as readable:
                            for i in range( int( partSize * partsPerFile / bufSize ) ):
                                buf = readable.read( bufSize )
                                writable.write( buf )
                                checksum.update( buf )
                    fileId = self.master.writeFile( job.jobStoreID, path )
                finally:
                    os.unlink( path )
                before = checksum.hexdigest( )

                # Verify
                #
                checksum = hashlib.md5( )
                with self.master.readFileStream( fileId ) as readable:
                    while True:
                        buf = readable.read( bufSize )
                        if not buf: break
                        checksum.update( buf )
                after = checksum.hexdigest( )
                self.assertEquals( before, after )
            self.master.delete( job )

        def testZeroLengthFiles( self ):
            job = self.master.createFirstJob( "1", 2, 3 )
            nullFile = self.master.writeFile( job.jobStoreID, '/dev/null' )
            with self.master.readFileStream( nullFile ) as f:
                self.assertEquals( f.read( ), "" )
            with self.master.writeFileStream( job.jobStoreID ) as ( f, nullStream ):
                pass
            with self.master.readFileStream( nullStream ) as f:
                self.assertEquals( f.read( ), "" )

        # FIXME: This method is currently used to alter test behavior in order to account for the (in
        # FIXME: ... my opinion) surprising behavior of loadJobTreeState() to reset message, children
        # FIXME: ... and remainingRetryCount. Resolve dispute and eliminate this method.

        def _prepareJobForComparison( self, job ):
            """
            :type job: jobTree.job.Job
            """
            copy = job.copy( )
            copy.children = [ ]
            copy.remainingRetryCount = self.default_try_count
            return copy


class FileJobStoreTest( hidden.AbstractJobStoreTest ):
    firstJobShouldExistAfterCreation = False
    jobStoreKeepsChildrenAttributeConsistent = False
    def createJobStore( self, config=None ):
        return FileJobStore( self.namePrefix, config )


class AWSJobStoreTest( hidden.AbstractJobStoreTest ):
    testRegion = "us-west-2"

    def createJobStore( self, config=None ):
        AWSJobStore._s3_part_size = 5 * 1024 * 1024
        return AWSJobStore.create( "%s:%s" % (self.testRegion, self.namePrefix), config )
