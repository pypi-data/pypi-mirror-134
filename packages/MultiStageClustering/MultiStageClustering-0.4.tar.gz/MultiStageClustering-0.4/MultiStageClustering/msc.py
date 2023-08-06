import pandas as pd
import numpy as np
from sklearn.cluster import  KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import collections 
from collections import defaultdict
import math
import warnings
import ray
pd.set_option('mode.chained_assignment',None) 
warnings.filterwarnings("ignore")

# list of columns that should be considered for clustering

   
@ray.remote
def kmeans_func(j,df):
    kmeans = KMeans(n_clusters = j)
    kmeans.fit(df)
    return j, kmeans.labels_ ,silhouette_score(df,kmeans.fit_predict(df))  
@ray.remote
def cluster_func(data,x,i,column_list,min_data_points):
    data = data[data["cluster_labels"]==x]
   
    if data.shape[0]>=min_data_points :
    
        # Initiaing two empty dictionaries for tracking the labels and silhouette_score
        dict1 = defaultdict()
        dict2 = defaultdict()


        # selecting the important features for first stage clustering
        df = data[column_list[i]]

        # Running kmeans for clusters two to nine 
        # calculating silhouette_score for all the cluster
        future_list = ray.get([kmeans_func.remote(j,df) for j in range(2,10)] )
        for value in future_list:
            dict1[value[0]]  = value[1]
            dict2[value[0]] = value[2]
        # initialising     
        max_value = -1
        max_clusters = 0

        # 
        for k in range(2,10) :
            if dict2[k] > max_value :
                max_value = dict2[k]
                max_clusters = k
        #        
        cluster_labels = dict1[max_clusters]  
        data.loc[:,'cluster_labels_next_stage'] = cluster_labels.astype(str)
        return  data
    else :
        data.loc[:,'cluster_labels_next_stage'] = '0'
        return data

def clustering(data_frame : pd.DataFrame, n : int ):

    # Checking if the provided data_frame has any null values
    if data_frame.isnull().sum().sum() > 0 :
        raise Exception("The Dataframe has atleast one null value, The Dataframe shouldn't have null values")

    # Category Column Check 
    if len(list(data_frame.select_dtypes(exclude =['number']).columns))   > 0 :
        raise Exception("The data frame has non numerical columns")  
    
    # is n the right value 
    if math.ceil(len(list(data_frame.columns))/10 ) > n :
        raise ValueError("The given n value is less than required ")
    elif math.ceil(len(list(data_frame.columns))/10 ) < n :
        raise ValueError("The given n value is greater than required ")
    else :
        pass
    
    list1 = [ i*10 for i in range(n+1) ]
    data_frame_column_list = list(data_frame.columns)
    column_list  = []
    [column_list.append(data_frame_column_list[list1[i]:list1[i+1]]) for i in range(len(list1)-1)]
    
    # creating a min_data_points in a cluster 
    min_data_points = (0.01)*(data_frame.shape[0])
    
    # initialise the dataframe dict 
    data_frame_dict ={}
    data_frame_dict[0] = data_frame
    data_frame_dict[0]['cluster_labels'] = '1'  
    for i in range(n) : 
        final_df = pd.DataFrame()  
        df_list = ray.get([cluster_func.remote(data_frame_dict[i],x,i,column_list,min_data_points) for x in list(data_frame_dict[i]["cluster_labels"].unique())])
        for z in df_list:
            final_df = pd.concat([final_df,z],axis =0)

        final_df.loc[:,"cluster_labels"] = final_df["cluster_labels"] + final_df["cluster_labels_next_stage"]
        final_df.loc[:,"cluster_labels"] = final_df["cluster_labels"].astype('category').cat.codes
        final_df.loc[:,"cluster_labels"] = final_df["cluster_labels"].astype('str')
        data_frame_dict[i+1] = final_df.drop('cluster_labels_next_stage',axis =1)
    
    return data_frame_dict[n]