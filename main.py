import controller.controllerStudent as cs
from model.student_model import StudentModel as sm
from model.agentLogicGradeStudent import KevinAgent
import View.gui_app as v
import controller.sql_server_starter as sql_starter
import controller.controllerTeacher as ct
import maskpass
import subprocess
# RUN STUDENT SIDE
# Example data for testing


pwd = maskpass.askpass(prompt="Password for sql account:", mask="#")
controller=  cs.ControllerStudent(pwd)
controller.start_student_interface()


    
# #MAIN TO RUN TEACHER SIDE
# import View.gui_app as v
# import controller.sql_server_starter as sql_starter
# import controller.controllerTeacher as ct
# import model as m
# import maskpass
# import subprocess
# if __name__ == "__main__":
#     #subprocess.check_call(["ollama", "pull", "llama3"])

#     print("\n\ndo you have the my sql database?\n y/Y-yes else-no")
#     letter = input()
#     #pwd = input("Password for sql account:")
#     pwd = maskpass.askpass(prompt="Password for sql account:", mask="#")

#     if (letter.upper()!='Y'):
#         sql_starter.database_initialization(pwd)
#     print(f"your letter is : {letter.upper()}")
#     sql_starter.clean_data_sql(pwd)
#     last_num_question,last_num_answer = 0,0

#     app = v.GUIApp(last_num_question,last_num_answer)
#     control_Teacher = ct.controllerTeacher(app ,pwd)
#     control_Teacher.runApp()