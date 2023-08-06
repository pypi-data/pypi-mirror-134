import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from feature_engine.transformation import (
    LogTransformer,
    YeoJohnsonTransformer,
)
from sklearn.pipeline import Pipeline
from prediction_model.core import config
from prediction_model.features import Mapper

pipeline = Pipeline([
    ('sop_lor_mapping',Mapper(variables=config.PREDICTORS_TO_MAP,mappings=config.PREDICTOR_MAPPING)),
    ('log_transform',LogTransformer(variables=config.PREDICTORS_LOG_TRANSFORM)),
    ('yeo_transform',YeoJohnsonTransformer(variables=config.PREDICTORS_YEO_TRANSFORM)),
    ('scaler',StandardScaler()),
    ('regression',LinearRegression())
])