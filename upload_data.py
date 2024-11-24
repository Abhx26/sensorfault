from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url="mongodb+srv://sensor:12345@cluster0.7mutf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(url)

#create database name and collection name
DATABASES_NAME='abhi'
COLLECTION_NAME='wafer'
df=pd.read_csv("/Users/abhx_26/Documents/SensorFault/notebooks/wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASES_NAME][COLLECTION_NAME].insert_many(json_record)