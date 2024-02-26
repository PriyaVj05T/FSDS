
import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str= os.path.join("artifacts","raw.csv")
    train_data_path:str= os.path.join("artifacts","train.csv")
    test_data_path:str= os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        
        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","diamond.csv")))
            logging.info("Data reading started")

            os.makedirs(os.path.dirname(os.path.join("artifacts","raw.csv")),exist_ok =True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved Raw data in artifacts folder")
            logging.info("Data splitting started")
            
            train_data,test_data= train_test_split(data,test_size=.25)
            logging.info("Data splited into train and test datasets")



            #os.makedirs(os.path.join(self.ingestion_config.train_data_path),exist_ok =True)
            #os.makedirs(os.path.join(self.ingestion_config.test_data_path),exist_ok =True)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
             

            logging.info("Data ingestion completed")


        except Exception as e:
            logging.info("Exception occured during data ingestion stage")
            raise customexception(e,sys)

