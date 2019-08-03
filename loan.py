import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *

class Loan(tk.Frame):
    def __init__(self,master):
        super(Loan,self).__init__()

        self.loan_frame_icon = tk.Frame(self,bg='#CC0001')
        self.icon_loan = set_icon_size(100,100,'loan.png')
        self.loan_icon = tk.Button(self.loan_frame_icon,image=self.icon_loan).grid(row=0)
        self.label_4 = Label(self.loan_frame_icon,text='Loan ',
                            font=('Arial','12','bold'),bg="#CC0001")
        self.label_4.grid(row=1,columnspan=2)
        self.loan_frame_icon.grid()