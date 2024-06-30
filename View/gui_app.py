#to started pip install customtkinter
#this is the main files when the program will start 

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import tkinter
import tkinter.messagebox
import customtkinter as ctk
from controller.sql_server_starter import database_initialization

class GUIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Autogen Agent Interaction")
        self.geometry(f"{1100}x{580}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.questions = ""    
       
        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Teacher submit:", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create the rest of the widgets using grid
        
        self.question_entry = ctk.CTkTextbox(self, width=400, height=200)
        self.question_entry.grid(row=0, column=1, columnspan=2, padx=20, pady=(20, 10))
        
        self.submit_button = ctk.CTkButton(self, text="Submit Question", command=self.submit_question)
        self.submit_button.grid(row=1, column=1, padx=20, pady=10)
        
        self.done_button = ctk.CTkButton(self, text="Done", command=self.done_input)
        self.done_button.grid(row=2, column=1, padx=20, pady=10)
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)    
    def sidebar_button_event(self):
        print("buttom activated")
    
    def submit_question(self):
        pass
        # question_text = self.question_entry.get("1.0", "end-1c")
        # self.questions += question_text + "\n"
        # self.question_entry.delete("1.0", "end")

    def done_input(self):
        pass
        # Initialize agents and run the group chat
        #get question , answers , keys

        # self.initialize_agents()
        
        # initializer.initiate_chat(manager, message=self.questions)
        
        # # Create a new window to display the answers
        # answers_window = ctk.CTkToplevel(self.root)
        # answers_window.title("Agent Answers")
        
        # answers_text = ctk.CTkTextbox(answers_window, width=600, height=400)
        # answers_text.pack(pady=10)
        
        # answers = ""
        # for message in groupchat.messages:
        #     answers += message["content"] + "\n"
        
        # answers_text.insert("1.0", answers)


if __name__ == "__main__":
    #database_initialization()
    app = GUIApp()
    app.mainloop()
