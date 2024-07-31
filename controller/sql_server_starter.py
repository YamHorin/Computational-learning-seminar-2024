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
    database = 'ai_answers'
    try:
        # Connect to MySQL server without specifying a database
        cnx = mysql.connector.connect(user='root', password=pwd)
        cursor = cnx.cursor()
        
        # Create the database if it does not exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        cnx.database = database
        
        # Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions_tbl (
            questions_id INT PRIMARY KEY,
            questions_text VARCHAR(2000) NOT NULL,
            points INT,
            key_words VARCHAR(2000) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    
        );
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS answers_tbl (
            answer_id INT AUTO_INCREMENT PRIMARY KEY,
            answer_text VARCHAR(2000) NOT NULL,
            createdBy VARCHAR(2000),
            question_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')
        # Call the function to create student_answers table
        create_student_answers_table(pwd)
        
        cnx.commit()
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist and could not be created")
        else:
            print(f"Database initialization error: {err}")
    finally:
        # Ensure resources are closed
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()   

def create_student_answers_table(pwd):
    try:
        cnx = mysql.connector.connect(user='root', password=pwd, database='ai_answers')
        cursor = cnx.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_answers (
            answer_id INT AUTO_INCREMENT PRIMARY KEY,
            answer_text VARCHAR(2000) NOT NULL,
            createdBy VARCHAR(2000),
            question_id INT NOT NULL,
            grade FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')
        
        cnx.commit()
        print("student_answers table created successfully")
    
    except mysql.connector.Error as err:
        print(f"Error creating student_answers table: {err}")
    finally:
        if cursor:
            cursor.close()
        if cnx:
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

def clean_data_sql (pwd):
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
  mycursor.execute('''
  delete
  FROM questions_tbl 
  ''')
  mycursor.execute('''
  delete
  FROM answers_tbl
  ''')
  cnx.commit()
  mycursor.close()
  cnx.close()      


####################################################################
#This version check if the DB exists, if not -> create it then continue
####################################################################
# import mysql.connector
# from mysql.connector import errorcode
# import maskpass

# def create_database(pwd):
#     try:
#         cnx = mysql.connector.connect(user='root', password=pwd)
#         mycursor = cnx.cursor()

#         # Check if the database exists
#         mycursor.execute("SHOW DATABASES")
#         databases = [database[0] for database in mycursor]

#         if 'ai_answers' not in databases:
#             # Create the database if it doesn't exist
#             mycursor.execute("CREATE DATABASE ai_answers")

#         mycursor.close()
#         cnx.close()

#     except mysql.connector.Error as err:
#         print(f"Error creating database: {err}")
#         raise

# def database_initialization(pwd):
#     try:
#         # Create the database if it doesn't exist
#         create_database(pwd)

#         # Now connect to the database
#         cnx = mysql.connector.connect(user='root', password=pwd, database='ai_answers')
#         mycursor = cnx.cursor()

#         # Create tables if they don't exist
#         mycursor.execute('''
#             CREATE TABLE IF NOT EXISTS test (
#                 test_id INT AUTO_INCREMENT PRIMARY KEY,
#                 test_name VARCHAR(255) NOT NULL
#             );
#         ''')

#         mycursor.execute('''
#             CREATE TABLE IF NOT EXISTS questions_tbl (
#                 questions_id INT PRIMARY KEY,
#                 questions_text VARCHAR(1000) NOT NULL,
#                 points INT,
#                 test_id  INT,
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#                 FOREIGN KEY (test_id) REFERENCES test(test_id)
#             );
#         ''')

#         mycursor.execute('''
#             CREATE TABLE IF NOT EXISTS answers_tbl (
#                 answer_id INT AUTO_INCREMENT PRIMARY KEY,
#                 answer_text VARCHAR(1000) NOT NULL,
#                 creadedBy VARCHAR(1000),
#                 question_id INT NOT NULL,
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             );
#         ''')

#         cnx.commit()
#         mycursor.close()
#         cnx.close()

#     except mysql.connector.Error as err:
#         print(f"Error initializing database: {err}")
#         raise

# def get_last_number_question_and_answer(pwd):
#     try:
#         # Create the database if it doesn't exist
#         create_database(pwd)

#         # Connect to the database
#         cnx = mysql.connector.connect(user='root', password=pwd, database='ai_answers')
#         mycursor = cnx.cursor(buffered=True)

#         database = 'ai_answers'
#         mycursor.execute(f'USE {database};')

#         mycursor.execute('SELECT COUNT(*) FROM questions_tbl')
#         num_qu = mycursor.fetchone()[0]  # Get the count result

#         mycursor.execute('SELECT COUNT(*) FROM answers_tbl')
#         num_ans = mycursor.fetchone()[0]  # Get the count result

#         cnx.commit()
#         mycursor.close()
#         cnx.close()

#         return num_qu, num_ans

#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("\n\nSomething is wrong with your user name or password\n\n")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("\n\nDatabase does not exist\n\n")
#         else:
#             print(err)
#         return None, None