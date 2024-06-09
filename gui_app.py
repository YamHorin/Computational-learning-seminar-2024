import customtkinter as ctk
from agent_logic import initialize_agents

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autogen Agent Interaction")
        self.questions = ""

        self.setup_gui()

    def setup_gui(self):
        ctk.CTkLabel(self.root, text="Enter your questions:").pack(pady=10)
        
        self.question_entry = ctk.CTkTextbox(self.root, width=400, height=200)
        self.question_entry.pack(pady=10)
        
        self.submit_button = ctk.CTkButton(self.root, text="Submit Question", command=self.submit_question)
        self.submit_button.pack(pady=10)
        
        self.done_button = ctk.CTkButton(self.root, text="Done", command=self.done_input)
        self.done_button.pack(pady=10)

    def submit_question(self):
        question_text = self.question_entry.get("1.0", "end-1c")
        self.questions += question_text + "\n"
        self.question_entry.delete("1.0", "end")

    def done_input(self):
        # Initialize agents and run the group chat
        self.initialize_agents()
        
        initializer.initiate_chat(manager, message=self.questions)
        
        # Create a new window to display the answers
        answers_window = ctk.CTkToplevel(self.root)
        answers_window.title("Agent Answers")
        
        answers_text = ctk.CTkTextbox(answers_window, width=600, height=400)
        answers_text.pack(pady=10)
        
        answers = ""
        for message in groupchat.messages:
            answers += message["content"] + "\n"
        
        answers_text.insert("1.0", answers)

    def initialize_agents(self):
        global initializer, manager, groupchat
        initializer, manager, groupchat = initialize_agents()

if __name__ == "__main__":
    root = ctk.CTk()
    app = GUIApp(root)
    root.mainloop()
