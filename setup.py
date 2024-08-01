import os
import subprocess
import controller.sql_server_starter as sql
def install_dependencies():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    subprocess.check_call(["ollama", "pull", "llama3"])

def main():
    install_dependencies()
    pwd = input("password to mysql account:")
    sql.database_initialization(pwd)
    sql.create_student_answers_table(pwd)
    print("Setup complete!")

if __name__ == "__main__":
    main()