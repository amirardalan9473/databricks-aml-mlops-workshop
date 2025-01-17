import json
import random
import pickle
import numpy
import os
import joblib

def init():
    global model
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "model.pkl"
    )
    # deserialize the model file back into a sklearn model
    # model = pickle.load(open(model_path,'rb'))
    model = joblib.load(model_path)

def run(raw_data):
    data = json.loads(raw_data)["data"]
    # data = numpy.array(data).reshape(-1, 1)
    result = model.predict(data)
    return result.tolist()
