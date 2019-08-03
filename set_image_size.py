from tkinter import *
import os
from PIL import ImageTk,Image
def set_icon_size(height,width,icon_name):
    temp_load=Image.open(os.getcwd()+'/'+'Load'+'/'+icon_name)
    temp_load=temp_load.resize((height,width),Image.ANTIALIAS)
    return ImageTk.PhotoImage(temp_load)
    