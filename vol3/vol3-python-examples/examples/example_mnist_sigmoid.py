#!/usr/bin/env python
"""
    Artificial Intelligence for Humans
    Volume 3: Deep Learning and Neural Networks
    Python Version
    http://www.aifh.org
    http://www.jeffheaton.com
    Code repository:
    https://github.com/jeffheaton/aifh
    Copyright 2015 by Jeff Heaton
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    For more information on Heaton Research copyrights, licenses
    and trademarks visit:
    http://www.heatonresearch.com/copyright
"""
import lasagne
from lib.aifh.mnist import *
import theano
import theano.tensor as T
import time
from lasagne.layers import DenseLayer
from lasagne.layers import InputLayer
from lasagne.nonlinearities import sigmoid
from lasagne.nonlinearities import softmax
from lasagne.nonlinearities import rectify
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet

layers0 = [('input', InputLayer),
           ('dense0', DenseLayer),
           ('output', DenseLayer)]

net0 = NeuralNet(layers=layers0,
    input_shape=(None, 28*28),
    dense0_num_units=800,
    dense0_nonlinearity = sigmoid,
    output_num_units=10,
    output_nonlinearity=softmax,

    update=nesterov_momentum,
    update_learning_rate=0.01,
    update_momentum=0.9,
    regression=False,

    eval_size=0.1,
    verbose=1,
    max_epochs=1000)

X_train, y_train, X_val, y_val, X_test, y_test = load_dataset(False)

net0.fit(X_train, y_train)