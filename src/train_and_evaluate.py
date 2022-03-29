# load train and test
# train algorithm
# save the metrics ,params

import os
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json


def eval_matrics(test_y,pred):
    rmse = np.sqrt(mean_squared_error(test_y,pred))
    mae = mean_absolute_error(test_y,pred)
    r2 = r2_score(test_y,pred)
    return rmse,mae,r2

def train_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    model_dir = config["model_dir"]

    target = [config["base"]["target_col"]]
    print(target)
    # Loading train and test
    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)
    # removing label and seperately defining it
    train_x = train.drop(target,axis = 1)
    test_x = test.drop(target,axis = 1)

    train_y = train[target]
    test_y = test[target]
    # building model
    lr = ElasticNet(alpha = alpha,
                     l1_ratio = l1_ratio,
                     random_state= random_state)
    # Fitting model on the train
    lr.fit(train_x,train_y)
    # Predicting
    pred = lr.predict(test_x)
    # evaluation metrics
    (rmse,mae,r2) = eval_matrics(test_y,pred)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)
    
    ########################################
    scores_file = config["report"]["scores"]
    params_file = config["report"]["params"]

    with open(scores_file,"w") as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2":r2
        }
        json.dump(scores,f,indent = 4)
    
    with open(params_file,"w") as f:
        params = {
            "alpha":alpha,
            "l1_ratio":l1_ratio
        }
        json.dump(params,f,indent = 4)
    ##################################

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    train_evaluate(config_path = parsed_args.config)

