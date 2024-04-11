from  flask import Flask, request, jsonify,render_template
#from aqi_predict.py import predict_aqi
import pickle
import bz2file as bz2
import sklearn

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

model = decompress_pickle('aqi_dt_comp.pbz2')

def predict_aqi(no2_value, o3_value,so2_value,co_value):
    
    return (model.predict([[no2_value, o3_value, so2_value, co_value]]).item())



