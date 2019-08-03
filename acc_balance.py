import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *

class Account_Balance(tk.Frame):
    def __init__(self, master):
        super(Account_Balance,self).__init__()

        self.account_balance_frame_icon = tk.Frame(self,bg='#cc0001')
        self.icon_account_balance = set_icon_size(100,100,'balance_account.png')
        self.account_balance_icon = tk.Button(self.account_balance_frame_icon,
                                            image=self.icon_account_balance).grid(row=0)
        self.label_3 = Label(self.account_balance_frame_icon,text='Account Balance',
                            font=("Arial","12","bold"),bg='#cc0001')
        self.label_3.grid(row=1,columnspan=2)
        self.account_balance_frame_icon.grid()
