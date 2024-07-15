#to started pip install customtkinter
#this is the main files when the program will start 

import customtkinter as ctk
#import View.objectsPrograms as obj
import objectsPrograms as obj

class GUIApp(ctk.CTk):
    def __init__(self , last_num_question , last_num_answer):
        super().__init__()
        #things for logic
        self.last_num_question = last_num_question
        self.last_num_answer = last_num_answer
        self.questions = []
        self.answers = []
        #factories
        self.factory_questions = obj.QuestionFactory( last_num_question)
        self.factory_answer_teacher = obj.AnswerFactory_teacher()
       

        #making the window
        self.title("Autogen Agent Interaction")
        self.geometry(f"{1100}x{1100}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

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
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%", "130%", "140%", "150%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create the rest of the widgets using grid
        self.question_label = ctk.CTkLabel(self, text="Question:", font=ctk.CTkFont(size=20, weight="bold"))
        self.question_label.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")
        self.question_entry = ctk.CTkTextbox(self, width=400, height=200)
        self.question_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=(5, 10))

        self.answer_label = ctk.CTkLabel(self, text="Answer:", font=ctk.CTkFont(size=20, weight="bold"))
        self.answer_label.grid(row=1, column=1, padx=10, pady=(10, 5), sticky="w")
        self.answer_entry = ctk.CTkTextbox(self, width=400, height=200)
        self.answer_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=(5, 10))

        self.keywords_label = ctk.CTkLabel(self, text="Keywords:", font=ctk.CTkFont(size=20, weight="bold"))
        self.keywords_label.grid(row=2, column=1, padx=10, pady=(10, 5), sticky="w")
        self.keywords_entry = ctk.CTkTextbox(self, width=400, height=100)
        self.keywords_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=(5, 10))

        self.points_label = ctk.CTkLabel(self, text="Points:", font=ctk.CTkFont(size=20, weight="bold"))
        self.points_label.grid(row=3, column=1, padx=10, pady=(10, 5), sticky="w")
        self.points_question = ctk.CTkTextbox(self, width=400, height=100)
        self.points_question.grid(row=3, column=1, columnspan=2,padx=10, pady=(5, 10))

        
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_question, width=200, height=50)
        self.submit_button.grid(row=4, column=2, padx=20, pady=10)

        self.done_button = ctk.CTkButton(self, text="Done", command=self.done_input, width=200, height=50)
        self.done_button.grid(row=4, column=3, padx=20, pady=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)    
    
    def sidebar_button_event(self):
        print("buttom activated")
    
    
    #TODO
    def submit_question(self):
        # question_text = self.question_entry.get("1.0", "end-1c")
        # self.question_entry.delete("1.0", "end")
         
        self.questions.append(self.factory_questions.createQuestion(self.question_entry.get("1.0", "end-1c")
                                                               ,self.points_question.get("1.0", "end-1c"),
                                                               self.keywords_entry.get("1.0", "end-1c")
                                                               ,))

    #TODO
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

app = GUIApp(0,0)
app.mainloop()

