from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_intgestion import DataIngestion
from src.mlproject.components.data_intgestion import DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custon Exception")
        raise CustomException(e, sys)

    