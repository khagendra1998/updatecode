import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *

class Report(tk.Frame):
    def __init__(self,master):
        super(Report,self).__init__()

        self.report_frame_icon = tk.Frame(self,bg='#cc0001')
        self.icon_report       = set_icon_size(100,100,'ri.png')
        self.report_icon       = tk.Button(self.report_frame_icon,
                                            image=self.icon_report).grid(row=0)
        self.label_5           = tk.Label(self.report_frame_icon,text='Report',
                                          font=("Arial","12","bold"),bg='#cc0001')
        self.label_5.grid(row=1,columnspan=2)
        self.report_frame_icon.grid()