import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *
from login import User_Log 



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("COMMON BANKING")
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.configure(background='#CC0001')
        
        #self.load_photo = set_icon_size(1300,720,'indiapost.png')
        #self.label = tk.Label(self,image=self.load_photo)
        #self.label.pack()

        self.L = tk.Label(self, text='Head Post Office Staff Savings & Co-operative Society Ltd. Alwar ',
              font=('Times new Roman', 30, 'bold'), bg='#CC0001', fg='yellow',justify="right")
        self.L.place(x=180,y=20)

        

        self.main()
        
    def main(self): 
        self.nn = User_Log(self)
        self.nn.configure(background="orange")
        self.nn.place(x=500,y=250)
        

        
if __name__ == '__main__':
    app = App()
    app.mainloop()