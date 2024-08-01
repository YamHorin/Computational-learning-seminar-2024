import tkinter as tk
import customtkinter as ctk
import cx_Oracle
import mysql.connector
from mysql.connector import errorcode
class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Checkly Login")
        self.geometry("500x300")
        
        # Password label and entry
        self.password_label = ctk.CTkLabel(self, text="Please log in with MySql password:", font=ctk.CTkFont(size=18))
        self.password_label.pack(pady=(40, 5))
        self.password_entry = ctk.CTkEntry(self, width=300, show='*' , state="normal")
        self.password_entry.pack(pady=5)

        # Radio buttons for user role
        self.role_var = tk.StringVar(value="Student")
        self.teacher_radio = ctk.CTkRadioButton(self, text="Teacher", variable=self.role_var, value="Teacher")
        self.teacher_radio.pack(pady=5)
        self.student_radio = ctk.CTkRadioButton(self, text="Student", variable=self.role_var, value="Student")
        self.student_radio.pack(pady=5)

        # Login button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=(20, 10))

    def login(self):
        password = self.password_entry.get()
        role = self.role_var.get()
        print (role)
        self.password_value = password
        self.role_value = role
        try:
            # Connect to Oracle database
            # dsn = cx_Oracle.makedsn('your_host', 'your_port', service_name='your_service_name')
            # connection = cx_Oracle.connect('your_username', password, dsn)
            # connection.close()
            #connect to mysql database
            cnx = mysql.connector.connect(user='root', password=password)
            cursor = cnx.cursor()
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()  
            # If connection is successful, display a success message
            tk.messagebox.showinfo("Login Successful", f"Logged in as {role}")
            self.destroy()
        # except cx_Oracle.DatabaseError as e:
        except mysql.connector.Error as err:
            tk.messagebox.showerror("Login Failed", "Invalid credentials or unable to connect to the database.")
            print(f"Database error occurred: {err}")
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist and could not be created")

# Create and run the login screen
# login_app = LoginScreen()
# login_app.mainloop()