import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_data":{
        "fixed_acidity": 78,
        "volatile_acidity": 78,
        "citric_acid" : 55,
        "residual_sugar" : 12,
        "chlorides" : 15,
        "free_sulfur_dioxide" : 18,
        "total_sulfur_dioxide" : 75,
        "density" : 45,
        "pH" : 78,
        "sulphates" : 46,
        "alcohol" : 48
    },
    "correct_range":{
        "fixed_acidity": 6,
        "volatile_acidity": 5,
        "citric_acid" : 5,
        "residual_sugar" : 1,
        "chlorides" : 1,
        "free_sulfur_dioxide" : 1,
        "total_sulfur_dioxide" : 5,
        "density" : 4,
        "pH" : 3,
        "sulphates" : 4,
        "alcohol" : 4
    },
    "incorrect_col":{
        "fixed_acidity1": 6,
        "volatile_acidity": 5,
        "citric_acid" : 5,
        "residual_sugar" : 1,
        "chlorides" : 1,
        "free_sulfur_dioxide" : 1,
        "total_sulfur_dioxide" : 5,
        "density" : 4,
        "pH" : 3,
        "sulphates" : 4,
        "alcohol" : 4
    }    
}

TARGET_range = {
    "min" : 3.0,
    "max" : 8.0
}

def form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert TARGET_range["min"] <= res <= TARGET_range["max"]

def api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert TARGET_range["min"] <= res["response"] <= TARGET_range["max"]