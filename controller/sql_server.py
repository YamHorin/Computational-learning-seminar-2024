#before use this file need install connector and my sql api of python:
#pip install pymysql
#pip install pymysql mysql-connector-python

import mysql.connector
from mysql.connector import errorcode
from pymysql import MySQLError
class sql_server:
    def __init__(self ,user_sql, password_sql ,database):
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
        print("connection with the my sql database has been complete\n\n")
        self.cnx.database = database
        self.database_name = database
        self.cursor = self.cnx.cursor()
        self.cursor.execute(f'USE {database};')


    def add_answers(self, answers):
        add_answer = '''INSERT INTO answers_tbl (answer_text, createdBy, question_id) VALUES (%s, %s, %s)'''

        for answer in answers:
            data_answer = (answer.text, answer.createdBy, answer.questionId)
            print(add_answer, data_answer)  # Print for debugging (optional)

            try:
                self.cursor.execute(add_answer, data_answer)
            except MySQLError as e:
                print(f"Error: {e}")

            print("Inserted answer:")  # Print message after successful insert
            answer.show()  # Call the show method to display the answer details
        self.cnx.commit()

        

    def add_questions(self,questions):
        add_question = '''INSERT INTO questions_tbl (questions_id, questions_text, points) VALUES (%s, %s, %s)'''
        for qu in questions:
            data_question = (qu.id , qu.text , qu.points )
            print (data_question)
            try:
                self.cursor.execute(add_question,data_question)
            except MySQLError as e:
                print(f"Error: {e}")
            print("insert in the sql database:")
            qu.show()
        print(f"insert questions in the sql database: {questions}")
        self.cnx.commit()

    def last_number_objects(self):
        self.cursor.execute(f'USE {self.database};')
        num_qu  =self.cursor.execute('''
        SELECT COUNT(*)
        FROM questions_tbl 
        ''')
        num_ans  =self.cursor.execute('''
        SELECT COUNT(*)
        FROM answers_tbl 
        ''')
        self.cnx.commit()
        return num_ans , num_qu
    def close_connection(self):
        self.cursor.close()
        self.cnx.close()        