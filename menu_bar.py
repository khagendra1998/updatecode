from tkinter import *

def nav_bar(self):
        menubar = Menu(self,bg='white')

        create_ac = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Create Account",menu=create_ac)

        account_detail = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Account Detail",menu=account_detail)

        account_balance = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Account Balance",menu=account_balance)

        loan = Menu(menubar,tearoff=0)
        loan.add_command(label="Loan Issue")
        loan.add_command(label="Loan Deposit")
        loan.add_command(label="Loan Extend")
        menubar.add_cascade(label="Loan",menu=loan)

        report = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Report", menu=report)

        service = Menu(menubar, tearoff=0)
        service.add_command(label="Deposit")
        service.add_command(label="Deposit Interest")
        service.add_command(label="Update User Profile")
        service.add_command(label="Account Summary")
        menubar.add_cascade(label="Service", menu=service)

        close_acc = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Close Account", menu=close_acc)

        calculator = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="EMI Calculator", menu=calculator)

        # display the menu
        self.config(menu=menubar)
