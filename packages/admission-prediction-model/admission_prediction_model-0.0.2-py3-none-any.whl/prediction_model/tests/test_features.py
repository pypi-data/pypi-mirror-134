from prediction_model.core import config
from prediction_model.features import Mapper

def test_Mapper(sample_input_data):
    mapper = Mapper(
        variables= config.PREDICTORS_TO_MAP,
        mappings= config.PREDICTOR_MAPPING
    )
    assert sample_input_data['SOP'].iat[0] == 4.5
    transform = mapper.transform(sample_input_data)
    assert transform['SOP'].iat[0] == 8
    