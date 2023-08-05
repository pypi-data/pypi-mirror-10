// Copyright Hugh Perkins 2014 hughperkins at gmail
//
// This Source Code Form is subject to the terms of the Mozilla Public License, 
// v. 2.0. If a copy of the MPL was not distributed with this file, You can 
// obtain one at http://mozilla.org/MPL/2.0/.

#include <iostream>
#include <stdexcept>
#include <cstring>

#include "EasyCL.h"
#include "PoolingBackward.h"
#include "StatefulTimer.h"
#include "stringhelper.h"

#include "PoolingBackwardGpuNaive.h"

using namespace std;

#undef VIRTUAL
#define VIRTUAL 
#undef STATIC
#define STATIC

VIRTUAL PoolingBackwardGpuNaive::~PoolingBackwardGpuNaive() {
    delete kernel;
    delete kMemset;
}
VIRTUAL void PoolingBackwardGpuNaive::backward( int batchSize, CLWrapper *gradOutputWrapper, CLWrapper *selectorsWrapper, 
        CLWrapper *gradInputWrapper ) {

    StatefulTimer::instance()->timeCheck("PoolingBackwardGpuNaive::backward start" );

    // first, memset errors to 0 ...
    kMemset->out( gradInputWrapper )->in( 0.0f )->in( batchSize * numPlanes * inputImageSize * inputImageSize );
    int globalSize = batchSize * numPlanes * inputImageSize * inputImageSize;
    int workgroupSize = 64;
    int numWorkgroups = ( globalSize + workgroupSize - 1 ) / workgroupSize;
    kMemset->run_1d( numWorkgroups * workgroupSize, workgroupSize );
    cl->finish();

    kernel->in( batchSize )->inout( gradOutputWrapper )->in( selectorsWrapper )->in( gradInputWrapper );
    globalSize = batchSize * numPlanes * outputImageSize * outputImageSize;
    workgroupSize = 64;
    numWorkgroups = ( globalSize + workgroupSize - 1 ) / workgroupSize;
    kernel->run_1d( numWorkgroups * workgroupSize, workgroupSize );
    cl->finish();

    StatefulTimer::instance()->timeCheck("PoolingBackwardGpuNaive::backward end" );
}
PoolingBackwardGpuNaive::PoolingBackwardGpuNaive( EasyCL *cl, bool padZeros, int numPlanes, int inputImageSize, int poolingSize ) :
        PoolingBackward( cl, padZeros, numPlanes, inputImageSize, poolingSize ) {
//    std::string options = "-D " + fn->getDefineName();
    string options = "";
    options += " -D gNumPlanes=" + toString( numPlanes );
    options += " -D gInputImageSize=" + toString( inputImageSize );
    options += " -D gInputImageSizeSquared=" + toString( inputImageSize * inputImageSize );
    options += " -D gOutputImageSize=" + toString( outputImageSize );
    options += " -D gOutputImageSizeSquared=" + toString( outputImageSize * outputImageSize );
    options += " -D gPoolingSize=" + toString( poolingSize );
    options += " -D gPadZeros=" + toString( padZeros ? 1 : 0 );

    // [[[cog
    // import stringify
    // stringify.write_kernel2( "kernel", "cl/PoolingBackwardGpuNaive.cl", "backward", 'options' )
    // stringify.write_kernel2( "kMemset", "cl/memset.cl", "memset", '""' )
    // ]]]
    // generated using cog, from cl/PoolingBackwardGpuNaive.cl:
    const char * kernelSource =  
    "// Copyright Hugh Perkins 2015 hughperkins at gmail\n" 
    "//\n" 
    "// This Source Code Form is subject to the terms of the Mozilla Public License,\n" 
    "// v. 2.0. If a copy of the MPL was not distributed with this file, You can\n" 
    "// obtain one at http://mozilla.org/MPL/2.0/.\n" 
    "\n" 
    "// inplane and outplane are always identical, 1:1 mapping, so can just write `plane`\n" 
    "// gradOutput: [n][plane][outrow][outcol]\n" 
    "// selectors: [n][plane][outrow][outcol]\n" 
    "// gradInput: [n][plane][inrow][incol]\n" 
    "// wont use workgroups (since 'naive')\n" 
    "// one thread per: [n][plane][outrow][outcol]\n" 
    "// globalId: [n][plane][outrow][outcol]\n" 
    "kernel void backward( const int batchSize,\n" 
    "    global const float *gradOutput, global const int *selectors, global float *gradInput ) {\n" 
    "\n" 
    "    #define globalId get_global_id(0)\n" 
    "    #define nPlaneCombo ( globalId / gOutputImageSizeSquared )\n" 
    "    #define outputPosCombo ( globalId % gOutputImageSizeSquared )\n" 
    "\n" 
    "    const int n = nPlaneCombo / gNumPlanes;\n" 
    "    const int plane = nPlaneCombo % gNumPlanes;\n" 
    "    const int outputRow = outputPosCombo / gOutputImageSize;\n" 
    "    const int outputCol = outputPosCombo % gOutputImageSize;\n" 
    "\n" 
    "    if( n >= batchSize ) {\n" 
    "        return;\n" 
    "    }\n" 
    "\n" 
    "    int resultIndex = ( ( n\n" 
    "        * gNumPlanes + plane )\n" 
    "        * gOutputImageSize + outputRow )\n" 
    "        * gOutputImageSize + outputCol;\n" 
    "    #define error ( gradOutput[resultIndex] )\n" 
    "    int selector = ( selectors[resultIndex] );\n" 
    "    #define drow ( selector / gPoolingSize )\n" 
    "    #define dcol ( selector % gPoolingSize )\n" 
    "    #define inputRow ( outputRow * gPoolingSize + drow )\n" 
    "    #define inputCol ( outputCol * gPoolingSize + dcol )\n" 
    "    int inputIndex = ( ( n\n" 
    "        * gNumPlanes + plane )\n" 
    "        * gInputImageSize + inputRow )\n" 
    "        * gInputImageSize + inputCol;\n" 
    "//    if( n < batchSize ) {\n" 
    "        gradInput[ inputIndex ] = error;\n" 
    "//    }\n" 
    "}\n" 
    "\n" 
    "";
    kernel = cl->buildKernelFromString( kernelSource, "backward", options, "cl/PoolingBackwardGpuNaive.cl" );
    // generated using cog, from cl/memset.cl:
    const char * kMemsetSource =  
    "// Copyright Hugh Perkins 2015 hughperkins at gmail\n" 
    "//\n" 
    "// This Source Code Form is subject to the terms of the Mozilla Public License,\n" 
    "// v. 2.0. If a copy of the MPL was not distributed with this file, You can\n" 
    "// obtain one at http://mozilla.org/MPL/2.0/.\n" 
    "\n" 
    "kernel void memset( global float *target, const float value, const int N ) {\n" 
    "    #define globalId get_global_id(0)\n" 
    "    if( globalId < N ) {\n" 
    "        target[globalId] = value;\n" 
    "    }\n" 
    "}\n" 
    "\n" 
    "";
    kMemset = cl->buildKernelFromString( kMemsetSource, "memset", "", "cl/memset.cl" );
    // [[[end]]]
}

