import tkinter as tk
import customtkinter as ctk
from datetime import datetime, timedelta
from tkinter import simpledialog, messagebox

class StudentGUI(ctk.CTk):
    def __init__(self, questions, model, on_done_callback, correct_answers, points):
        super().__init__()
        self.questions = []
        for q in questions:
            self.questions.append(q.text)
        self.model = model
        self.student_answers = []
        self.current_question_index = 0
        self.on_done_callback = on_done_callback
        self.correct_answers = correct_answers
        self.points = points
        
        self.title("Student Test Interface")
        self.geometry("800x600")
        
        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Student Interface:", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
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

        # Create the question display label with points
        self.question_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=20, weight="bold"), wraplength=800)
        self.question_label.grid(row=0, column=1, columnspan=2, padx=10, pady=(10, 5), sticky="w")

        # Create answer entry
        self.answer_label = ctk.CTkLabel(self, text="Answer:", font=ctk.CTkFont(size=20, weight="bold"))
        self.answer_label.grid(row=1, column=1, padx=10, pady=(5, 2), sticky="w")
        self.answer_entry = ctk.CTkTextbox(self, width=300, height=150)
        self.answer_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=(2, 5))

        # Create buttons for navigation
        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_previous_question)
        self.back_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        self.continue_button = ctk.CTkButton(self, text="Continue", command=self.show_next_question)
        self.continue_button.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        
        self.done_button = ctk.CTkButton(self.sidebar_frame, text="DONE", command=self.done_button)
        self.done_button.grid(row=9, column=0, padx=20, pady=(10, 20), sticky="ew")

        # Create timer label
        self.timer_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=18))
        self.timer_label.grid(row=3, column=1, columnspan=2, padx=10, pady=(5, 10))
        
        self.hello_button = ctk.CTkButton(self.sidebar_frame, text="Say Hello", command=self.say_hello)
        self.hello_button.grid(row=4, column=0, padx=20, pady=(10, 20), sticky="ew")

        # Initialize timer
        self.start_time = datetime.now()
        self.update_timer()

        self.update_question_display()

    def say_hello(self):
        self.answer_entry.insert('1.0' , '''
The primary factors that influence the demand for a good or service in a competitive market are:

Price of the Good or Service: Generally, as the price of a good or service decreases, the quantity demanded increases, and vice versa (law of demand).

Income of Consumers: As consumers' income increases, they are typically able to purchase more goods and services, shifting the demand curve to the right. Conversely, a decrease in income will usually decrease demand.

Prices of Related Goods:
    Substitutes: If the price of a substitute good rises, the demand for the good in question may increase.
    Complements: If the price of a complementary good rises, the demand for the good in question may decrease.

Consumer Preferences: Changes in tastes and preferences can increase or decrease demand. For example, if a good becomes fashionable, demand for it will increase.

Expectations of Future Prices: If consumers expect prices to rise in the future, they may increase their current demand. Conversely, if they expect prices to fall, they might reduce current demand.

Number of Buyers: An increase in the number of consumers can increase demand, while a decrease in the number of consumers can reduce demand.

Seasonal Changes: Certain goods and services experience changes in demand due to seasonal factors.

Advertising and Publicity: Effective advertising can increase demand by making more consumers aware of the good or service.

''')
        print ("done")
    def update_question_display(self):
        question = self.questions[self.current_question_index]
        points = self.model.points[self.current_question_index]
        display_text = f"Question: {question}({points} points)"
        self.question_label.configure(text=display_text)
    
    def show_next_question(self):
        self.save_answer()
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.update_question_display()
            self.answer_entry.delete("1.0", tk.END)  # Clear previous answer
        else:
            self.pop_window_all_done()

    def pop_window_all_done(self):
        all_done_window = ctk.CTkToplevel(self)
        all_done_window.title("All Done")
        all_done_window.geometry("400x200")
        
        # Create and configure the label
        done_label = ctk.CTkLabel(all_done_window, text="All done!", font=ctk.CTkFont(size=40, weight="bold"))
        done_label.pack(expand=True, pady=20)


    def show_previous_question(self):
        self.save_answer()
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.update_question_display()
            self.answer_entry.delete("1.0", tk.END)  # Clear previous answer

    def save_answer(self):
        answer = self.answer_entry.get("1.0", tk.END).strip()
        if len(self.student_answers) <= self.current_question_index:
            self.student_answers.append(answer)
        else:
            self.student_answers[self.current_question_index] = answer

    def done_button(self):
        self.save_answer()
        self.grades = self.model.grade_answers(self.student_answers)
        # self.model.save_grades(self.grades)
        self.final_grade = self.model.final_grade(self.grades)
        # Call the callback function to start the autogen agent
        #self.on_done_callback(grades, self.correct_answers, self.points, self.student_answers, final_grade)
        self.destroy()

    def update_timer(self):
        # Calculate remaining time
        current_time = datetime.now()
        elapsed_time = current_time - self.start_time
        remaining_time = timedelta(hours=1) - elapsed_time

        # Format remaining time as hours, minutes, and seconds
        hours = remaining_time.seconds // 3600
        minutes = (remaining_time.seconds // 60) % 60
        seconds = remaining_time.seconds % 60
        timer_str = f"Time remaining: {hours:02}:{minutes:02}:{seconds:02}"
        self.timer_label.configure(text=timer_str)

        # Schedule next update after 1 second
        self.after(1000, self.update_timer)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)




# class StudentGUI(ctk.CTk):
#     def __init__(self, questions):
#         super().__init__()
#         self.questions = questions
#         self.current_question_index = 0
        
#         self.title("Student Test Interface")
#         self.geometry("1100x1100")
        
#         # Configure grid layout (4x4)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure((2, 3), weight=0)
#         self.grid_rowconfigure((0, 1, 2), weight=1)

#         # Create sidebar frame with widgets
#         self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
#         self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
#         self.sidebar_frame.grid_rowconfigure(4, weight=1)
#         self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Student Interface:", font=ctk.CTkFont(size=20, weight="bold"))
#         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
#         self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
#         self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
#         self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
#                                                              command=self.change_appearance_mode_event)
#         self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
#         self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
#         self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
#         self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%", "130%", "140%", "150%"],
#                                                      command=self.change_scaling_event)
#         self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

#         # Create the question display label
#         self.question_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=20, weight="bold"), wraplength=800)
#         self.question_label.grid(row=0, column=1, columnspan=2, padx=10, pady=(20, 5), sticky="w")

#         # Create answer entry
#         self.answer_label = ctk.CTkLabel(self, text="Answer:", font=ctk.CTkFont(size=20, weight="bold"))
#         self.answer_label.grid(row=1, column=1, padx=10, pady=(10, 5), sticky="w")
#         self.answer_entry = ctk.CTkTextbox(self, width=400, height=200)
#         self.answer_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=(5, 10))

#         # Create buttons for navigation
#         self.back_button = ctk.CTkButton(self, text="Back", command=self.show_previous_question)
#         self.back_button.grid(row=2, column=1, padx=20, pady=10, sticky="e")

#         self.continue_button = ctk.CTkButton(self, text="Continue", command=self.show_next_question)
#         self.continue_button.grid(row=2, column=2, padx=20, pady=10, sticky="w")
        
#         self.done_button = ctk.CTkButton(self.sidebar_frame, text="DONE", command=self.done_button)
#         self.done_button.grid(row=9, column=0, padx=20, pady=(10, 20), sticky="ew")

#         # Create timer label
#         self.timer_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=18))
#         self.timer_label.grid(row=3, column=1, columnspan=2, padx=10, pady=(10, 20))

#         # Initialize timer
#         self.start_time = datetime.now()
#         self.update_timer()

#         self.update_question_display()

#     def update_question_display(self):
#         current_question = self.questions[self.current_question_index]
#         self.question_label.configure(text=current_question)

#     def show_next_question(self):
#         if self.current_question_index < len(self.questions) - 1:
#             self.current_question_index += 1
#             self.update_question_display()

#     def show_previous_question(self):
#         if self.current_question_index > 0:
#             self.current_question_index -= 1
#             self.update_question_display()

#     def done_button(self):
#         print("STUDENT DONE")
#         self.destroy()
        

#     def update_timer(self):
#         # Calculate remaining time
#         current_time = datetime.now()
#         elapsed_time = current_time - self.start_time
#         remaining_time = timedelta(hours=1) - elapsed_time

#         # Format remaining time as hours, minutes, and seconds
#         hours = remaining_time.seconds // 3600
#         minutes = (remaining_time.seconds // 60) % 60
#         seconds = remaining_time.seconds % 60
#         timer_str = f"Time remaining: {hours:02}:{minutes:02}:{seconds:02}"
#         self.timer_label.configure(text=timer_str)

#         # Schedule next update after 1 second
#         self.after(1000, self.update_timer)

#     def change_appearance_mode_event(self, new_appearance_mode: str):
#         ctk.set_appearance_mode(new_appearance_mode)

#     def change_scaling_event(self, new_scaling: str):
#         new_scaling_float = int(new_scaling.replace("%", "")) / 100
#         ctk.set_widget_scaling(new_scaling_float)

# # Example usage:
# questions = [
#     "What color is the sky?",
#     "What is the capital of France?",
#     "Who wrote 'Romeo and Juliet'?"
# ]

# app = StudentGUI()
# app.mainloop()
