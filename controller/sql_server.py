#before use this file need install connector and my sql api of python:
#pip install pymysql
#pip install pymysql mysql-connector-python

import mysql.connector
from mysql.connector import errorcode
from pymysql import MySQLError
from View.objectsPrograms import Answer ,Question
class sql_server:
    def __init__(self ,database , password_sql , user_sql):
        try:
            self.cnx = mysql.connector.connect( user = user_sql,
                                            password = password_sql,
                                            database=database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        self.database_name = database
        self.cursor = self.database.cursor()
        self.cursor.execute(f'USE {database};')


    def add_answers(self, answers):
        add_answer = '''INSTERT INTO answers_tbl (answer_text ,creadedBy ,question_id) VALUES (%s, %s, %s)'''
        for answer in answers:
            data_answer = (answer.answer_text , answer.creadedBy , answer.id_question)
            try:
                self.cursor.execute(add_answer,data_answer)
            except MySQLError as e:
                print(f"Error: {e}")
            print("insert in the sql database:")
            answer.show()
        

    def add_questions(self,questions , test_id):
        add_question = '''INSTERT INTO questions_tbl (questions_id ,questions_text ,points ,test_id ) VALUES (%s, %s, %s,%s)'''
        for qu in questions:
            data_question = (qu.id , qu.text , qu.points,test_id )
            try:
                self.cursor.execute(add_question,data_question)
            except MySQLError as e:
                print(f"Error: {e}")
            print("insert in the sql database:")
            qu.show()
        print(f"insert questions in the sql database: {questions}")

    def add_test(self,test_name):
        self.cursor.execute(sql = f"INSERT INTO test (test_name) VALUES ({test_name})")       