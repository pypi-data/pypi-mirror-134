import pandas as pd
from fuzzywuzzy import fuzz

from bot.src.predict import Predictor
from bot.src.utils.constant import Path
from bot.src.utils.nlp import Natural_Language_Processing


class Chat():
    def __init__(self):
        self.fruit = ['jeruk', 'apel', 'anggur', 'alpukat', 'durian', 'mangga']
        self.predictor = Predictor()
        self.response = self.load_response()
        self.nlp_tools = Natural_Language_Processing()

    def fruit_check(self, sentences):
        sentences = list(sentences)
        for sentence in sentences:
            sentence = sentence.split(" ")
            fruit_list = []
            for i in sentence:
                for j in self.fruit:
                    score = fuzz.ratio(i,j)
                    if score >= 85:
                        fruit_list.append(j)
        return fruit_list
    
    def prep_data(self, sentence):
        data = pd.Series(sentence)
        data = self.nlp_tools.clean(data)
        return data 

    def load_response(self):
        data = pd.read_csv(Path.RESPONSE)
        return data
    
    def get_response(self, pred, fruit):
        res = ""
        if fruit == []:
            fruit = 0
        if pred[0] == "other":
            res = "Mohon maaf tapi kami tidak mengerti apa yang anda maksud"
        elif pred == "ask_product":
            res = eval(self.response[self.response['label'] == "ask_product"]['response'].iloc[0])
            if fruit == 0:
                res = res[0]
            else:
                fruit = ", ".join(fruit)
                res = res[1] + fruit
        elif pred == "buy":
            res = eval(self.response[self.response['label'] == "buy"]['response'].iloc[0])
            if fruit == 0:
                res = res[1]
            else:
                fruit = ", ".join(fruit)
                res = res[0] + fruit
        else:
            temp = self.response[self.response['label'] == pred[0]]
            if fruit != 0:
                for i in fruit:
                    res = res + temp[temp['fruit'] == i]['response'].iloc[0] + "\n"
            else:
                res = temp[temp['fruit'] == str(fruit)]['response'].iloc[0]
        return res

    def __call__(self, sentence):
        sentence = self.prep_data(sentence)
        pred = self.predictor.predict(sentence)
        print(pred)
        fruit = self.fruit_check(sentence)
        response = self.get_response(pred, fruit)
        return response

if __name__ == "__main__":
    chatbot = Chat()
    sentence = input("input: ")
    while sentence != "quit":
        print("Chabot: " + chatbot(sentence))
        sentence = input("input: ")
    