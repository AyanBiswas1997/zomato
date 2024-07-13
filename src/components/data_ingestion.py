import os
from dataclasses import dataclass
import sys
from src.exception import customexception
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class dataingestionconfig():
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")
class dataingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()
    def initiate_dataingestion(self):
        logging.info("write the data ingestion method")
        try:
            df=pd.read_csv('Notebook\Data\zomato.csv')
            logging.info("read the dataset")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("traintest spilit initiated")
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingestion data completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise customexception(e,sys)
if __name__=='__main__':
    obj=dataingestion()
    obj.initiate_dataingestion()





