from pathlib import Path
import typing as t
from joblib import load,dump
import pandas as pd
import prediction_model.features as features
from sklearn.pipeline import Pipeline
from prediction_model.core import config,DATASET_DIR,TRAINED_MODEL_DIR
from .__init__ import __version__ as _version #could change

#_version = 2.0

def load_dataset(*,file_name:str) -> pd.DataFrame:
    dataset = pd.read_csv(Path(f'{DATASET_DIR}/{file_name}'))
    dataset = dataset.rename(columns= config.variables_to_rename)
    try:
        dataset.drop(config.columns_to_drop,axis=1,inplace=True)
    except:
        pass
    return dataset

def remove_old_pipeline(*, files_to_keep: t.List[str]) -> None:
    do_not_delete = files_to_keep + ['__init__.py']
    for model_file in Path(TRAINED_MODEL_DIR).iterdir():
        if model_file not in do_not_delete:
            model_file.unlink()

def save_pipeline(*,pipeline_to_persist: Pipeline) -> None:
    save_file_name = f'{config.pipeline_save_file}{_version}.pkl'
    save_path = Path(TRAINED_MODEL_DIR) / save_file_name
    remove_old_pipeline(files_to_keep = [save_file_name])
    dump(pipeline_to_persist, save_path)

def load_pipeline(*,file_name: str) -> Pipeline:
    load_path = Path(TRAINED_MODEL_DIR) / file_name
    return load(filename=load_path)