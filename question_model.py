class Question_Model:
    def __init__(self,txt,ans):
        self.txt=txt
        self.ans=ans
    def print(self):
        print(f"{self.txt}\n{self.ans}")