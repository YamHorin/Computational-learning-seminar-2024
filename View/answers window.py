import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog, messagebox

# Define larger font sizes
LARGE_FONT = ("Arial", 16)
LARGER_FONT = ("Arial", 18)

class EditDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, initial_value=""):
        self.initial_value = initial_value
        super().__init__(parent, title=title)

    def body(self, master):
        self.geometry("600x300")  # Set the size of the edit dialog
        tk.Label(master, text="Edit the answer:", font=LARGER_FONT).pack(pady=10)
        self.entry = tk.Entry(master, font=LARGE_FONT, width=50)
        self.entry.pack(padx=20, pady=10)
        self.entry.insert(0, self.initial_value)
        return self.entry

    def apply(self):
        self.result = self.entry.get()

class TestAnswersWindow(ctk.CTk):
    def __init__(self, answers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answers = answers
        
        self.title("Test Answers")
        self.geometry("600x500")
        
        self.answer_widgets = []
        self.create_widgets()
        
    def create_widgets(self):
        for i, answer in enumerate(self.answers):
            frame = ctk.CTkFrame(self)
            frame.pack(pady=10, padx=10, fill="x")

            # Calculate the required width for the answer label
            width = max(20, len(answer) // 2)  # Adjust as needed
            
            answer_label = ctk.CTkLabel(frame, text=answer, font=LARGE_FONT, width=width)
            answer_label.pack(side="left", padx=10)
            
            edit_button = ctk.CTkButton(frame, text="Edit", font=LARGE_FONT, command=lambda i=i: self.edit_answer(i))
            edit_button.pack(side="right", padx=10)
            
            self.answer_widgets.append((answer_label, edit_button))
        
        # Add the Done button at the bottom
        done_button = ctk.CTkButton(self, text="Done", font=LARGE_FONT, command=self.done)
        done_button.pack(pady=20)
    
    def edit_answer(self, index):
        current_answer = self.answers[index]
        edit_dialog = EditDialog(self, "Edit Answer", initial_value=current_answer)
        
        if edit_dialog.result:
            self.answers[index] = edit_dialog.result
            # Update the answer label text and adjust the width dynamically
            width = max(20, len(edit_dialog.result) // 2)  # Adjust as needed
            self.answer_widgets[index][0].configure(text=edit_dialog.result, width=width)
            messagebox.showinfo("Success", f"Answer {index + 1} updated.")

    def done(self):
        #self.cleanup()
        self.destroy()
        #messagebox.showinfo("Done", "All answers are updated and saved!")

    def cleanup(self):
        # Perform any additional cleanup here if needed
        # Example: Ensure all widgets are properly handled
        print("Performing cleanup...")

if __name__ == "__main__":
    answers = ["Answer 1", "A very very very very long answer that needs more space", "Answer 3", "Another long answer to test the width adjustment"]
    app = TestAnswersWindow(answers)
    app.mainloop()
