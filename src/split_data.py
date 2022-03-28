# split the dataset
# save it in data\processed folder

import os
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from get_data import get_data,read_params

def split_data(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    test_path = config["split_data"]["test_path"]
    train_path = config["split_data"]["train_path"]
    raw_path = config["load_data"]["raw_dataset_csv"] 
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_path,sep = ",")
    train,test = train_test_split(df,
                 test_size = split_ratio,
                 random_state =random_state)
    train.to_csv(train_path,sep = ',',index = False,encoding = 'utf-8')
    test.to_csv(test_path,sep = ',',index = False,encoding = 'utf-8')

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    split_data(config_path = parsed_args.config)

