import subprocess

# import student agent
# import sql --> student need other tables then the teacher: need to get the test from teacher DB and save its answers to another
# initialize gui and start test taking 
#  retrieve student answer and save to DB 
# when student press DONE button --> activate function to grade each answer with cosin similarity 
#                                    then activate agent 

from View.student_screen import StudentGUI
from model.student_model import StudentModel
from model.agentLogicGradeStudent import KevinAgent
import controller.sql_server as sql
class ControllerStudent ():
    def __init__(self ,pwd):
        self.sql_server = sql.sql_server( 'root',pwd,'ai_answers')


    def start_student_interface(self ,questions, correct_answers, keywords, points):
       

        correct_answers = self.sql_server.get_all_answers()
        questions , keywords = self.sql_server.get_all_questions()
        points = [q.points for q in questions]
        model = StudentModel(correct_answers, keywords, points)
        gui = StudentGUI(questions, model, self.on_done_callback, correct_answers, points)
        gui.mainloop()
        #TODO save answers

    def on_done_callback(grades, correct_answers, points, student_answers, final_grade):
        # Initialize the agent with correct answers and points
        # agent = KevinAgent(correct_answers, points)
        # initializer, manager, groupchat = agent.initialize_agents()
        
        # # Provide feedback using the grades
        # feedback = agent.provide_feedback(grades)
        
        # # Print or handle the feedback as needed
        # print("Feedback from Agent:")
        # print(feedback)
        correct_answers = [answer.text for answer in correct_answers]
        agent = KevinAgent(correct_answers, points)
        initializer, manager, groupchat = agent.initialize_agents()

        # Start the conversation by sending a message to the group chat
        initial_message = "Provide feedback based on the following grades and answers: " + str(grades) + str(student_answers)
        chat_result = initializer.initiate_chat(manager, message=initial_message)

        print(f"Final test grade: {final_grade}")


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


