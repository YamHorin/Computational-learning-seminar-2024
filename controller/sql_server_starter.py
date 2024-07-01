#Installation
# pip install maskpass
# pip install mysql-connector-python
#  in mysql workbanch:
# show  databases;
# create database ai_answers;

import mysql.connector
from mysql.connector import errorcode
import maskpass
def database_initialization(pwd):

  
  try:
    cnx = mysql.connector.connect( user = 'root',
                                  password = pwd,
                                  database='ai_answers')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  
  
  database = 'ai_answers'
  
  mycursor  = cnx.cursor()
  mycursor.execute(f'USE {database};')
  mycursor.execute('''
  CREATE TABLE IF NOT EXISTS test (
      test_id INT AUTO_INCREMENT PRIMARY KEY,
      test_name VARCHAR(255) NOT NULL
      
  );
                   
  ''')                 
                   
  mycursor.execute('''
  CREATE TABLE IF NOT EXISTS questions_tbl (
      questions_id INT PRIMARY KEY,
      questions_text VARCHAR(1000) NOT NULL,
      points INT,
      test_id  INT,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
      FOREIGN KEY (test_id) REFERENCES test(test_id)
  );
                   
  ''')
                   
                   
  mycursor.execute('''
  CREATE TABLE IF NOT EXISTS answers_tbl (
      answer_id INT AUTO_INCREMENT PRIMARY KEY,
      answer_text VARCHAR(1000) NOT NULL,
      creadedBy VARCHAR(1000),
      question_id INT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
                   
  ''')
                   
  cnx.commit()
  mycursor.close()
  cnx.close()             
                 
def get_last_number_question_and_answer(pwd):
  
  try:
    cnx = mysql.connector.connect( user = 'root',
                                  password = pwd,
                                  database='ai_answers')
    mycursor  = cnx.cursor(buffered=True)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("\n\nSomething is wrong with your user name or password\n\n")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("\n\nDatabase does not exist\n\n")
    else:
      print(err)
  
  
  database = 'ai_answers'
  

  mycursor.execute(f'USE {database};')
  num_qu  =mycursor.execute('''
  SELECT COUNT(*)
  FROM questions_tbl
  ''')
  num_ans  =mycursor.execute('''
  SELECT COUNT(*)
  FROM answers_tbl
  ''')
  cnx.commit()
  mycursor.close()
  cnx.close()      

  return num_qu,num_ans
