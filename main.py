from data import question_data
from question_model import Question_Model
from quiz_brain import Quiz_Brain
questions=[Question_Model(item["question"],item["correct_answer"]) for item in question_data]
game=Quiz_Brain(questions)
while game.is_more():
    game.next_question()
print(f"You completed the quiz!! Your score is {game.score}/{len(questions)}")



if __name__ == '__main__':
    pass
