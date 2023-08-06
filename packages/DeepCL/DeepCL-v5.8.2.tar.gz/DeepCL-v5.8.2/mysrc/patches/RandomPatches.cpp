// Copyright Hugh Perkins 2014 hughperkins at gmail
//
// This Source Code Form is subject to the terms of the Mozilla Public License, 
// v. 2.0. If a copy of the MPL was not distributed with this file, You can 
// obtain one at http://mozilla.org/MPL/2.0/.

#include <iostream>

#include "net/NeuralNet.h"
#include "layer/Layer.h"
#include "RandomPatches.h"
#include "RandomPatchesMaker.h"
#include "util/RandomSingleton.h"
#include "PatchExtractor.h"

using namespace std;

#undef VIRTUAL
#define VIRTUAL 
#undef STATIC
#define STATIC

RandomPatches::RandomPatches( Layer *previousLayer, RandomPatchesMaker *maker ) :
        Layer( previousLayer, maker ),
        patchSize( maker->_patchSize ),
        numPlanes ( previousLayer->getOutputPlanes() ),
        inputImageSize( previousLayer->getOutputImageSize() ),
        outputImageSize( maker->_patchSize ),
        output(0),
        batchSize(0),
        allocatedSize(0) {
    if( inputImageSize == 0 ) {
//        maker->net->print();
        throw runtime_error("Error: Pooling layer " + toString( layerIndex ) + ": input image size is 0" );
    }
    if( outputImageSize == 0 ) {
//        maker->net->print();
        throw runtime_error("Error: Pooling layer " + toString( layerIndex ) + ": output image size is 0" );
    }
    if( previousLayer->needsBackProp() ) {
        throw runtime_error("Error: RandomPatches layer does not provide backprop currently, so you cannot put it after a layer that needs backprop");
    }
}
VIRTUAL RandomPatches::~RandomPatches() {
    if( output != 0 ) {
        delete[] output;
    }
}
VIRTUAL std::string RandomPatches::getClassName() const {
    return "RandomPatches";
}
VIRTUAL void RandomPatches::setBatchSize( int batchSize ) {
    if( batchSize <= allocatedSize ) {
        this->batchSize = batchSize;
        return;
    }
    if( output != 0 ) {
        delete[] output;
    }
    this->batchSize = batchSize;
    this->allocatedSize = batchSize;
    output = new float[ getOutputSize() ];
}
VIRTUAL int RandomPatches::getOutputSize() {
    return batchSize * numPlanes * outputImageSize * outputImageSize;
}
VIRTUAL float *RandomPatches::getOutput() {
    return output;
}
VIRTUAL bool RandomPatches::needsBackProp() {
    return false;
}
VIRTUAL int RandomPatches::getOutputSize() const {
    return batchSize * numPlanes * outputImageSize * outputImageSize;
}
VIRTUAL int RandomPatches::getOutputImageSize() const {
    return outputImageSize;
}
VIRTUAL int RandomPatches::getOutputPlanes() const {
    return numPlanes;
}
VIRTUAL int RandomPatches::getPersistSize() const {
    return 0;
}
VIRTUAL bool RandomPatches::providesGradInputWrapper() const {
    return false;
}
VIRTUAL bool RandomPatches::hasOutputWrapper() const {
    return false;
}
VIRTUAL void RandomPatches::forward() {
    float *upstreamOutput = previousLayer->getOutput();
    for( int n = 0; n < batchSize; n++ ) {
        int patchMargin = inputImageSize - outputImageSize;
        int patchRow = patchMargin / 2;
        int patchCol = patchMargin / 2;
        if( training ) {
            patchRow = RandomSingleton::instance()->uniformInt( 0, patchMargin );
            patchCol = RandomSingleton::instance()->uniformInt( 0, patchMargin );
        }
        PatchExtractor::extractPatch( n, numPlanes, inputImageSize, patchSize, patchRow, patchCol, upstreamOutput, output );
    }
}
VIRTUAL std::string RandomPatches::asString() const {
    return "RandomPatches{ inputPlanes=" + toString(numPlanes) + " inputImageSize=" + toString(inputImageSize) + " patchSize=" + toString( patchSize ) + " }";
}


