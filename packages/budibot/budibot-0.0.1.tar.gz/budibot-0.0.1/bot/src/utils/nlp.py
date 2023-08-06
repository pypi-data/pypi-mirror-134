from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import pandas as pd
import string


from bot.src.utils.logger import Logger

class Natural_Language_Processing():
    
    def __init__(self):
        self.stemmer = StemmerFactory().create_stemmer()
        self.remover = StopWordRemoverFactory().create_stop_word_remover()
        
        self.logger = Logger("Data Cleaning")

    def stemming(self, sentence):     
        return self.stemmer.stem(sentence)

    def remove_stopwords(self, sentence):
        return self.remover.remove(sentence)

    def clean_punc(self, sentence):
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        return sentence
    
    def clean(self, series):
        self.logger.log('removing punctuation...')
        series = series.apply(self.clean_punc)
        self.logger.log('stemming...')
        series = series.apply(self.stemming)
        self.logger.log('removing stop words...')
        series = series.apply(self.remove_stopwords)

        return series