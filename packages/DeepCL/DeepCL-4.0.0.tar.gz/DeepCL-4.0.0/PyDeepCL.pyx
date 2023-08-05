# Copyright Hugh Perkins 2015
#
# This Source Code Form is subject to the terms of the Mozilla Public License, 
# v. 2.0. If a copy of the MPL was not distributed with this file, You can 
# obtain one at http://mozilla.org/MPL/2.0/.

from cython cimport view
from cpython cimport array as c_array
from array import array
import threading
from libcpp.string cimport string
from libcpp cimport bool

cimport cDeepCL

include "EasyCL.pyx"
include "SGD.pyx"
include "NeuralNet.pyx"
include "Layer.pyx"
include "LayerMaker.pyx"
include "GenericLoader.pyx"
include "NetLearner.pyx"
include "NetDefToNet.pyx"

def checkException():
    cdef int threwException = 0
    cdef string message = ""
    cDeepCL.checkException( &threwException, &message)
    # print('threwException: ' + str(threwException) + ' ' + message ) 
    if threwException:
        raise RuntimeError(message)

def interruptableCall( function, args ):
    mythread = threading.Thread( target=function, args = args )
    mythread.daemon = True
    mythread.start()
    while mythread.isAlive():
        mythread.join(0.1)
        #print('join timed out')

def toCppString( pyString ):
    if isinstance( pyString, unicode ):
        return pyString.encode('utf8')
    return pyString

cdef class QLearner:
    cdef cDeepCL.QLearner *thisptr
    def __cinit__(self,SGD sgd, Scenario scenario,NeuralNet net):
        scenario.net = net
        self.thisptr = new cDeepCL.QLearner(
            sgd.thisptr, scenario.thisptr, net.thisptr)
    def __dealloc__(self):
        del self.thisptr
    def _run( self ):
        self.thisptr.run()
    def run( self ):
        interruptableCall( self._run, [] ) 
    def setLambda( self, float thislambda ):
        self.thisptr.setLambda( thislambda )
    def setMaxSamples( self, int maxSamples ):
        self.thisptr.setMaxSamples( maxSamples )
    def setEpsilon( self, float epsilon ):
        self.thisptr.setEpsilon( epsilon )
    # def setLearningRate( self, float learningRate ):
    #     self.thisptr.setLearningRate( learningRate )


#cdef void Scenario_print(  void *pyObject ):
#    (<object>pyObject).show()

#cdef void Scenario_printQRepresentation( cDeepCL.NeuralNet *net, void *pyObject ):
#    # print('Scenario_printQRepresentation')
#    scenario = <object>pyObject
#    scenario.showQ(scenario.net)

cdef void Scenario_getPerception( float *perception, void *pyObject ):
    pyPerception = (<object>pyObject).getPerception()
    for i in range(len(pyPerception)):
        perception[i] = pyPerception[i]

#[[[cog
# import ScenarioDefs
# import cog_cython
# cog_cython.pyx_write_overrideable_class( 'cDeepCL', 'CyScenario', 'Scenario',
#     ScenarioDefs.defs, ['getPerception'] )
#]]]
# generated using cog (as far as the [[end]] bit:
cdef int Scenario_getPerceptionSize(  void *pyObject ):
    return (<object>pyObject).getPerceptionSize()

cdef int Scenario_getPerceptionPlanes(  void *pyObject ):
    return (<object>pyObject).getPerceptionPlanes()

cdef void Scenario_reset(  void *pyObject ):
    (<object>pyObject).reset()

cdef int Scenario_getNumActions(  void *pyObject ):
    return (<object>pyObject).getNumActions()

cdef float Scenario_act( int index,  void *pyObject ):
    return (<object>pyObject).act(index)

cdef bool Scenario_hasFinished(  void *pyObject ):
    return (<object>pyObject).hasFinished()

cdef class Scenario:
    cdef cDeepCL.CyScenario *thisptr
    def __cinit__(self):
        self.thisptr = new cDeepCL.CyScenario(<void *>self )

        self.thisptr.setGetPerceptionSize( Scenario_getPerceptionSize )
        self.thisptr.setGetPerceptionPlanes( Scenario_getPerceptionPlanes )
        self.thisptr.setGetPerception( Scenario_getPerception )
        self.thisptr.setReset( Scenario_reset )
        self.thisptr.setGetNumActions( Scenario_getNumActions )
        self.thisptr.setAct( Scenario_act )
        self.thisptr.setHasFinished( Scenario_hasFinished )

    def getPerceptionSize(self):
        raise Exception("Method needs to be overridden: Scenario.getPerceptionSize()")

    def getPerceptionPlanes(self):
        raise Exception("Method needs to be overridden: Scenario.getPerceptionPlanes()")

    def reset(self):
        raise Exception("Method needs to be overridden: Scenario.reset()")

    def getNumActions(self):
        raise Exception("Method needs to be overridden: Scenario.getNumActions()")

    def act(self, index):
        raise Exception("Method needs to be overridden: Scenario.act()")

    def hasFinished(self):
        raise Exception("Method needs to be overridden: Scenario.hasFinished()")

#[[[end]]]
 
#    def show(self):
#        raise Exception("Method needs to be overridden: Scenario.show()")

#    def showQ(self):
#        r aise Exception("Method needs to be overridden: Scenario.showQ()")

    def getPerception(self, perception):
        raise Exception("Method needs to be overridden: Scenario.getPerception()")

