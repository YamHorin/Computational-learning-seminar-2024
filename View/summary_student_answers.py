import customtkinter as ctk
import controller.sql_server

# Initialize the customtkinter window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Define the root window before using it
root = ctk.CTk()
root.title("Test Answers Review")
root.geometry("600x600")

# Create a scrollable frame inside the root window
scrollable_frame = ctk.CTkScrollableFrame(root, width=550, height=550)
scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)


# Sample data for questions, answers, reviews, and points
''' Connect to DB '''
questions = [
    "What is the impact of price on demand?",
    "How does income affect demand?",
    "What is the role of substitute goods in demand?",
    "How do substitute prices influence demand?",
    "What factors can transform demand?",
    "How do future price expectations affect demand?"
]

answers = [
    "Determinant of demand, as even minute changes in price can have a profound impact...",
    "Increase in income often leading to a substantial upward shift in the demand curve...",
    "Changes in substitute prices can either stimulate or reduce demand for a product...",
    "Changes in substitute prices can either stimulate or reduce demand for a product...",
    "Exert a transformative influence on demand, leading to significant shifts...",
    "Anticipated future price movements, which can either stimulate or dampen demand..."
]

reviews = [
    "This answer covers the essential points but could use more detail.",
    "This answer needs more detail in discussing the impact on demand.",
    "Good analysis, but lacks depth in explaining substitute goods.",
    "Well written but missed a key point about price elasticity.",
    "Excellent! Covered all the necessary points with great clarity.",
    "Lacks clarity, but the overall idea is correct."
]

points = [
    "Points: 5/10",
    "Points: 7/10",
    "Points: 6/10",
    "Points: 8/10",
    "Points: 10/10",
    "Points: 4/10"
]

# Loop to create the question, answer, review, and points display
for i in range(len(questions)):
    # Display the question number
    question_label = ctk.CTkLabel(scrollable_frame, text=f"Question {i+1}", font=("Arial", 16, "bold"))
    question_label.grid(row=i*5, column=0, padx=10, pady=(10, 0), sticky="w")

    # Display the question text
    question_text_label = ctk.CTkLabel(scrollable_frame, text=questions[i], font=("Arial", 14), wraplength=500)
    question_text_label.grid(row=i*5+1, column=0, padx=10, pady=(0, 5), sticky="w")

    # Display the answer with the label "Answer:"
    answer_label = ctk.CTkLabel(scrollable_frame, text=f"Answer: {answers[i]}", font=("Arial", 14), wraplength=500)
    answer_label.grid(row=i*5+2, column=0, padx=10, pady=(0, 5), sticky="w")

    # Display the review
    review_label = ctk.CTkLabel(scrollable_frame, text=f"Feedback: {reviews[i]}", font=("Arial", 12), wraplength=500)
    review_label.grid(row=i*5+3, column=0, padx=10, pady=(0, 5), sticky="w")

    # Display the points
    points_label = ctk.CTkLabel(scrollable_frame, text=points[i], font=("Arial", 12))
    points_label.grid(row=i*5+4, column=0, padx=10, pady=(0, 10), sticky="w")

# Done button
done_button = ctk.CTkButton(root, text="Done", font=("Arial", 14), command=root.destroy)
done_button.pack(pady=10)

# Run the application
root.mainloop()