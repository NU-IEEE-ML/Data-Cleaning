import numpy as np
import sklearn as sk
import sklearn.model_selection as model_selection
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error,silhouette_score,silhouette_samples


def data_split(path):
    data = pd.read_csv(path)
    train,test = model_selection.train_test_split(data,test_size=0.25,random_state=1)
    return train,test

def kmeans(path,n_clusters):
    train,test = data_split(path)
    kmeans = KMeans(n_clusters=n_clusters, algorithm='full')
    kmeans.fit(train)
    preds = kmeans.predict(test)
    range_n_clusters = [6,8,10,12,14,16,18,20,22]
    # for i in range_n_clusters:
    #     kmeans = KMeans(n_clusters=i)
    #     cluster_labels = kmeans.fit_predict(train)
    #     silhouette_avg = silhouette_score(train, cluster_labels)
    #     print("For n_clusters =", i,
    #           "The average silhouette_score is :", silhouette_avg)
    # mse = mean_squared_error(test['price'],preds)
    # preds_rmse = mse **(1/2)
    # print(preds_rmse)
    # print(mse)

def knn(path):
    train,test = data_split(path)
    knn = KNeighborsRegressor()
    knn.fit(train,train['price'])
    preds = knn.predict(test)
    mse = mean_squared_error(test['price'],preds)
    preds_rmse = mse **(1/2)
    print(preds_rmse)
    print(mse)

# kmeans('cleaned_data.csv',6)
knn('cleaned_data.csv')