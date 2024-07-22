from controller.controllerStudent import start_student_interface
# RUN STUDENT SIDE
# Example data for testing
questions = [
    "What color is the sky?",
    "What is the capital of France?",
    "Who wrote 'Romeo and Juliet'?"
]

# Example correct answers and keywords
correct_answers = [
    "The color of the sky is blue",
    "The capital of France is Paris",
    "Shakespeare wrote 'Romeo and Juliet'"
]

keywords = [
    ["blue"],
    ["Paris"],
    ["Shakespeare"]
]

# Points for each question
points = [3, 5, 10]

if __name__ == "__main__":
    start_student_interface(questions, correct_answers, keywords, points)


# MAIN TO RUN TEACHER SIDE
# import View.gui_app as v
# import controller.sql_server_starter as sql_starter
# import controller.controllerTeacher as ct
# import Model as m
# import maskpass

# print("\n\ndo you have the my sql database?\n y/Y-yes else-no")
# letter = input()
# #pwd = input("Password for sql account:")
# pwd = maskpass.askpass(prompt="Password for sql account:", mask="#")

# if (letter.upper()=='Y'):
#     sql_starter.database_initialization(pwd)
# print(f"your letter is : {letter.upper()}")
# last_num_question,last_num_answer = sql_starter.get_last_number_question_and_answer(pwd)
# print (f"last_num_question {last_num_question} last_num_answer{last_num_answer}\n")

# app = v.GUIApp(last_num_question,last_num_answer)
# print("app number 1 has been upload...")
# control_Teacher = ct.controllerTeacher(app ,pwd)
# control_Teacher.runApp()