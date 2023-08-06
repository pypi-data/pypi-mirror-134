from strictyaml.parser import load
from prediction_model.validation import validate_inputs
from prediction_model.core import config
from prediction_model.data_manager import load_pipeline
import prediction_model.features
import typing as t
import pandas as pd
from .__init__ import __version__ as _version 


pipeline_file_name = f"{config.pipeline_save_file}{_version}.pkl"
_pipeline = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*,input_data: t.Union[pd.DataFrame, dict]) -> dict:
    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {'predictions': None, "version": _version, 'errors': errors}
    if not errors:
        predictions = _pipeline.predict(validated_data)
        results = {
            'predictions': predictions,
            'version': _version,
            'errors': errors,
        }
    
    return results