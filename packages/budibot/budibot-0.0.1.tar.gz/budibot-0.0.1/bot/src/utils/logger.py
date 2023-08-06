class Logger():
    def __init__(self, object_name:str):
        self.object_name = object_name

    def log(self, sentence):
        print("["+self.object_name+"] "+sentence)