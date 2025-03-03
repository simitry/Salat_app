import customtkinter as ctk

class MyButtonFrame(ctk.CTkFrame):
    def __init__(self, master,title):
        super().__init__(master)
        self.title = title
        
        self.title = ctk.CTkLabel(self, text = self.title, corner_radius=6,font=("Arial",13, "bold") ,text_color = "black").grid(row=0, column=0, padx=10, pady=(10, 10),sticky = "w")
        self.button_1 = ctk.CTkButton(self, text ="Create Table").grid(row=1, column=0, padx=10, pady=(0, 10), sticky="e")
        
        