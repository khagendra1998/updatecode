import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *

class Service(tk.Frame):
    def __init__(self, master):
        super(Service,self).__init__()
        self.sett_frame_icon = tk.Frame(self,bg='#cc0001')
        self.icon_sett = set_icon_size(100,100,'settings.png')
        self.sett_icon = tk.Button(self.sett_frame_icon,image=self.icon_sett).grid(row=0)
        self.label_6   = tk.Label(self.sett_frame_icon,text='Service',
                                  font=("Arial","12","bold"),bg="#cc0001")
        self.label_6.grid(row=1,columnspan=2)
        self.sett_frame_icon.grid()