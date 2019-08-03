import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *
#from after_login import After

class Create(tk.Frame):
    def __init__(self,master):
        super(Create,self).__init__()
        self.create_account_frame_icon = tk.Frame(self,bg="#cc0001")
        self.icon_CA = set_icon_size(100,100,'cacc.png')
        self.create_account_icon = tk.Button(self.create_account_frame_icon,image=self.icon_CA).grid(row=0)
        self.label=tk.Label(self.create_account_frame_icon,text='Create Account',
                            font=("Arial","12","bold"),bg='#cc0001').grid(row=1,columnspan=2)
        self.create_account_frame_icon.grid()
    
    def entry_detail(self):
        self.labelfont = ('times', 20, 'bold') 
        Label(self, text='Loan Account Number    ',font=self.labelfont,bg='#CC0001').grid(row=0) 
        Label(self, text='Name of Employee       ',font=self.labelfont,bg='#CC0001').grid(row=1)
        Label(self, text='Account Office         ',font=self.labelfont,bg='#CC0001').grid(row=2)
        Label(self, text='Designation of Employee',font=self.labelfont,bg='#CC0001').grid(row=3)
        Label(self, text='Contact Number         ',font=self.labelfont,bg='#CC0001').grid(row=4)
        Label(self, text='Email ID               ',font=self.labelfont,bg='#CC0001').grid(row=5)
        Label(self, text='Address                ',font=self.labelfont,bg='#CC0001').grid(row=6)