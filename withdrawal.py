import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *

class Withdrawal(tk.Frame):
    def __init__(self,master):
        super(Withdrawal,self).__init__()
        self.withd_frame_icon = tk.Frame(self,bg='#cc0001')
        self.icon_withd = set_icon_size(100,100,'withdrawal.png')
        self.withd_icon = tk.Button(self.withd_frame_icon,image=self.icon_withd).grid(row=0)
        self.label_7     = tk.Label(self.withd_frame_icon,text='Withdrawal',
                                  font=("Arial","12","bold"),bg="#cc0001")
        self.label_7.grid(row=1,columnspan=2)
        self.withd_frame_icon.grid()