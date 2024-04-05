from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data[0]['results']:
    y = Question(i['question'], i['correct_answer'])
    question_bank.append(y)
# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
final = quiz.final_answer()
print("You've completed the quiz")
print(f"Your final score was: {final}")
