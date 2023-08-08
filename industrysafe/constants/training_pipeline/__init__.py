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
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["images", "labels", "classes.names", "train.txt", "val.txt"]
