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
        initial_message = "Provide feedback based on the following grades and answers: " + str(grades) + str(student_answers)
        chat_result = initializer.initiate_chat(manager, message=initial_message)
        messages = groupchat.messages
        text = str(messages[-1]["content"])
        print(text)
        feedbacks, points = self.extract_feedbacks_and_points(text)
        print(f"{feedbacks} {points}")
        print(f"Final test grade: {final_grade}")
        app_finale = summary_student_answers.SummeryStudentAnswers(student_answers , self.questions , feedbacks ,points)
        app_finale.mainloop()
        self.save_students_answers_in_db(student_answers , self.questions , feedbacks ,points)
    def save_students_answers_in_db(self ,student_answers ,questions , feedbacks ,points):
        data = []
        # CREATE TABLE IF NOT EXISTS student_answers (
        #     answer_id INT AUTO_INCREMENT PRIMARY KEY,
        #     answer_text VARCHAR(2000) NOT NULL,
        #     createdBy VARCHAR(2000),
        #     question_id INT NOT NULL,
        #     grade FLOAT,
        #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        #     feedback VARCHAR(3000)
        # );
        for answer , question , feedback , points_for_answer in zip (student_answers ,questions , feedbacks ,points):
            data.append((answer , question , feedback , points_for_answer))
        self.sql_server.add_answers_students(data)
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
                    try:
                        parts = line.split(":")[1].strip().split("/")
                        awarded_points = round(float(parts[0]))
                        total_points = float(parts[1]) if len(parts) > 1 else awarded_points
                        current_points = (awarded_points, total_points)
                    except (ValueError, IndexError):
                        current_points = None
                else:
                    current_feedback.append(line)

        # Append the last feedback and points if any
        if current_feedback:
            feedbacks.append("\n".join(current_feedback))
            if current_points is not None:
                points.append(current_points)

        return feedbacks, points
