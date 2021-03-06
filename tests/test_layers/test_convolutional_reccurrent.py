# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

from polyaxon_schemas.initializations import (
    GlorotNormalInitializerConfig,
    OrthogonalInitializerConfig,
)
from polyaxon_schemas.initializations import ZerosInitializerConfig
from polyaxon_schemas.layers.convolutional_recurrent import (
    ConvRecurrent2DConfig,
    ConvLSTM2DConfig,
)

from tests.utils import assert_equal_layers


class TestConvolutionalRecurrentConfigs(TestCase):
    def test_conv_recurrent_2d_config(self):
        config_dict = {
            'filters': 20,
            'kernel_size': 3,
            'strides': [1, 1],
            'padding': 'valid',
            'data_format': None,
            'dilation_rate': [1, 1],
            'return_sequences': False,
            'go_backwards': False,
            'stateful': False
        }
        config = ConvRecurrent2DConfig.from_dict(config_dict)
        assert_equal_layers(config, config_dict)

    def test_conv_lstm_2d_config(self):
        config_dict = {
            'filters': 20,
            'kernel_size': 3,
            'strides': [1, 1],
            'padding': 'valid',
            'data_format': None,
            'dilation_rate': [1, 1],
            'activation': 'tanh',
            'recurrent_activation': 'hard_sigmoid',
            'use_bias': True,
            'kernel_initializer': GlorotNormalInitializerConfig().to_schema(),
            'recurrent_initializer': OrthogonalInitializerConfig().to_schema(),
            'bias_initializer': ZerosInitializerConfig().to_schema(),
            'unit_forget_bias': True,
            'kernel_regularizer': None,
            'recurrent_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'recurrent_constraint': None,
            'bias_constraint': None,
            'return_sequences': False,
            'go_backwards': False,
            'stateful': False,
            'dropout': 0.,
            'recurrent_dropout': 0.
        }
        config = ConvLSTM2DConfig.from_dict(config_dict)
        assert_equal_layers(config, config_dict)
