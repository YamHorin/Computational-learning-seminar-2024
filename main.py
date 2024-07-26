# from controller.controllerStudent import start_student_interface
# from Model.student_model import StudentModel as sm
# from Model.agentLogicGradeStudent import KevinAgent

# # RUN STUDENT SIDE
# # Example data for testing
# questions = [
#     "What year world war 2 started",
#     "What is the capital of France?",
#     "Who wrote 'Romeo and Juliet'?"
# ]

# # Example correct answers and keywords
# correct_answers = [
#     "World war 2 started in 1939",
#     "The capital of France is Paris",
#     "Shakespeare wrote 'Romeo and Juliet'"
# ]

# keywords = [
#     ["1939"],
#     ["Paris"],
#     ["Shakespeare"]
# ]

# # Points for each question
# points = [3, 5, 10]
# student_answers = [
#     "The sky is blue",
#     "The capital is Paris",
#     "Shakespeare"
# ]

# start_student_interface(questions, correct_answers, keywords, points)


# model = sm(correct_answers, keywords, points)
# grades = model.grade_answers(student_answers)

# agent = KevinAgent(correct_answers, points)
# initializer, manager, groupchat = agent.initialize_agents()

# # Start the conversation by sending a message to the group chat
# initial_message = "Provide feedback based on the following grades: " + str(grades)
# chat_result = initializer.initiate_chat(manager, message=initial_message)

# final_grade = model.final_grade(grades)
# print(f"Final test grade: {final_grade}")

# print("Final response:", chat_result)

# # Process the conversation
# while groupchat.messages:
#     manager.step()

# # Retrieve and print feedback
# # Assuming the feedback is in the last message
# feedback_message = groupchat.messages[-1]['content']
# feedback = agent.generate_feedback(feedback_message)
    
# # Print or handle the feedback as needed
# print("Feedback from Agent:")
# print(feedback)

    
#MAIN TO RUN TEACHER SIDE
import View.gui_app as v
import controller.sql_server_starter as sql_starter
import controller.controllerTeacher as ct
import model as m
import maskpass
if __name__ == "__main__":
    print("\n\ndo you have the my sql database?\n y/Y-yes else-no")
    letter = input()
    #pwd = input("Password for sql account:")
    pwd = maskpass.askpass(prompt="Password for sql account:", mask="#")

    if (letter.upper()!='Y'):
        sql_starter.database_initialization(pwd)
    print(f"your letter is : {letter.upper()}")
    sql_starter.clean_data_sql(pwd)
    last_num_question,last_num_answer = 0,0
    print (f"last_num_question {last_num_question} last_num_answer{last_num_answer}\n")

    app = v.GUIApp(last_num_question,last_num_answer)
    print("app number 1 has been upload...")
    control_Teacher = ct.controllerTeacher(app ,pwd)
    control_Teacher.runApp()