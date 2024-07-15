import tkinter as tk
import customtkinter as ctk
import cx_Oracle

class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Checkly Login")
        self.geometry("500x300")

        # Password label and entry
        self.password_label = ctk.CTkLabel(self, text="Please log in with MySql password:", font=ctk.CTkFont(size=18))
        self.password_label.pack(pady=(40, 5))
        self.password_entry = ctk.CTkEntry(self, width=300, show='*')
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

        try:
            # Connect to Oracle database
            dsn = cx_Oracle.makedsn('your_host', 'your_port', service_name='your_service_name')
            connection = cx_Oracle.connect('your_username', password, dsn)
            connection.close()
            
            # If connection is successful, display a success message
            tk.messagebox.showinfo("Login Successful", f"Logged in as {role}")
        except cx_Oracle.DatabaseError as e:
            tk.messagebox.showerror("Login Failed", "Invalid credentials or unable to connect to the database.")
            print(f"Database error occurred: {e}")

# Create and run the login screen
login_app = LoginScreen()
login_app.mainloop()