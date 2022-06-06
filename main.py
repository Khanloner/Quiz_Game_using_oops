from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# for data in question_data:
#     for item in data:
#         question_bank.append(data[item])
for question in question_data:
    question_txt = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_txt, question_ans)
    question_bank.append(new_question)

quiz= QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")