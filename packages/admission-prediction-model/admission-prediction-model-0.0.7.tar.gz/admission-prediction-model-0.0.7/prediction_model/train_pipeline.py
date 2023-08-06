from sklearn.model_selection import train_test_split
from prediction_model.pipeline import pipeline
from prediction_model.data_manager import load_dataset,save_pipeline
from prediction_model.core import config

def run_training() -> None:
    dataset = load_dataset(file_name=config.training_data_file)

    X_train, _ , y_train, _ = train_test_split(
        dataset.drop([config.TARGET],axis=1),
        dataset[config.TARGET],
        test_size = config.test_size,
        random_state= config.SEED
    )
    
    pipeline.fit(X_train,y_train)
    save_pipeline(pipeline_to_persist = pipeline)
    print("Pipeline saved!")

if __name__ == "__main__":
    run_training()