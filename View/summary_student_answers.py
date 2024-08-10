import customtkinter as ctk
import controller.sql_server


class SummeryStudentAnswers(ctk.CTk):
    def __init__(self, answers, questions, feedbacks, points, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.questions = questions
        self.answers = answers
        self.feedbacks = feedbacks
        self.points = points
        self.title("Student Answers")
        self.geometry('600x600')
        self.create_widgets()
    # # Initialize the customtkinter window
    # ctk.set_appearance_mode("dark")
    # ctk.set_default_color_theme("blue")

    # # Define the root window before using it
    # root = ctk.CTk()
    # root.title("Test Answers Review")
    # root.geometry("600x600")

    def create_widgets(self):
        # Create a scrollable frame inside the root window
        scrollable_frame = ctk.CTkScrollableFrame(self, width=550, height=550)
        scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)
        #scrollable_frame = ctk.CTkScrollableFrame(self, width=550, height=550)
        #scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

    # Loop to create the question, answer, review, and points display
        for i in range(len(self.questions)):
            # Display the question number
            question_label = ctk.CTkLabel(scrollable_frame, text=f"Question {i+1}", font=("Arial", 26, "bold"))
            question_label.grid(row=i*6, column=0, padx=10, pady=(10, 0), sticky="w")

            # Display the question text
            question_text_label = ctk.CTkLabel(scrollable_frame, text=self.questions[i].text, font=("Arial", 24), wraplength=500)
            question_text_label.grid(row=i*6+1, column=0, padx=10, pady=(0, 5), sticky="w")

            # Display the answer with the label "Answer:"
            answer_label = ctk.CTkLabel(scrollable_frame, text=f"Answer:", font=("Arial", 26,"bold"), wraplength=500)
            answer_label.grid(row=i*6+2, column=0, padx=10, pady=(10, 0), sticky="w")

            answer_text_label = ctk.CTkLabel(scrollable_frame, text=self.answers[i], font=("Arial", 24), wraplength=500)
            answer_text_label.grid(row=i*6+3, column=0, padx=10, pady=(0, 5), sticky="w")

            # Display the review
            review_label = ctk.CTkLabel(scrollable_frame, text=f"Feedback: {self.feedbacks[i]}", font=("Arial", 22), wraplength=500 , text_color='green')
            review_label.grid(row=i*6+4, column=0, padx=10, pady=(0, 5), sticky="w")

            # Display the points
            points_label = ctk.CTkLabel(scrollable_frame, text=f"grade : {self.points[i][0]}/{self.points[i][1]}", font=("Arial", 22) , text_color='blue')
            points_label.grid(row=i*6+5, column=0, padx=10, pady=(0, 10), sticky="w")

        # Done button
        done_button = ctk.CTkButton(self, text="Done", font=("Arial", 14), command=self.destroy)
        done_button.pack(pady=10)

    def done(self):
        self.destroy()

    # Run the application
    #self.mainloop()