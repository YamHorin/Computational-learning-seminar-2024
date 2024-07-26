# Installation
# pip install maskpass
# pip install mysql-connector-python
# in mysql workbanch:
# show  databases;
# create database ai_answers;

import mysql.connector
from mysql.connector import errorcode


def get_connection(pwd):
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password=pwd,
        port=3306,
        database='ai_question'
    )


def database_initialization(pwd):
    # try:
    #   cnx = mysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     password=pwd,
    #     port='3306',
    #     database='ai_question')
    #
    # except mysql.connector.Error as err:
    #   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #     print("Something is wrong with your user name or password")
    #   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #     print("Database does not exist")
    #   else:
    #     print(err)

    try:
        cnx = get_connection(pwd)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    database = 'ai_question'
    mycursor = cnx.cursor()
    mycursor.execute(f'USE {database};')
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS test_tbl(
        test_id INT AUTO_INCREMENT PRIMARY KEY,
        test_name VARCHAR(255) NOT NULL,
        test_grade INT)''')

    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS questions_tbl (
        questions_id INT PRIMARY KEY,
        questions_text VARCHAR(1000) NOT NULL,
        points INT,
        test_id  INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
        FOREIGN KEY (test_id) REFERENCES test_tbl(test_id)
    )
                   
    ''')

    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS answers_t (
        answer_id INT AUTO_INCREMENT PRIMARY KEY,
        answer_text VARCHAR(1000) NOT NULL,
        question_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (question_id) REFERENCES questions_tbl(questions_id)
    )
                   
    ''')

    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS answers_s (
            answer_id INT AUTO_INCREMENT PRIMARY KEY,
            answer_text VARCHAR(1000) NOT NULL,
            question_id INT NOT NULL,
            ans_points INT,
            answer_review VARCHAR(1000),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_id) REFERENCES questions_tbl(questions_id)
        )

        ''')

    cnx.commit()
    mycursor.close()
    cnx.close()


def get_last_number_question_and_answer(pwd):

    cnx = None

    try:
        cnx = get_connection(pwd)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    database = 'ai_question'
    mycursor = cnx.cursor()
    mycursor.execute(f'USE {database};')
    num_qu = mycursor.execute('''
    SELECT COUNT(*)
    FROM questions_tbl
    ''')
    # Ensure all results are read
    while mycursor.nextset():
        pass

    num_ans = mycursor.execute('''
    SELECT COUNT(*)
    FROM answers_s
    ''')
    # Ensure all results are read
    while mycursor.nextset():
        pass

    cnx.commit()
    mycursor.close()
    cnx.close()

    return num_qu, num_ans

####################################################################
# This version check if the DB exists, if not -> create it then continue
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
#             print("\n\nSomething is wrong with your username or password\n\n")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("\n\nDatabase does not exist\n\n")
#         else:
#             print(err)
#         return None, None
