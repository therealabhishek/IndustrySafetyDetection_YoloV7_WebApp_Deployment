import os

ARTIFACTS_DIR:str = "artifacts"

"""
Data Ingestion Constants
"""

DATA_INGESTION_DIR_NAME = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"

DATA_INGESTION_S3_DATA_NAME = "isd_data_mini.zip"

DATA_BUCKET_NAME = "indsafe-data"


"""
Data Validation Constants
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["images", "labels", "classes.names", "train.txt", "val.txt"]


"""
Model Trainer Constants
"""

MODEL_TRAINER_DIR_NAME:str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_URL = "https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt"

MODEL_TRAINER_NO_EPOCHS:int = 1

MODEL_TRAINER_BATCH_SIZE:int = 8


"""
Model Pusher Constants
"""
MODEL_BUCKET_NAME = "indsafe-model"
S3_MODEL_NAME = "best.pt"