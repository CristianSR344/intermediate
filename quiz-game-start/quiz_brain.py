class QuizzBrain():
    
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
        
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)
        
    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answarer is {correct_answer}")
        print(f"Your current score is: {self.score} / {self.q_number}")
        print("\n")
