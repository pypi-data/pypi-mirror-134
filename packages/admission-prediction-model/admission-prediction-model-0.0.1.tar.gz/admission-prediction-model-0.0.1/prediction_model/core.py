from pathlib import Path
from typing import Dict, List
from strictyaml import YAML,load
from pydantic import BaseModel
#import __init__ as core#could change

PACKAGE_ROOT = Path(".").resolve()
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models/"
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"

class Config(BaseModel):
    variables_to_rename : Dict
    columns_to_drop : List
    pipeline_save_file : str
    training_data_file : str
    test_size : float
    SEED : int
    TARGET : str
    PREDICTORS : List
    PREDICTORS_DISCRETE : List
    PREDICTOR_MAPPING : Dict
    PREDICTORS_TO_MAP : List
    PREDICTORS_LOG_TRANSFORM : List
    PREDICTORS_YEO_TRANSFORM : List

def find_config_file() -> Path:
    if Path(CONFIG_FILE_PATH).is_file():
        return CONFIG_FILE_PATH
    raise Exception(f'Config not found at {CONFIG_FILE_PATH}')

def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    if not cfg_path:
        cfg_path = find_config_file()
    if cfg_path:
        with open(cfg_path,"r") as config_file:
            parsed_config = load(config_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at {cfg_path}")

def create_and_validate_config(parsed_config: YAML = None) -> Config:
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()
    
    _config = Config(**parsed_config.data)
    return _config

config = create_and_validate_config()