import tkinter as tk
from datetime import datetime , timedelta
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chekly Student Dash")
        self.geometry("1000x700")

        # Create sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        # Add sidebar buttons
        self.home_button = ctk.CTkButton(self.sidebar, text="Home")
        self.home_button.pack(pady=10)

        self.tests_button = ctk.CTkButton(self.sidebar, text="Tests")
        self.tests_button.pack(pady=10) 

        self.profile_button = ctk.CTkButton(self.sidebar, text="Profile")
        self.profile_button.pack(pady=10) 

        # Create main content are
        self.main_content = ctk.CTkFrame(self)
        self.main_content.pack(side="right", fill="both", expand=True)

        # Add widgets to main content
        self.add_clock_widget()
        self.add_upcoming_test_widget()
        self.add_graph_widget()
        # Add more widgets as needed

    def add_clock_widget(self):
        clock_frame = ctk.CTkFrame(self.main_content)
        clock_frame.grid(row=0, column=0, padx=10, pady=10)
        
        ctk.CTkLabel(clock_frame, text="11:00").pack()

    def add_upcoming_test_widget(self):
        test_frame = ctk.CTkFrame(self.main_content)
        test_frame.grid(row=0, column=1, padx=10, pady=10)
        
        ctk.CTkLabel(test_frame, text="Upcoming Test").pack()
        ctk.CTkButton(test_frame, text="Set reminder").pack()

    def add_graph_widget(self):
        graph_frame = ctk.CTkFrame(self.main_content)
        graph_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4, 5], [2, 4, 3, 5, 3])
        
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()