#pip install customtkinter
import customtkinter as ctk

# Function to handle the button click event
def get_input():
    user_input = entry.get()
    print(f'User input: {user_input}')
    # You can use the input further as needed

# Create the main application window
app = ctk.CTk()

# Set the title of the window
app.title("CustomTkinter Input Example")

# Set the size of the window
app.geometry("300x200")

# Create an entry widget for text input
entry = ctk.CTkEntry(master=app, width=200)
entry.pack(pady=20)

# Create a button that will call the get_input function when clicked
button = ctk.CTkButton(master=app, text="Submit", command=get_input)
button.pack(pady=10)

# Start the main event loop
app.mainloop()