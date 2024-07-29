import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog, messagebox

# Define larger font sizes
LARGE_FONT = ("Arial", 24)
LARGER_FONT = ("Arial", 28)

class EditDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, initial_value=""):
        self.initial_value = initial_value
        super().__init__(parent, title=title)

    def body(self, master):
        self.geometry("600x300")  # Set the size of the edit dialog
        tk.Label(master, text="Edit the answer:", font=LARGER_FONT).pack(pady=10)
        
        self.text = tk.Text(master, font=LARGE_FONT, width=50, height=10, wrap=tk.WORD)
        self.text.pack(padx=20, pady=10)
        self.text.insert(tk.END, self.initial_value)

        # Add a scrollbar to the text widget
        scrollbar = tk.Scrollbar(master, command=self.text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scrollbar.set)

        return self.text

    def apply(self):
        self.result = self.text.get("1.0", tk.END).strip()

class AnswerWindow(ctk.CTkToplevel):
    def __init__(self, parent, index, answer):
        super().__init__(parent)
        self.parent = parent
        self.index = index
        self.answer = answer
        self.title("Answer Window")
        self.geometry("800x800")  # Set a larger size for the answer window

        text_frame = ctk.CTkFrame(self)
        text_frame.pack(expand=True, fill='both', padx=20, pady=20)

        self.text_widget = tk.Text(text_frame, font=LARGER_FONT, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both', side=tk.LEFT)
        self.text_widget.insert(tk.END, answer)
        self.text_widget.config(state=tk.DISABLED)  # Make the text read-only

        scrollbar = tk.Scrollbar(text_frame, command=self.text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        edit_button = ctk.CTkButton(self, text="Edit", command=self.edit_answer)
        edit_button.pack(pady=20)

    def edit_answer(self):
        edit_dialog = EditDialog(self, "Edit Answer", initial_value=self.answer)

        if edit_dialog.result:
            self.answer = edit_dialog.result
            self.parent.answers[self.index] = edit_dialog.result
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, edit_dialog.result)
            self.text_widget.config(state=tk.DISABLED)
            messagebox.showinfo("Success", f"Answer {self.index + 1} updated.")
            self.parent.update_answer_label(self.index, edit_dialog.result)

class TestAnswersWindow(ctk.CTk):
    def __init__(self, answers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answers = answers
        self.title("Test Answers")
        self.geometry('800x800')

        self.answer_widgets = []
        self.create_widgets()

    def create_widgets(self):
        for i, answer in enumerate(self.answers):
            frame = ctk.CTkFrame(self)
            frame.pack(pady=10, padx=10, fill="x")

            answer_button = ctk.CTkButton(frame, text=f"Answer {i + 1}", font=LARGE_FONT, command=lambda i=i, a=answer: self.show_answer(i, a))
            answer_button.pack(pady=10, padx=10)

            answer_label = ctk.CTkLabel(frame, text=answer, font=LARGE_FONT)
            answer_label.pack(pady=10, padx=10)

            self.answer_widgets.append((answer_label, answer_button))

        # Add the Done button at the bottom
        done_button = ctk.CTkButton(self, text="Done", font=LARGE_FONT, command=self.done)
        done_button.pack(pady=20)

    def show_answer(self, index, answer):
        answer_window = AnswerWindow(self, index, answer)
        answer_window.grab_set()

    def update_answer_label(self, index, new_text):
        self.answer_widgets[index][0].configure(text=new_text)

    def done(self):
        self.destroy()
        # Optional: Show a message box when done
        # messagebox.showinfo("Done", "All answers are updated and saved!")

if __name__ == "__main__":
    answers = [
        "In a highly competitive environment, the Price of the Good or Service is the most significant determinant of demand, as even minute changes in price can have a profound impact on quantity demanded and ultimately affect a firm's revenue and profitability.",
        "Consumer Income is another crucial factor influencing demand, with an increase in income often leading to a substantial upward shift in the demand curve and driving increased consumption and sales for a good or service.",
        "The Prices of Related Goods, including both substitutes and complements, play a vital role in shaping demand, as changes in substitute prices can either stimulate or reduce demand for a product, while complement price changes can significantly enhance or diminish its value proposition to consumers.",
        "The Prices of Related Goods, including both substitutes and complements, play a vital role in shaping demand, as changes in substitute prices can either stimulate or reduce demand for a product, while complement price changes can significantly enhance or diminish its value proposition to consumers.",
        "Consumer Preferences, encompassing profound shifts in tastes, preferences, and values, can exert a transformative influence on demand, leading to significant shifts in the demand curve and potentially even altering consumer behavior and purchasing patterns.",
        "Expectations of Future Prices are another critical consideration, as consumers adjust their current consumption patterns based on anticipated future price movements, which can either stimulate or dampen demand for a good or service, ultimately influencing a firm's competitive advantage and ability to attract and retain customers."
    ]

    app = TestAnswersWindow(answers)
    app.mainloop()
