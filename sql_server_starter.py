# Installation
#pip install mysql-connector-python
#in mysql:
# show  databases;
# create database ai_questions;

import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect( user = 'root',
                                password = 'deganit@0800abc',
                                database='ai_questions')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

database = 'ai_questions'

mycursor  = cnx.cursor()
mycursor.execute(f'USE {database};')
                 
mycursor.execute('''
CREATE TABLE questions_tbl (
    questions_id INT AUTO_INCREMENT PRIMARY KEY,
    questions_text VARCHAR(255) NOT NULL,
    test_id  INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
                 
''')
                 
                 
mycursor.execute('''
CREATE TABLE answers_tbl (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    answer_text VARCHAR(255) NOT NULL,
    
    
    test_id INT NOT NULL,
    question_id INT NOT NULL,
    date DATE NOT NULL
);
                 
''')
                 
                 
                 
                 
 
