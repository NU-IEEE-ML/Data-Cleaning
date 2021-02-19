import numpy as np
import sklearn as sk
import sklearn.model_selection as model_selection
import sklearn.cluster as cluster
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
def data_split(path):
    data = pd.read_csv(path)
    train,test = model_selection.train_test_split(data,test_size=0.25,random_state=1)
    return train,test

def kmeans(path,n_clusters):
    train,test = data_split(path)
    kmeans = cluster.KMeans(n_clusters=n_clusters, algorithm='full')
    kmeans.fit(train)
    preds = kmeans.predict(test)
    mse = mean_squared_error(test['price'],preds)
    preds_rmse = mse **(1/2)
    print(preds_rmse)
    print(mse)


kmeans('cleaned_data.csv',4)