import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *
#from login import User_Log


class Out(tk.Frame):
    def __init__(self,master):
        super(Out,self).__init__()
        self.logout_frame_icon = tk.Frame(self,bg='#cc0001')
        self.icon_logout = set_icon_size(50,50,'logout.png')
        self.logout_icon = tk.Button(self.logout_frame_icon,image=self.icon_logout,
                                    command=self.Exit_Called).grid(row=0)

        self.label_6      = tk.Label(self.logout_frame_icon,text='logout',
                                     font=("Arial","12","bold"),bg="#cc0001")
        self.label_6.grid(row=1,columnspan=2)
        
        self.logout_frame_icon.grid()

    def Exit_Called(self):
        self.var=tk.messagebox.askokcancel(title='Confirm Your Exit',message="Do You Really Want To Exit ?")
        if self.var:
            quit()
            
        else:
            return True
