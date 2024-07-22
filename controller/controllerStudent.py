import subprocess

# import student agent
# import sql --> student need other tables then the teacher: need to get the test from teacher DB and save its answers to another
# initialize gui and start test taking 
#  retrieve student answer and save to DB 
# when student press DONE button --> activate function to grade each answer with cosin similarity 
#                                    then activate agent 

from View.student_screen import StudentGUI
from Model.student_model import StudentModel
from Model.agentLogicGradeStudent import KevinAgent

def start_student_interface(questions, correct_answers, keywords, points):
    model = StudentModel(correct_answers, keywords, points)
#    gui = StudentGUI(questions, model, on_done_callback)
    gui = StudentGUI(questions, model, on_done_callback, correct_answers, points)
    gui.mainloop()

def on_done_callback(grades, correct_answers, points):
     # Initialize the agent with correct answers and points
    agent = KevinAgent(correct_answers, points)
    initializer, manager, groupchat = agent.initialize_agents()
    
    # Provide feedback using the grades
    feedback = agent.provide_feedback(grades)
    
    # Print or handle the feedback as needed
    print("Feedback from Agent:")
    print(feedback)


# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
       
# from Model.agentLogicGradeStudent import StudentModel
# # import model.agentLogicGradeStudent as student_model
# from View import student_screen as StudentGUI


# class StudentController:
#     def __init__(self, questions, ai_answers, key_words):
#         self.model = StudentModel()
#         self.view = StudentGUI(questions, self)
#         self.ai_answers = ai_answers
#         self.key_words = key_words

#     def run(self):
#         self.view.mainloop()

#     def save_answer(self, question_index, answer):
#         self.model.save_answer(question_index, answer)

#     def get_answer(self, index):
#         return self.model.get_answers()[index]

#     def done_pressed(self):
#         student_answers = self.model.get_answers()
#         for i, answer in enumerate(student_answers):
#             similarity = self.model.calculate_similarity(self.ai_answers[i], answer, self.key_words)
#             print(f"Question {i+1}: Similarity Score = {similarity}")
#         # Here you can activate the agent
#         print("STUDENT DONE")
#         self.view.destroy()

# # Example usage:
# questions = [
#     "What color is the sky?",
#     "What is the capital of France?",
#     "Who wrote 'Romeo and Juliet'?"
# ]

# ai_answers = [
#     "The sky is blue.",
#     "blue",
#     "The color of the sky is blue.",
#     "They are blue."
# ]

# key_words = [
#     ["blue", "sky"]
# ]

# controller = StudentController(questions, ai_answers, key_words)
# controller.run()


