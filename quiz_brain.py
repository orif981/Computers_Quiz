class Quiz_Brain:
    def __init__(self,questions):
        self.question_number,self.score=0,0
        self.questions=questions
    def next_question(self):
        response=input(f"Q{self.question_number+1}. {self.questions[self.question_number].txt} (True/False):   ").lower()
        self.question_number+=1
        if self.check_answer(response):
            self.score+=1
            print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    def is_more(self): return self.question_number<len(self.questions)
    def check_answer(self,response):
        return response==self.questions[self.question_number-1].ans.lower()

