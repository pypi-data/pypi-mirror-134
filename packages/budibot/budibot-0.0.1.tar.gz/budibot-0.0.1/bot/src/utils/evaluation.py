from sklearn.metrics import accuracy_score
import pandas as pd

class Evaluation():
    def accuracy(pred:pd.Series, ytest:pd.Series):
        return accuracy_score(pred, ytest)