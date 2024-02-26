from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd
import os
import sys

obj = DataIngestion()
obj.initiate_data_ingestion()