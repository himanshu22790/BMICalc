from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import numpy as np

window = Tk()
window.title("Himanshu's Calculator")
window.geometry("400x400")
tabC = ttk.Notebook(window)
tab1 = ttk.Frame(tabC)
tab2 = ttk.Frame(tabC)

tabC.add(tab1, text='Calculator')
tabC.add(tab2, text='BMI')
tabC.pack(expand=1, fill="both")


def press(num):
    global expression
    expression = expression+str(num)
    text.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        text.set(total)
        expression = ''
    except:
        text.set('Error')
        expression = ''


def clear():
    global expression
    expression = ''
    text.set('')

def clearbox(self):
    word_text.delete(0,END)
    return
def clearbox2(self):
    weight.delete(0,END)
    return
def clearbox3(self):
    height.delete(0,END)
    return

def convert_w():
    global a1,a
    a = weight.get()
    print(a1)

    if a1 == 'Kilograms':
        return a
    elif a1 == 'Pounds':
        a = float(a)/2.20462
        return a
    elif a1 == 'Ounces':
        a = float(a)/35.274
        return a
    elif a1 == 'Stones':
        a = float(a)/0.157473
        return a
    
def convert_h():
    global b,b1
    b= height.get()
    print(b1)
    if b1 == 'Meters':
        return b
    elif b1 == 'cm':
        b = float(b)/100
        return b
    elif b1 == 'inches':
        b = float(b)/39.3701
        return b

def calculate():
    global bmi
    convert_w()
    convert_h()
    bmi = float(a)/float(b)**2
    result = round(bmi,2)
    if bmi <= 18.5:
        messagebox.showinfo("Result", "Your Body Mass Index is: " + str(result) + "\n You're underweight")
    elif bmi > 18.5 and bmi < 24.9:
        messagebox.showinfo("Result", "Your Body Mass Index is: " + str(result) + "\n You're good!!")
    elif bmi >= 25 and bmi < 29.9:
        messagebox.showinfo("Result", "Your Body Mass Index is: " + str(result) + "\n You're overweight")
    else:
        messagebox.showinfo("Result", "Your Body Mass Index is: " + str(result) + "\n You're Obese, eat less!") 

text = StringVar()
word_text = Entry(tab1, textvariable=text, fg='grey')
word_text.grid(row=4,columnspan=4, ipadx=70)
text.set("Enter Your Expression: ")
word_text.bind("<Button-1>", clearbox)

expression = ''
bmi=''

button1 = Button(tab1, text='7', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(7), height=1, width=6)
button1.grid(row=5, column=0)
button2 = Button(tab1, text='8', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(8), height=1, width=6)
button2.grid(row=5, column=1)
button3 = Button(tab1, text='9', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(9), height=1, width=6)
button3.grid(row=5, column=2)
button4 = Button(tab1, text='4', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(4), height=1, width=6)
button4.grid(row=6, column=0)
button5 = Button(tab1, text='5', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(5), height=1, width=6)
button5.grid(row=6, column=1)
button6 = Button(tab1, text='6', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(6), height=1, width=6)
button6.grid(row=6, column=2)
button7 = Button(tab1, text='1', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(1), height=1, width=6)
button7.grid(row=7, column=0)
button8 = Button(tab1, text='2', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(2), height=1, width=6)
button8.grid(row=7, column=1)
button9 = Button(tab1, text='3', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(3), height=1, width=6)
button9.grid(row=7, column=2)
button0 = Button(tab1, text='0', font='Times', bg='blue', fg='yellow',
                 command=lambda: press(0), height=1, width=6)
button0.grid(row=8, column=1)
plus = Button(tab1, text='+', font='Times', bg='blue', fg='yellow',
              command=lambda: press('+'), height=1, width=6)
plus.grid(row=5, column=3)
minus = Button(tab1, text='-', font='Times', bg='blue', fg='yellow',
               command=lambda: press('-'), height=1, width=6)
minus.grid(row=6, column=3)
mult = Button(tab1, text='*', font='Times', bg='blue', fg='yellow',
              command=lambda: press('*'), height=1, width=6)
mult.grid(row=7, column=3)
divide = Button(tab1, text='/', font='Times', bg='blue', fg='yellow',
                command=lambda: press('/'), height=1, width=6)
divide.grid(row=8, column=3)
decimal = Button(tab1, text='.', font='Times', bg='blue', fg='yellow',
                 command=lambda: press('.'), height=1, width=6)
decimal.grid(row=8, column=0)
equal = Button(tab1, text='=', font='Times', bg='blue', fg='yellow',
               command=equalpress, height=1, width=6)
equal.grid(row=8, column=2)
clear = Button(tab1, text='CE', font='Times', bg='blue', fg='yellow',
               command=clear, height=1, width=6)
clear.grid(row=4, column=3)

label2 = Label(tab2, text='Calculate Body Mass Index')
label2.grid(row=0, column = 0)

WeightList = ["Kilograms", "Pounds", "Ounces","Stone"]
HeightList = ["Meters","cm","inches"]

ddw = StringVar()
ddw.set(WeightList[0]) #default
wts = OptionMenu(tab2, ddw, *WeightList)
wts.grid(row=1,column=4)

ddh = StringVar()
ddh.set(HeightList[0]) #default
wts = OptionMenu(tab2, ddh, *HeightList)
wts.grid(row=3,column=4)
a1=ddw.get()
b1=ddh.get()

weighttext = StringVar()
weight = Entry(tab2, textvariable=weighttext, fg='grey')
weighttext.set("Enter Weight")
weight.bind("<Button-1>", clearbox2)
weight.grid(row=1, column=0, columnspan=2, ipadx=40)


def ddw_change(*args):
    global a1
    a1=ddw.get()
    return a1


ddw.trace('w', ddw_change)



heighttext = StringVar()
height = Entry(tab2, textvariable=heighttext, fg='grey')
heighttext.set("Enter Height: ")
height.bind("<Button-1>", clearbox3)
height.grid(row=3, column=0, columnspan=2, ipadx=40)



def ddh_change(*args):
    global b1
    b1 = ddh.get()
    return b1
ddh.trace('w', ddh_change)

calc = Button(tab2,text="Calculate", font='Times', bg = 'black', fg='white',command=calculate)
calc.grid(row=4,column=0)




window.mainloop()
