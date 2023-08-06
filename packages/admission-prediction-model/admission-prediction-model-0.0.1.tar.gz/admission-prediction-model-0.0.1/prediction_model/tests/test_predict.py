from prediction_model.predict import make_prediction
import math
import numpy as np

def test_make_prediction(sample_input_data):
    expected_first_prediction_value = 0.92

    result = make_prediction(input_data=sample_input_data)
    predictions = result['predictions']
    assert isinstance(predictions, np.ndarray)
    value_first_prediction = predictions[0]
    assert isinstance(value_first_prediction, float)
    assert result['errors'] is None
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=0.4)