from src.End_to_End_ML_Project import logger
from src.End_to_End_ML_Project.logger import logging     # either of both we can use

from src.End_to_End_ML_Project.exception import CustomException
import sys

from src.End_to_End_ML_Project.components.data_ingestion import DataIngestionConfig
from src.End_to_End_ML_Project.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
#        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
        