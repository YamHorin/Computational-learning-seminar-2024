    #TODO:
    ## write a function agent 3 that he will grade the answer base on the question 
    # and the answers from the bank
    # and give an explation of what he could do betetr
    # function will be  

import Model.cosineSimilarityMatrix as cosin

class StudentModel:
    def __init__(self):
        # self.questions = questions
        # self.answers = [""] * len(questions)  # Placeholder for student answers
        self.student_answers = []
    
    def save_answer(self, question_index, answer):
        if len(self.student_answers) <= question_index:
            self.student_answers.extend([None] * (question_index - len(self.student_answers) + 1))
        self.student_answers[question_index] = answer
        
    def get_answers(self):
        return self.answers

    def grade_answers(self, ai_answers, key_words):
        grades = []
        for i, answer in enumerate(self.answers):
            grades.append(cosin.caculateSimilarityAnswersWithKeyWordStudentToAgent(ai_answers[i], answer, key_words))
        return grades
