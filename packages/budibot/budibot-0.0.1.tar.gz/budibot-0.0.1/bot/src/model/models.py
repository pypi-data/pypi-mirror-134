from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
class Models():
    def get_multinomialnb():
        return MultinomialNB()
    def get_svc():
        return SVC()