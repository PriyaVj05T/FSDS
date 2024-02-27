import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import os
import sys
from dataclasses import dataclass
from src.DimondPricePrediction.utils.utils import save_object
from src.DimondPricePrediction.utils.utils import evaluate_model
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet

@dataclass

class ModelTrainerConfig:
    trained_model_file_path =os.path.join('artifacts','model.pkl')


class ModelTrainer:
    def __init__(self):
        pass    

    def initiate_model_training(self):
        pass