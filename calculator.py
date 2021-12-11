from tkinter import *
from tkinter import font
from tkinter.font import BOLD

root = Tk()
root.title('Calculator')
root.geometry("380x350")

# Text input area
e = Entry(root, width=35, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=70, ipady=5)
# e.place(x=1, y=10, height=40, width=300)

# Label(root, text="rcn4o").grid(row=1, column=2)

# function to get numbers


def number_input(num):
    if num == 'X':
        num = '*'
    exp = str(e.get())
    e.delete(0, END)
    e.insert(0, str(exp)+str(num))
    if (num == '*' or num == '/' or num == '+' or num == '-'):
        if (exp[len(exp)-1] == '*' or exp[len(exp)-1] == '/' or exp[len(exp)-1] == '+' or exp[len(exp)-1] == '-'):
            e.delete(0, END)
            e.insert(0, str(exp[:-1])+str(num))


def clear():
    e.delete(0, END)


def clearE():
    exp = str(e.get())
    e.delete(len(exp)-1, END)


def evaluate():
    exp = str(e.get())
    e.delete(0, END)
    e.insert(0, round(eval(exp), 5))


# Buttons 0-9, +, -, *, /, =, %, ., C, CE
# buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

btn7 = Button(root, text="7", padx=30, pady=10, font=BOLD,
              command=lambda: number_input(7)).grid(row=1, column=0)
btn8 = Button(root, text="8", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(8)).grid(row=1, column=1)
btn9 = Button(root, text="9", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(9)).grid(row=1, column=2)
btnMul = Button(root, text="x", padx=31, pady=10,  font=BOLD,
                command=lambda: number_input('X')).grid(row=1, column=3)

btn4 = Button(root, text="4", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(4)).grid(row=2, column=0)
btn5 = Button(root, text="5", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(5)).grid(row=2, column=1)
btn6 = Button(root, text="6", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(6)).grid(row=2, column=2)
btnDiv = Button(root, text="/", padx=32, pady=10,  font=BOLD,
                command=lambda: number_input('/')).grid(row=2, column=3)

btn1 = Button(root, text="1", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(1)).grid(row=3, column=0)
btn2 = Button(root, text="2", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(2)).grid(row=3, column=1)
btn3 = Button(root, text="3", padx=30, pady=10,  font=BOLD,
              command=lambda: number_input(3)).grid(row=3, column=2)
btnAdd = Button(root, text="+", padx=29, pady=10,  font=BOLD,
                command=lambda: number_input('+')).grid(row=3, column=3)

btn0 = Button(root, text="0", padx=78, pady=10,  font=BOLD,
              command=lambda: number_input(0)).grid(row=4, column=0, columnspan=2)
btnDot = Button(root, text=".", padx=33, pady=10,  font=BOLD,
                command=lambda: number_input('.')).grid(row=4, column=2)
btnSub = Button(root, text="-", padx=32, pady=10,  font=BOLD,
                command=lambda: number_input('-')).grid(row=4, column=3)

btnC = Button(root, text="C", padx=30, pady=10,  font=BOLD,
              command=clear).grid(row=5, column=0)
btnCE = Button(root, text="CE", padx=22, pady=10,
               font=BOLD, command=clearE).grid(row=5, column=1)
btnEqual = Button(root, text="=", padx=76, pady=10,  font=BOLD,
                  command=evaluate).grid(row=5, column=2, columnspan=2)


root.mainloop()
