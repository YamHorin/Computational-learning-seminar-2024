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


    def start_student_interface(self):
       

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