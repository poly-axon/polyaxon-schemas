# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon_schemas.base import BaseMultiSchema
from polyaxon_schemas.layers.advanced_activations import (
    LeakyReLUConfig,
    PReLUConfig,
    ELUConfig,
    ThresholdedReLUConfig
)
from polyaxon_schemas.layers.convolutional import (
    Conv1DConfig,
    Conv2DConfig,
    Conv3DConfig,
    Conv2DTransposeConfig,
    Conv3DTransposeConfig,
    SeparableConv2DConfig,
    UpSampling1DConfig,
    UpSampling2DConfig,
    UpSampling3DConfig,
    ZeroPadding1DConfig,
    ZeroPadding2DConfig,
    ZeroPadding3DConfig,
    Cropping1DConfig,
    Cropping2DConfig,
    Cropping3DConfig,
)
from polyaxon_schemas.layers.convolutional_recurrent import ConvLSTM2DConfig, ConvRecurrent2DConfig
from polyaxon_schemas.layers.core import (
    MaskingConfig,
    DropoutConfig,
    SpatialDropout1DConfig,
    SpatialDropout2DConfig,
    SpatialDropout3DConfig,
    ActivationConfig,
    ReshapeConfig,
    PermuteConfig,
    FlattenConfig,
    RepeatVectorConfig,
    DenseConfig,
    ActivityRegularizationConfig,
    CastConfig,
)
from polyaxon_schemas.layers.embeddings import EmbeddingConfig
from polyaxon_schemas.layers.local import LocallyConnected1DConfig, LocallyConnected2DConfig
from polyaxon_schemas.layers.merge import MergeConfig
from polyaxon_schemas.layers.noise import (
    GaussianDropoutConfig,
    GaussianNoiseConfig,
    AlphaDropoutConfig
)
from polyaxon_schemas.layers.normalization import BatchNormalizationConfig
from polyaxon_schemas.layers.pooling import (
    MaxPooling1DConfig,
    AveragePooling1DConfig,
    MaxPooling2DConfig,
    AveragePooling2DConfig,
    MaxPooling3DConfig,
    AveragePooling3DConfig,
    GlobalAveragePooling1DConfig,
    GlobalMaxPooling1DConfig,
    GlobalAveragePooling2DConfig,
    GlobalMaxPooling2DConfig,
    GlobalAveragePooling3DConfig,
    GlobalMaxPooling3DConfig,
)
from polyaxon_schemas.layers.recurrent import (
    RecurrentConfig,
    GRUConfig,
    LSTMConfig,
    SimpleRNNConfig
)
from polyaxon_schemas.layers.wrappers import (
    WrapperConfig,
    TimeDistributedConfig,
    BidirectionalConfig,
)
from polyaxon_schemas.processing.image import (
    ResizeConfig,
    CentralCropConfig,
    RandomCropConfig,
    ExtractGlimpseConfig,
    ToBoundingBoxConfig,
    FlipConfig,
    TransposeConfig,
    Rotate90Config,
    ConvertColorSpaceConfig,
    ConvertImagesDtypeConfig,
    AdjustBrightnessConfig,
    AdjustContrastConfig,
    AdjustHueConfig,
    AdjustSaturationConfig,
    AdjustGammaConfig,
    StandardizationConfig,
    DrawBoundingBoxesConfig,
    TotalVariationConfig
)


class LayerSchema(BaseMultiSchema):
    __multi_schema_name__ = 'layer'
    __configs__ = {
        LeakyReLUConfig.IDENTIFIER: LeakyReLUConfig,
        PReLUConfig.IDENTIFIER: PReLUConfig,
        ELUConfig.IDENTIFIER: ELUConfig,
        ThresholdedReLUConfig.IDENTIFIER: ThresholdedReLUConfig,
        Conv1DConfig.IDENTIFIER: Conv1DConfig,
        Conv2DConfig.IDENTIFIER: Conv2DConfig,
        Conv3DConfig.IDENTIFIER: Conv3DConfig,
        Conv2DTransposeConfig.IDENTIFIER: Conv2DTransposeConfig,
        Conv3DTransposeConfig.IDENTIFIER: Conv3DTransposeConfig,
        SeparableConv2DConfig.IDENTIFIER: SeparableConv2DConfig,
        UpSampling1DConfig.IDENTIFIER: UpSampling1DConfig,
        UpSampling2DConfig.IDENTIFIER: UpSampling2DConfig,
        UpSampling3DConfig.IDENTIFIER: UpSampling3DConfig,
        ZeroPadding1DConfig.IDENTIFIER: ZeroPadding1DConfig,
        ZeroPadding2DConfig.IDENTIFIER: ZeroPadding2DConfig,
        ZeroPadding3DConfig.IDENTIFIER: ZeroPadding3DConfig,
        Cropping1DConfig.IDENTIFIER: Cropping1DConfig,
        Cropping2DConfig.IDENTIFIER: Cropping2DConfig,
        Cropping3DConfig.IDENTIFIER: Cropping3DConfig,
        ConvRecurrent2DConfig.IDENTIFIER: ConvRecurrent2DConfig,
        ConvLSTM2DConfig.IDENTIFIER: ConvLSTM2DConfig,
        MaskingConfig.IDENTIFIER: MaskingConfig,
        DropoutConfig.IDENTIFIER: DropoutConfig,
        SpatialDropout1DConfig.IDENTIFIER: SpatialDropout1DConfig,
        SpatialDropout2DConfig.IDENTIFIER: SpatialDropout2DConfig,
        SpatialDropout3DConfig.IDENTIFIER: SpatialDropout3DConfig,
        ActivationConfig.IDENTIFIER: ActivationConfig,
        ReshapeConfig.IDENTIFIER: ReshapeConfig,
        PermuteConfig.IDENTIFIER: PermuteConfig,
        FlattenConfig.IDENTIFIER: FlattenConfig,
        RepeatVectorConfig.IDENTIFIER: RepeatVectorConfig,
        DenseConfig.IDENTIFIER: DenseConfig,
        ActivityRegularizationConfig.IDENTIFIER: ActivityRegularizationConfig,
        CastConfig.IDENTIFIER: CastConfig,
        EmbeddingConfig.IDENTIFIER: EmbeddingConfig,
        LocallyConnected1DConfig.IDENTIFIER: LocallyConnected1DConfig,
        LocallyConnected2DConfig.IDENTIFIER: LocallyConnected2DConfig,
        MergeConfig.IDENTIFIER: MergeConfig,
        GaussianNoiseConfig.IDENTIFIER: GaussianNoiseConfig,
        GaussianDropoutConfig.IDENTIFIER: GaussianDropoutConfig,
        AlphaDropoutConfig.IDENTIFIER: AlphaDropoutConfig,
        BatchNormalizationConfig.IDENTIFIER: BatchNormalizationConfig,
        MaxPooling1DConfig.IDENTIFIER: MaxPooling1DConfig,
        AveragePooling1DConfig.IDENTIFIER: AveragePooling1DConfig,
        MaxPooling2DConfig.IDENTIFIER: MaxPooling2DConfig,
        AveragePooling2DConfig.IDENTIFIER: AveragePooling2DConfig,
        MaxPooling3DConfig.IDENTIFIER: MaxPooling3DConfig,
        AveragePooling3DConfig.IDENTIFIER: AveragePooling3DConfig,
        GlobalAveragePooling1DConfig.IDENTIFIER: GlobalAveragePooling1DConfig,
        GlobalMaxPooling1DConfig.IDENTIFIER: GlobalMaxPooling1DConfig,
        GlobalAveragePooling2DConfig.IDENTIFIER: GlobalAveragePooling2DConfig,
        GlobalMaxPooling2DConfig.IDENTIFIER: GlobalMaxPooling2DConfig,
        GlobalAveragePooling3DConfig.IDENTIFIER: GlobalAveragePooling3DConfig,
        GlobalMaxPooling3DConfig.IDENTIFIER: GlobalMaxPooling3DConfig,
        RecurrentConfig.IDENTIFIER: RecurrentConfig,
        SimpleRNNConfig.IDENTIFIER: SimpleRNNConfig,
        GRUConfig.IDENTIFIER: GRUConfig,
        LSTMConfig.IDENTIFIER: LSTMConfig,
        WrapperConfig.IDENTIFIER: WrapperConfig,
        TimeDistributedConfig.IDENTIFIER: TimeDistributedConfig,
        BidirectionalConfig.IDENTIFIER: BidirectionalConfig,

        # Processors
        ResizeConfig.IDENTIFIER: ResizeConfig,
        CentralCropConfig.IDENTIFIER: CentralCropConfig,
        RandomCropConfig.IDENTIFIER: RandomCropConfig,
        ExtractGlimpseConfig.IDENTIFIER: ExtractGlimpseConfig,
        ToBoundingBoxConfig.IDENTIFIER: ToBoundingBoxConfig,
        FlipConfig.IDENTIFIER: FlipConfig,
        TransposeConfig.IDENTIFIER: TransposeConfig,
        Rotate90Config.IDENTIFIER: Rotate90Config,
        ConvertColorSpaceConfig.IDENTIFIER: ConvertColorSpaceConfig,
        ConvertImagesDtypeConfig.IDENTIFIER: ConvertImagesDtypeConfig,
        AdjustBrightnessConfig.IDENTIFIER: AdjustBrightnessConfig,
        AdjustContrastConfig.IDENTIFIER: AdjustContrastConfig,
        AdjustHueConfig.IDENTIFIER: AdjustHueConfig,
        AdjustSaturationConfig.IDENTIFIER: AdjustSaturationConfig,
        AdjustGammaConfig.IDENTIFIER: AdjustGammaConfig,
        StandardizationConfig.IDENTIFIER: StandardizationConfig,
        DrawBoundingBoxesConfig.IDENTIFIER: DrawBoundingBoxesConfig,
        TotalVariationConfig.IDENTIFIER: TotalVariationConfig,
    }
