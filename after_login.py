import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *
from menu_bar import *
from logout import Out
from create_acc import Create
from acc_detail import Account_Detail
from acc_balance import Account_Balance
from loan import Loan
from report import Report
from service import Service
from withdrawal import Withdrawal
from calculator import Calculator

class After(tk.Frame):
    def __init__(self,master):
        super(After,self).__init__()
        self.logout()
        self.create_acc()
        self.acc_detail()
        self.acc_balance()
        self.loan()
        self.report()
        self.service()
        self.withdraw()
        self.calculator()

    def logout(self):
        self.log = Out(self)
        self.log.place(x=1000,y=100)

    def create_acc(self):
        self.create = Create(self)
        self.create.place(x=400,y=200)
    
    def acc_detail(self):
        self.detail = Account_Detail(self)
        self.detail.place(x=600,y=200)

    def acc_balance(self):
        self.balance = Account_Balance(self)
        self.balance.place(x=800,y=200)

    def loan(self):
        self.info_loan = Loan(self)
        self.info_loan.place(x=1000,y=200)

    def report(self):
        self.rep = Report(self)
        self.rep.place(x=400,y=400)

    def service(self):
        self.serv = Service(self)
        self.serv.place(x=600,y=400)

    def withdraw(self):
        self.withd = Withdrawal(self)
        self.withd.place(x=800,y=400)

    def calculator(self):
        self.cal = Calculator(self)
        self.cal.place(x=1000,y=400)