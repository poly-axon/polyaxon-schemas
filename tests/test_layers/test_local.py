# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

from polyaxon_schemas.initializations import ZerosInitializerConfig, GlorotUniformInitializerConfig
from polyaxon_schemas.layers.local import LocallyConnected1DConfig, LocallyConnected2DConfig

from tests.utils import assert_equal_layers


class TestLocalConfigs(TestCase):
    @staticmethod
    def assert_local_config(local_class, dim):
        config_dict = {
            'filters': 20,
            'kernel_size': 3,
            'strides': 1 if dim == 1 else [1, 1],
            'padding': 'valid',
            'data_format': None,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': GlorotUniformInitializerConfig().to_schema(),
            'bias_initializer': ZerosInitializerConfig().to_schema(),
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None,
        }
        if dim > 1:
            config_dict['data_format'] = None
        config = local_class.from_dict(config_dict)
        assert_equal_layers(config, config_dict)

    def test_local_config(self):
        self.assert_local_config(LocallyConnected1DConfig, 1)
        self.assert_local_config(LocallyConnected2DConfig, 2)
