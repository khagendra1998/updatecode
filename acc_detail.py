import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *


class Account_Detail(tk.Frame):
    def __init__(self, master):
        super(Account_Detail,self).__init__()

        self.account_detail_frame_icon = tk.Frame(self,bg='#cc0001')
        self.icon_account_detail = set_icon_size(100,100,'di.png')
        self.account_detail_icon = tk.Button(self.account_detail_frame_icon,
                                            image=self.icon_account_detail).grid(row=0)
        self.label_2 = tk.Label(self.account_detail_frame_icon,text='Account Detail',
                                font=("Arial","12","bold"),bg='#cc0001')
        self.label_2.grid(row=1,columnspan=2)
        self.account_detail_frame_icon.grid()