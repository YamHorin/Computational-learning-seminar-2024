#before use this file need install connector and my sql api of python:
#pip install pymysql
#pip install pymysql mysql-connector-python

import mysql.connector
from View import objectsPrograms
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

            try:
                self.cursor.execute(add_answer, data_answer)
            except MySQLError as e:
                print(f"Error: {e}")

            print("**Inserted answer:")  # Print message after successful insert
            answer.show()
            print("\n\n")  # Call the show method to display the answer details
        self.cnx.commit()

        

    def add_questions(self,questions):
        add_question = '''INSERT INTO questions_tbl (questions_id, questions_text, points , key_words) VALUES (%s, %s, %s ,%s)'''
        for qu in questions:
            data_question = (qu.id , qu.text , qu.points ,qu.keyWords )
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
    
    def get_all_questions(self):
        self.cursor.execute("SELECT * FROM ai_answers.questions_tbl")
        questions = []
        list_of_list_of_key_words = []
        factory_questions = objectsPrograms.QuestionFactory(0)
        
        for row in self.cursor.fetchall():
            questions_id, questions_text, points, key_words, created_at = row
            question = factory_questions.createQuestionFromDB(questions_id, questions_text, points, key_words)
            questions.append(question)
            
            keyWords_list = [item.strip() for item in key_words.split(',')]
            list_of_list_of_key_words.append(keyWords_list)
            
           ### print(f"Question got from the DB: {questions_id}, {questions_text}, {points}, {key_words}, {created_at}")
        
        self.cnx.commit()
        return questions, list_of_list_of_key_words

    
    def get_all_answers(self):
        self.cursor.execute("SELECT * FROM ai_answers.answers_tbl")

        ANSWERs = []
        rows = self.cursor.fetchall()  # Fetch all rows from the executed query
        for row in rows:
            answer_id, answer_text, createdBy, question_id, created_at = row
            answer = objectsPrograms.Answer(answer_text, question_id, createdBy)
            ANSWERs.append(answer)
            ###print('Got answer from DB:')
           ### answer.show()

        return ANSWERs

    def add_student_answer(self, answer_text, student_id, question_id, grade):
        add_answer = '''INSERT INTO student_answers (answer_text, createdBy, question_id, grade) VALUES (%s, %s, %s, %s)'''
        grade = float(grade) if grade is not None else None
        data_answer = (answer_text, student_id, question_id, grade)

        try:
            self.cursor.execute(add_answer, data_answer)
            self.cnx.commit()
            print(f"Student answer for question {question_id} inserted successfully")
        except MySQLError as e:
            print(f"Error inserting student answer: {e}")
    def add_answers_students(self, list_data):
        add_answer_text = "INSERT INTO ai_answers.student_answers (answer_text, createdBy, question_id, grade, feedback) VALUES (%s, %s, %s, %s, %s)"
        for i, data in enumerate(list_data):
            answer_text = data[0]
            student_id = "student"
            question_id = i + 1
            grade = data[3]
            feedback = data[2]
            data_answer = (answer_text, student_id, question_id, grade, feedback)

            try:
                self.cursor.execute(add_answer_text, data_answer)
                self.cnx.commit()
                print(f"Student answer for data {data} inserted successfully")
            except MySQLError as e:
                print(f"Error inserting student answer: {e}")

    def close_connection(self):
        self.cursor.close() 
        self.cnx.close()        