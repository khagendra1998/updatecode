import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
import pickle
from tkinter import messagebox
from set_image_size import *
from after_login import After


class User_Log(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.username = tk.Label(self, text='USERNAME', bg='orange', font=('Times New Roman', 15, 'bold'))
        self.password = tk.Label(self, text='PASSWORD', bg='orange', font=('Times New Roman', 15, 'bold'))
        self.username.grid(row=0)
        self.password.grid(row=1)
        self.user = tk.StringVar()
        self.Pass = tk.StringVar()
        self.username_entry = tk.Entry(self, font=('arial', 15, 'bold'), textvariable=self.user)
        self.password_entry = tk.Entry(self, font=('arial', 15, 'bold'), show='*', textvariable=self.Pass)
        self.username_entry.grid(row=0, column=1, pady=10)
        self.password_entry.grid(row=1, column=1, pady=10)
        self.eye=set_icon_size(20,20,'eye_icon.png')
        self.view_password=tk.Button(self,image=self.eye,bg='green')
        self.view_password.grid(row=1,column=3)

        self.login_button = tk.Button(self, text='Login', font=('arial', 15, 'bold'), 
                                    width=10,command=self.check_id_password)
        self.login_button.grid(row=2, column=1)
        
        self.Exit_button = tk.Button(self, text='Exit', font=('arial', 15, 'bold'), 
                                    width=10,command=self.Exit_Called)
        self.Exit_button.grid(row=2, column=2,)

    def check_id_password(self):
        with open( os.getcwd()+"/"+"bin"+"/"+"credential.pkl",'rb') as ReadFile: #opening file as pickle from the bin directory
            dictionary_user_password=pickle.load(ReadFile)  #retriving the file
        self.user_name = dictionary_user_password['username']  #retrving the user name from the file
        self.password  = dictionary_user_password['password']   #retriving the pasword belongs to the username
        if not self.user.get or not self.Pass.get():              #if one of the values are null
            tk.messagebox.showerror(title='Error Login',message='Null Value Field Error!')     #message to show error
        elif self.user.get() == self.user_name and self.Pass.get() == self.password:
            User_Log.destroy(self)

            self.ne = After(self)
            self.ne.grid()


        else:
            tk.messagebox.showerror(title='Error Login',message='Wrong Credentials(ID/Password) !')

            self.username_entry.delete(0,END)
            self.password_entry.delete(0,END)
        # logged_in()
    def Exit_Called(self):
        self.var=tk.messagebox.askokcancel(title='Confirm Your Exit',message="Do You Really Want To Exit ?")
        if self.var:
            quit()
        else:
            return True
