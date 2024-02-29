from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData
custdataobj= CustomData(2.03,62.0,58.0,8.06,8.12,5.05,"Very Good","J","SI2")
data = custdataobj.get_data_as_dataframe()
print(data)