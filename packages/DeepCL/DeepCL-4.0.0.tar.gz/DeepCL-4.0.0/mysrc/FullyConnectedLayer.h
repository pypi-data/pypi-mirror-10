// Copyright Hugh Perkins 2015 hughperkins at gmail
//
// This Source Code Form is subject to the terms of the Mozilla Public License, 
// v. 2.0. If a copy of the MPL was not distributed with this file, You can 
// obtain one at http://mozilla.org/MPL/2.0/.

#pragma once

#include "Layer.h"
#include "ConvolutionalLayer.h"

class FullyConnectedMaker;

#define VIRTUAL virtual
#define STATIC static

class FullyConnectedLayer : public Layer {
public:
    const int numPlanes;
    const int imageSize;
//    ActivationFunction const*fn;

    ConvolutionalLayer *convolutionalLayer;
    int batchSize;

    // [[[cog
    // import cog_addheaders
    // cog_addheaders.add()
    // ]]]
    // generated, using cog:
    FullyConnectedLayer( EasyCL *cl, Layer *previousLayer, FullyConnectedMaker *maker );
    VIRTUAL ~FullyConnectedLayer();
    VIRTUAL std::string getClassName() const;
    VIRTUAL void setBatchSize( int batchSize );
    VIRTUAL int getOutputCubeSize() const;
    VIRTUAL int getOutputImageSize() const;
    VIRTUAL int getOutputPlanes() const;
    VIRTUAL int getPersistSize() const;
    VIRTUAL void persistToArray(float *array);
    VIRTUAL void unpersistFromArray(float const*array);
    VIRTUAL void setWeights( float *weights, float *bias );
    VIRTUAL int getWeightsSize() const;
    VIRTUAL int getBiasSize() const;
    VIRTUAL int getOutputSize() const;
    VIRTUAL float *getOutput();
    VIRTUAL float *getGradInput();
    VIRTUAL CLWrapper *getGradWeightsWrapper();
    VIRTUAL CLWrapper *getGradBiasWrapper();
    VIRTUAL CLWrapper *getWeightsWrapper();
    VIRTUAL CLWrapper *getBiasWrapper();
    VIRTUAL bool biased();
    VIRTUAL bool providesGradInputWrapper() const;
    VIRTUAL CLWrapper *getGradInputWrapper();
    VIRTUAL bool hasOutputWrapper() const;
    VIRTUAL CLWrapper *getOutputWrapper();
    VIRTUAL bool needsBackProp();
    VIRTUAL void forward();
    VIRTUAL void backward();
    VIRTUAL bool needsTrainerState() const;
    VIRTUAL TrainerState *getTrainerState();
    VIRTUAL TrainerState *getBiasTrainerState();
    VIRTUAL void setTrainerState( TrainerStateMaker *TrainerStateMaker );
    VIRTUAL std::string asString() const;

    // [[[end]]]
};

