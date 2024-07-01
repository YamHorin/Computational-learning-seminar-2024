import customtkinter
import tkinter as tk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Making the window
        self.title("Loading")
        self.geometry(f"{500}x{580}")
        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.label = customtkinter.CTkLabel(self, text="Loading, please wait...", font=customtkinter.CTkFont(size=20))
        self.label.grid(row=0, column=1, pady=(20, 0))

        self.loading_canvas = tk.Canvas(self, width=90, height=90, bg="white", highlightthickness=0)
        self.loading_canvas.grid(row=1, column=1, pady=(20, 0))
        self.arc = self.loading_canvas.create_arc(10, 10, 90, 90, start=0, extent=150, fill="blue")
        
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)


        self.angle = 0
        self.animate_loading_circle()

    def animate_loading_circle(self):
        self.loading_canvas.itemconfig(self.arc, start=self.angle)
        self.angle = (self.angle + 30) % 360
        self.after(50, self.animate_loading_circle)  # Adjust the delay as needed

app = App()
app.mainloop()
