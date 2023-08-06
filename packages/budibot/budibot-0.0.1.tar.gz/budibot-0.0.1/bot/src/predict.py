import pickle
import pandas as pd

from bot.src.utils.logger import Logger
from bot.src.utils.constant import Path


class Predictor():
    def __init__(self):
        self.logger = Logger("Prediction")
        self.model = self.load_model()

    def prep_data(self, data):
        with open(Path.VECTORIZER, 'rb') as file:
            vectorizer = pickle.load(file)
        
        return vectorizer.transform(data)

    def load_model(self):
        self.logger.log("load model...")
        with open(Path.MODEL, 'rb') as file:
            model = pickle.load(file)
        self.logger.log("model loaded: " + Path.MODEL)
        return model

    def predict(self, sentences):
        self.logger.log("making prediction...")
        data = self.prep_data(sentences)
        pred = self.model.predict(data)
        # print(self.model.predict_log_proba(data))
        pred_list = self.model.predict_proba(data)
        if pred_list.std() < 0.15:
            pred[0] = "other"
        return pred