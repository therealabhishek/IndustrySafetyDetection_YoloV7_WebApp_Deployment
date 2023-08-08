import sys, os
from industrysafe.logger import logging
from industrysafe.exception import IndustryException
from industrysafe.components.data_ingestion import DataIngestion
from industrysafe.components.data_validation import DataValidation
from industrysafe.configuration.s3_operations import S3Operation

from industrysafe.entity.config_entity import DataIngestionConfig, DataValidationConfig

from industrysafe.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.s3_operations = S3Operation()



    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the data from URL")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact
        
        except Exception as e:
            raise IndustryException(e, sys)
        

    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifact
    ) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifact

        except Exception as e:
            raise IndustryException(e, sys) from e

        

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )

        
        except Exception as e:
            raise IndustryException(e, sys)