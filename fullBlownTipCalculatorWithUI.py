"""
Python script adds UI to original tip calculator I created
"""
#gets all the dependencies to run python script
from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk


#creates main window, while also creating the size of it and the name of it
root = Tk()
root.geometry('500x650')
root.title("Tip Calculator")
#root.config(background="white")

#exit screen
def exitt():
    exit()

#grabs any image from its file explorer address and sets the variable to grabbing it

#HAVE TO CHANGE PATH OF WHERE IMAGE IS
imge=Image.open(r"C:\Users\jereb\Downloads\download.jpg")
photo=ImageTk.PhotoImage(imge)


#puts photo into window
lab=Label(image=photo)
lab.pack()

bill=DoubleVar()
tip_percent=DoubleVar()

def abt():
    tkinter.messagebox.showinfo("Welcome","This my first python project. It is just a simple tip calculator.")

def ext_1():
    exit()



    

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=ext_1)

subm2 = Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=abt)


    
def tip_calculation_win():
    window = Tk()
    window.title("welcome to tip calculation window")
    window.geometry('250x100')
    flat_tip = str(round(tip_percent.get() / 100 * bill.get(), 2))
    label_02 = Label(window, text = 'your tip is this number:' + str(flat_tip), relief = "solid", font = ('arial', 12, 'bold')).place(x = 30, y = 70)
    
#Actual buttons
label_0 = Label(root, text="Tip Calculator",relief="solid",width=20,font=("arial", 19,"bold"))
label_0.place(x=90,y=150)

#parameters for the calculation
label_1 = Label(root, text="Total Bill :",width=20,font=("bold", 10))
label_1.place(x=80,y=240)

entry_1 = Entry(root,textvar=bill)
entry_1.place(x=240,y=242)

label_2 = Label(root, text="Tip Percentage :",width=20,font=("bold", 10))
label_2.place(x=80,y=280)

entry_2 = Entry(root,textvar=tip_percent)
entry_2.place(x=240,y=282)


#def tip_calculation(bill, tip_percentage):
    #flat_tip = str(round(tip_percentage / 100 * bill, 2))
    


var=StringVar()






but_calculation=Button(root,text="Calculate Tip",width=12,bg='brown',fg='white',command=tip_calculation_win).place(x=208,y=560)

root.mainloop()
