#to started pip install customtkinter
#this is the main files when the program will start 

import customtkinter as ctk
import View.objectsPrograms as obj
##import objectsPrograms as obj
#from View import objectsPrograms as obj
from model.agentLogixMake_AI_Answers import initialize_agents


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
    
    
    def submit_question(self):
        # question_text = self.question_entry.get("1.0", "end-1c")
        # self.question_entry.delete("1.0", "end")

        #TODO make a point submit text or a scaling option emenu
        #pass        
        # self.questions.append(self.factory_questions.createQuestion(self.question_entry.get("1.0", "end-1c")
        #                                                        ,10,
        #                                                        self.keywords_entry.get("1.0", "end-1c")
        #                                                        ,))

         # Retrieve input values
        question_text = self.question_entry.get("1.0", "end-1c")
        keywords = self.keywords_entry.get("1.0", "end-1c")
        points = self.points_optionemenu.get("1.0", "end-1c")
        answers_text = self.answer_entry.get("1.0", "end-1c")

        # Create a question object using the factory
        question = self.factory_questions.createQuestion(
            question_text=question_text,
            points=points,
            keyWords=keywords,
            id_answer_teacher=None,
            answerFromTeacher=answers_text,
            test_id=1  # Example test_id, this should be dynamically set.
        )

        # Create an answer object using the factory
        answer = self.factory_answer_teacher.createAnswer(
            answers_text=answers_text,
            answer_points=points,
            id_question=question.id
        )

        # Append the created objects to the lists
        self.questions.append(question)
        self.answers.append(answer)

        # Display the created question and answer (example: printing for now)
        print("Question:", question_text)
        print("Answer:", answers_text)
        print("Keywords:", keywords)
        print("Points:", points)

        # Clear the input fields after submission
        self.question_entry.delete("1.0", "end")
        self.answer_entry.delete("1.0", "end")
        self.keywords_entry.delete("1.0", "end")

    def done_input(self):
        #pass
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
        # Assuming `answers_teacher` is accessible or passed to this method
        initializer, manager, groupchat = initialize_agents(answers_teacher=self.answers)

        # Initialize agents and run the group chat
        initializer.initiate_chat(manager, message=self.questions)

        # Debugging: Log the contents of `self.questions` to ensure they are correct
        print("Sending questions to agents:")
        for question in self.questions:
            print(f"Question: {question.question_text}")
            print(f"Answers: {question.answers_text}")
            print(f"Keywords: {question.keywords}")
            print(f"Points: {question.points}")

        # Clearing questions and answers lists after chat
        self.questions.clear()
        self.answers.clear()

        # Create a new window to display the answers (example: printing for now)
        print("Initializing agents and starting group chat...")
        self.destroy()

app = GUIApp(0,0)
app.mainloop()



###############################################
#TRY OTHER IMPLEMENTATION
# to start pip install customtkinter
# this is the main files when the program will start 

# import customtkinter as ctk
# from View import objectsPrograms as obj
# from model import agentLogixMake_AI_Answers

# class GUIApp(ctk.CTk):
#     def __init__(self, last_num_question, last_num_answer):
#         super().__init__()
#         # Initial values for logic
#         self.last_num_question = last_num_question
#         self.last_num_answer = last_num_answer
#         self.questions = []
#         self.answers = []
#         # Factories for creating questions and answers
#         self.factory_questions = obj.QuestionFactory(last_num_question)
#         self.factory_answer_teacher = obj.AnswerFactory_teacher()

#         # Setting up the main window
#         self.title("Autogen Agent Interaction")
#         self.geometry(f"{1100}x{1100}")

#         # Configure grid layout (4x4)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure((2, 3), weight=0)
#         self.grid_rowconfigure((0, 1, 2), weight=1)

#         # Create sidebar frame with widgets
#         self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
#         self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
#         self.sidebar_frame.grid_rowconfigure(4, weight=1)

#         # Sidebar widgets
#         self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Teacher submit:", font=ctk.CTkFont(size=20, weight="bold"))
#         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
#         self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
#         self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
#         self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
#         self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
#         self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
#         self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
#         self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
#         self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
#         self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
#         self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
#         self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
#         self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
#         self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

#         # Create textbox to display agent answers
#         self.textbox = ctk.CTkTextbox(self, width=250)
#         self.textbox.grid(row=0, column=1, columnspan=2, rowspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.textbox.insert("0.0", "Agent answers will be shown here...\n\n")

#         # Entry fields for user input
#         self.main_entry = ctk.CTkEntry(self, placeholder_text="Add question")
#         self.main_entry.grid(row=4, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#         # create keyword entry
#         self.keyword_entry = ctk.CTkEntry(self, placeholder_text="Add keywords")
#         self.keyword_entry.grid(row=4, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#         # create answer entry
#         self.answer_entry = ctk.CTkEntry(self, placeholder_text="Add answers")
#         self.answer_entry.grid(row=5, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#         # create points entry
#         self.points_entry = ctk.CTkEntry(self, placeholder_text="Add points")
#         self.points_entry.grid(row=5, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#         # create submit button
#         self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_question)
#         self.submit_button.grid(row=6, column=0, columnspan=4, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
#         # create done button
#         self.done_button = ctk.CTkButton(self, text="Done", command=self.done_button_event)
#         self.done_button.grid(row=7, column=0, columnspan=4, padx=(20, 0), pady=(20, 20), sticky="nsew")

#     def sidebar_button_event(self):
#         print("Sidebar button clicked")

#     def change_appearance_mode_event(self, new_appearance_mode):
#         ctk.set_appearance_mode(new_appearance_mode)

#     def change_scaling_event(self, new_scaling):
#         ctk.set_widget_scaling(new_scaling)

#     def submit_question(self):
#         # Retrieve input values
#         question_text = self.main_entry.get()
#         keywords = self.keyword_entry.get()
#         points = self.points_entry.get()
#         answers_text = self.answer_entry.get()

#         # Create a question object using the factory
#         question = self.factory_questions.createQuestion(
#             question_text=question_text,
#             points=points,
#             keyWords=keywords,
#             id_answer_teacher=None,
#             answerFromTeacher=answers_text,
#             test_id=1  # Example test_id, this should be dynamically set.
#         )

#         # Create an answer object using the factory
#         answer = self.factory_answer_teacher.createAnswer(
#             answers_text=answers_text,
#             answer_points=points,
#             id_question=question.id
#         )

#         # Append the created objects to the lists
#         self.questions.append(question)
#         self.answers.append(answer)

#         # Display the created question and answer
#         question.show()
#         answer.show()

#         # Clear the input fields after submission
#         self.main_entry.delete(0, 'end')
#         self.keyword_entry.delete(0, 'end')
#         self.answer_entry.delete(0, 'end')
#         self.points_entry.delete(0, 'end')

#     def done_button_event(self):
#         # Implement functionality to finalize changes or any desired action
#         print("Done button clicked")
#             # Initialize agents and start group chat
#         initializer, manager, groupchat = agentLogixMake_AI_Answers.initialize_agents(self.questions)

#         # Start the group chat
#     #    manager.start()

#     #    self.initialize_agents()
        
#         initializer.initiate_chat(manager, message=self.questions)
        
# if __name__ == "__main__":
#     app = GUIApp(last_num_question=0, last_num_answer=0)
#     app.mainloop()


