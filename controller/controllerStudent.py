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
        self.gui = StudentGUI(questions, model, self.on_done_callback, correct_answers, points)
        self.gui.mainloop()
        self.on_done_callback(self.gui.grades, correct_answers, points, self.gui.student_answers, self.gui.final_grade)

    def save_student_answers(self, student_answers, grades):
        for i, (answer, grade) in enumerate(zip(student_answers, grades)):
            question_id = i + 1  # Assuming question IDs start from 1
            grade = float(grade) if grade is not None else None
            self.sql_server.add_student_answer(answer, "student", question_id, grade)


    def on_done_callback(self, grades, correct_answers, points, student_answers, final_grade):
        self.save_student_answers(student_answers, grades)
        correct_answers = [answer.text for answer in correct_answers]
        agent = KevinAgent(correct_answers, points)
        initializer, manager, groupchat = agent.initialize_agents()
 
        # Prepare a detailed message for the agent
        initial_message = "Provide feedback based on the following information:\n"
        for i, (grade, answer, correct, point) in enumerate(zip(grades, student_answers, correct_answers, points), 1):
            initial_message += f"Question {i}:\n"
            initial_message += f"Student's answer: {answer}\n"
            initial_message += f"Correct answer: {correct}\n"
            initial_message += f"Student's grade: {grade}/{point}\n\n"

        initial_message += f"Total points possible: {sum(points)}\n"
        initial_message += f"Total points earned: {sum(grades)}\n"
        initial_message += f"Please provide feedback for each question and calculate the final grade."
        # Start the conversation by sending a message to the group chat
        chat_result = initializer.initiate_chat(manager, message=initial_message)

        # Extract the last message from the chat result
        last_message = chat_result.chat_history[-1]['content'] if chat_result.chat_history else "No feedback provided"

        # Generate and print the feedback
        feedback = agent.generate_feedback(last_message)
        print(feedback)

        print(f"Calculated final grade: {final_grade}")
        # initial_message += f"Total points possible: {sum(points)}"
        # # initial_message = "Provide feedback based on the following grades and answers: " + str(grades) + str(student_answers)
        # chat_result = initializer.initiate_chat(manager, message=initial_message)
        # # Extract the last message from the chat result
        # last_message = chat_result.chat_history[-1]['content'] if chat_result.chat_history else "No feedback provided"

        # # Generate and print the feedback
        # feedback = agent.generate_feedback(last_message)
        # print(feedback)

        # print(f"Final test grade: {final_grade}")
 