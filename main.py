
import controller.controllerStudent as cs
from model.student_model import StudentModel as sm
from model.agentLogicGradeStudent import KevinAgent
import controller.sql_server_starter as sql_starter
import controller.controllerTeacher as ct
import View.login_screen as login
import View.gui_app as v
import controller.sql_server_starter as sql_starter
if __name__ == "__main__":
    opening_app = login.LoginScreen()
    opening_app.mainloop()
    pwd = opening_app.password_value
    role = opening_app.role_value
    
    if role =='student':
        controller=  cs.ControllerStudent(pwd)
        controller.start_student_interface()
    else:
        sql_starter.database_initialization(pwd)
        sql_starter.clean_data_sql(pwd)
        last_num_question,last_num_answer = 0,0
        app = v.GUIApp(last_num_question,last_num_answer)
        control_Teacher = ct.controllerTeacher(app ,pwd)
        control_Teacher.runApp()