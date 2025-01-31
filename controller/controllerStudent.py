

# import student agent
# import sql --> student need other tables then the teacher: need to get the test from teacher DB and save its answers to another
# initialize gui and start test taking 
#  retrieve student answer and save to DB 
# when student press DONE button --> activate function to grade each answer with cosin similarity 
#                                    then activate agent 
import re
from View.student_screen import StudentGUI
from model.student_model import StudentModel
from model.agentLogicGradeStudent import KevinAgent
import controller.sql_server as sql
import tkinter as tk
import View.summary_student_answers as summary_student_answers
from tkinter import messagebox  
class ControllerStudent ():
    def __init__(self ,pwd):
        self.sql_server = sql.sql_server( 'root',pwd,'ai_answers')


    def start_student_interface(self):
        correct_answers = self.sql_server.get_all_answers()
        questions , keywords = self.sql_server.get_all_questions()
        self.questions = questions
        if (len(correct_answers)==0 or len(questions) ==0):
            messagebox.showerror("Error", " mySQL database has no values!!")
            raise ValueError("database has no values")
        points = [q.points for q in questions]
        model = StudentModel(correct_answers, keywords, points)
        self.gui = StudentGUI(questions, model, self.on_done_callback, correct_answers, points)
        self.gui.mainloop()
        self.on_done_callback(self.gui.grades,correct_answers , points , self.gui.student_answers , self.gui.final_grade)


    def on_done_callback(self, grades, correct_answers, points, student_answers, final_grade):
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
        message = "".join (f"\n {i+1} \n question:{question.text}  \n answer{answer} \n grade:{grade} \{question.points} \n\n" for i,(question ,answer ,grade) in enumerate(zip(self.questions , student_answers , grades)))
        initial_message = "Provide feedback based on the following questions ,answers and grades :\n"+message
        print(initial_message)
        chat_result = initializer.initiate_chat(manager, message=initial_message)
        messages = groupchat.messages
        text = str(messages[-1]["content"])
        print(text)
        feedbacks = self.extract_feedbacks_and_points(text)
        points = [(grade , question.points) for (grade , question) in zip (grades , self.questions) ]
        print(f"{feedbacks} {points}")
        print(f"Final test grade: {final_grade}")
        app_finale = summary_student_answers.SummeryStudentAnswers(student_answers , self.questions , feedbacks ,points , final_grade)
        app_finale.mainloop()
        self.sql_server.save_student_answers(student_answers , points , feedbacks)
    def extract_feedbacks_and_points(self ,text):
        lines = text.splitlines()
        feedbacks = []
        points = []
        current_feedback = []
        feedback_start = None
        current_points = None

        for i, line in enumerate(lines):
            if line.startswith("Feedback for Question"):
                if current_feedback:
                    # Append the previous feedback and points
                    feedbacks.append("\n".join(current_feedback))
                    if current_points is not None:
                        points.append(current_points)
                    current_feedback = []
                    current_points = None

                feedback_start = i
                question_number = line.split(":")[0].split()[-1]  # Extract question number
                current_feedback.append(f"Feedback for question {question_number}:")
            elif feedback_start is not None:
                if line.startswith("Points:"):
                    # Extract points information
                        match = re.search(r'Points:\s*(\d+)/(\d+)', text)
                        if match:
                            current_points = (int(match.group(1)), int(match.group(2)))
                            print(points)
                        else:
                            print("could not find points!!!!")
                            current_points = None
                else:
                    current_feedback.append(line)

        # Append the last feedback and points if any
        if current_feedback:
            feedbacks.append("\n".join(current_feedback))
            if current_points is not None:
                points.append(current_points)

        return feedbacks
