import mysql.connector
from mysql.connector import errorcode


class sql_server:
    def __init__(self ,database , password_sql , user_sql):
        try:
            self.database = mysql.connector.connect( user = user_sql,
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
        self.connector = self.database.cursor()
        self.database.cursor().execute(f'USE {database};')
    def add_answers(answers):
        pass
    def add_questions(questions):
        pass
    def add_test(test_name):
        pass        