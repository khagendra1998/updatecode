import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *

class Calculator(tk.Frame):
    def __init__(self, master):
        super(Calculator,self).__init__()
        self.emi_frame_icon = tk.Frame(self,bg='#CC0001')
        self.icon_emi = set_icon_size(100,100,'emi.png')
        self.emi_icon = tk.Button(self.emi_frame_icon,image=self.icon_emi).grid(row=0)
        self.label_8 = tk.Label(self.emi_frame_icon,text='EMI Calculator',
                                font=("Arial",12,"bold"),bg='#CC0001')
        self.label_8.grid(row=1,columnspan=2)
        self.emi_frame_icon.grid()