
class QuizBrain:

    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1} {question.text} (True/False) : ")
        user_answer = user_answer.lower()
        self.question_number += 1
        if user_answer == question.answer.lower():
            print("You Got it Right!")
            print(f"The correct answer was : {question.answer}")
            self.score += 1
        else:
            print("Incorrect answer!")
            print(f"The correct answer was : {question.answer}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)



