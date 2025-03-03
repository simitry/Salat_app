import customtkinter
import Class.ButtonFrame as bf
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Salat App")
        self.geometry("500x500")
        self.maxsize(width=500, height =500)
        self.minsize(width = 500, height = 500)
        
        
        self.checkbox_var = customtkinter.BooleanVar()
        self.button_frame=bf.MyButtonFrame(self,"My Buttons").grid(row=0, column=0, padx=0, pady=(0,10), sticky="ne")
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text= "Fajr",variable = self.checkbox_var,command=self.on_checkbox).grid(row=0, column=1, padx=10, pady=(0,10), sticky="w")
        
    def on_checkbox(self):
        if self.checkbox_var.get():
            print("gyat")
        
