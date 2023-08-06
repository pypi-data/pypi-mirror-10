cdef class NetLearner: 
    cdef cDeepCL.CyNetLearner *thisptr
    def __cinit__( self, SGD sgd, NeuralNet neuralnet,
            Ntrain, float[:] trainData, int[:] trainLabels,
            Ntest, float[:] testData, int[:] testLabels,
            batchSize ):
        self.thisptr = new cDeepCL.CyNetLearner(
            sgd.thisptr, neuralnet.thisptr,
            Ntrain, &trainData[0], &trainLabels[0],
            Ntest, &testData[0], &testLabels[0],
            batchSize )
    def __dealloc(self):
        del self.thisptr
#    def setTrainingData( self, Ntrain, float[:] trainData, int[:] trainLabels ):
#        self.thisptr.setTrainingData( Ntrain, &trainData[0], &trainLabels[0] )
#    def setTestingData( self, Ntest, float[:] testData, int[:] testLabels ):
#        self.thisptr.setTestingData( Ntest, &testData[0], &testLabels[0] )
    def setSchedule( self, numEpochs ):
        self.thisptr.setSchedule( numEpochs )
    def setDumpTimings( self, bint dumpTimings ):
        self.thisptr.setDumpTimings( dumpTimings )
#    def setBatchSize( self, batchSize ):
#        self.thisptr.setBatchSize( batchSize )
    def _run(self):
        with nogil:
           self.thisptr.run()
    def run(self):
        interruptableCall( self._run, [] ) 
##        with nogil:
##            thisptr._learn( learningRate )
        checkException()


