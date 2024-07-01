import View.gui_app as v
import controller.sql_server_starter as sql_starter
import controller.controllerTeacher as ct
import model as m

print("\n\ndo you have the my sql database?\n y/Y-yes else-no")
letter = input()

if (letter.upper()=='Y'):
    sql_starter.database_initialization()
print(f"your letter is : {letter.upper()}")
last_num_question,last_num_answer = sql_starter.get_last_number_question_and_answer()

app = v.GUIApp(last_num_question,last_num_answer)
control_Teacher = ct.controllerTeacher(app)
control_Teacher.runApp()