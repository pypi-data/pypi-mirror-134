import pandas as pd
from sklearn.base import BaseEstimator,TransformerMixin
import typing as t
import numpy as np

class Mapper(BaseEstimator,TransformerMixin):

  def __init__(self,variables,mappings):
    if not isinstance(variables,list):
      raise ValueError('variables should be in the form of a list')
    self.variables = variables
    self.mappings = mappings
  
  def fit(self,X,y=None):
    return self
  
  def transform(self,X):
    X = X.copy()
    for feature in self.variables:
      X[feature] = X[feature].astype(str)
      X[feature] = X[feature].map(self.mappings)
      X[feature] = X[feature].astype(int)
    return X