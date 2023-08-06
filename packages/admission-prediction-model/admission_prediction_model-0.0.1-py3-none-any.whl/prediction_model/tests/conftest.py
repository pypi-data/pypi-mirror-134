import pytest
from prediction_model.core import config
from prediction_model.data_manager import load_dataset

@pytest.fixture
def sample_input_data():
    return load_dataset(file_name=config.training_data_file)