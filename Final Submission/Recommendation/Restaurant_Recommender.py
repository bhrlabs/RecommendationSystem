"""
Restaurant Recommendation System
Using Yelp Dataset
"""

import numpy as np
from sklearn.neighbors import KDTree
from sklearn import preprocessing
import csv

# CSV with Business IDs and Coordinates
coordinate_file = "Features/Coordinates_Phoenix.csv"
user_feature_file = "Features/"
res_features_file = "Features/"
res_file = "Restaurants_Details_PHX.csv"


def get_user_feature(user_id):
    user_feature = []
    with open(user_feature_file, 'rb') as inp:
        pass

    return user_feature


def get_res_features(res_ids):
    res_features = []
    with open(res_features_file, 'rb') as inp:
        pass

    return res_features


# Get K nearest neighbors to the inputted user coordinates.
def get_knn(cod):
    # Load all Coordinates
    X = []
    res_ids = []
    with open(coordinate_file, 'rb') as inp:
        header = True
        for row in csv.reader(inp):
            if header:
                header = False
                continue
            X.append(row[1:])
            res_ids.append(row[0])

    X = np.asarray(X)

    # Finding K nearest neighbors using KD Tree
    tree = KDTree(X, leaf_size=2)
    dist, ind = tree.query(cod, k=25)

    res_ids_dist = []
    for i in ind:
        res_ids_dist.append([res_ids[i], dist[i]])

    return res_ids_dist


# Scaling distances on the scale of 0 to 1
def scale_dist(dist):
    minmaxscaler = preprocessing.MinMaxScaler(feature_range=(0, 1), copy=True)
    dist = np.asarray(dist)
    scaled_dist = minmaxscaler.fit_transform(dist[0])
    return scaled_dist


if __name__ == '__main__':

    # User latitude and longitude as Input
    cod = [33.4, 112.0]
    cod[0] = float(raw_input("Enter the latitude: Like 33.4 something "))
    cod[1] = float(raw_input("Enter the longitude: Like 112.0 something "))

    # User ID as Input
    user_id = str(raw_input("Enter User ID:"))

    user_feature = get_user_feature(user_id)

    res_ids_dist = get_knn(cod)

    res_features = get_res_features(res_ids_dist[:1])

    ratings = res_features.dot(user_feature)

    scaled_dist = scale_dist(res_ids_dist[1:])

    res_ids_dist[1:] = scaled_dist

    #Sort in descending order of distances


    pass



