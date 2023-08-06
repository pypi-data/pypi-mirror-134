from typing import Optional,Tuple,Dict,List
import pandas as pd
from prediction_model.core import config
from pydantic import BaseModel, ValidationError

def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[Dict]]:
    
    input_data.rename(columns=config.variables_to_rename, inplace=True)
    relevant_data = input_data[config.PREDICTORS].copy()
    errors = None

    try:
        MultiplePredictionInputs(inputs=relevant_data.to_dict(orient="records"))
    
    except ValidationError as error:
        errors = error.json()

    return relevant_data,errors

class PredictionSchema(BaseModel):
    GRE: Optional[int]
    TOEFL: Optional[int]
    Rating: Optional[int]
    SOP: Optional[float]
    LOR: Optional[float]
    CGPA: Optional[float]
    Research: Optional[int]

class MultiplePredictionInputs(BaseModel):
    inputs: List[PredictionSchema]