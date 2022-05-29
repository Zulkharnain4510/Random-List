# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random 
#Generate 5 random numbers between 10 and 30 
randomlist = random.sample(range(10, 30), 5) 
print(randomlist)
from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("500x500")

random_number_list = Label(root)
random_number_sorted_list = Label(root)

def randomlist():
    randomlist = random.sample(range(10,30),5)
    random_number_list["text"] = "random list : " + str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"] = "sorted random numbers : " + str(randomlist)

btn=Button(root,text="generate random list ",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()

