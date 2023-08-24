from tkinter import * 

root = Tk()
root.title("Calculator")
frame = Entry(root, width=35, borderwidth=5)
frame.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def clickButton(number):
    curr = frame.get()
    frame.delete(0,END)

    frame.insert(0,str(curr)+ str(number))

def button_clear():
    frame.delete(0,END)

def add_Button():
    first= frame.get()
    global f
    global math
    math = 'addition'
    f = int(first)
    frame.delete(0,END)

def equal_Button():
    second = frame.get()
    frame.delete(0,END)
    if math == 'addition':
        frame.insert(0,f+ int(second))
    if math == 'subtract':
        frame.insert(0,f- int(second))
    if math == 'multiply':
        frame.insert(0,f* int(second))
    if math == 'divide':
        frame.insert(0,f/ int(second))

def subtract_Button():
    first= frame.get()
    global f
    global math
    math = 'subtract'
    f = int(first)
    frame.delete(0,END)

def multiply_Button():
    first= frame.get()
    global f
    global math
    math = 'multiply'
    f = int(first)
    frame.delete(0,END)

def divide_Button():
    first= frame.get()
    global f
    global math
    math = 'divide'
    f = int(first)
    frame.delete(0,END)


button1=  Button(root,text='1',padx=40,pady=20,command=lambda: clickButton(1))
button2=  Button(root,text='2',padx=40,pady=20,command=lambda: clickButton(2))
button3=  Button(root,text='3',padx=40,pady=20,command=lambda: clickButton(3))
button4=  Button(root,text='4',padx=40,pady=20,command=lambda: clickButton(4))
button5=  Button(root,text='5',padx=40,pady=20,command=lambda: clickButton(5))
button6=  Button(root,text='6',padx=40,pady=20,command=lambda: clickButton(6))
button7=  Button(root,text='7',padx=40,pady=20,command=lambda: clickButton(7))
button8=  Button(root,text='8',padx=40,pady=20,command=lambda: clickButton(8))
button9=  Button(root,text='9',padx=40,pady=20,command=lambda: clickButton(9))
button0=  Button(root,text='0',padx=40,pady=20,command=lambda: clickButton(0))
AddButton = Button(root,text='+',padx=39,pady=20,command=lambda: add_Button())
EqualButton = Button(root,text='=',padx=91,pady=20,command=lambda: equal_Button())
ClearButton = Button(root,text='Clear',padx=79,pady=20,command=lambda: button_clear())

SubtractButton = Button(root,text='-',padx=41,pady=20,command=lambda: subtract_Button())
DivideButton = Button(root,text='/',padx=41 ,pady=20,command=lambda: divide_Button())
MultiplyButton = Button(root,text='x',padx=40,pady=20,command=lambda: multiply_Button())



button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
AddButton.grid(row=5,column=0)
ClearButton.grid(row=4,column=1,columnspan=2)
EqualButton.grid(row=5,column=1,columnspan=2)

SubtractButton.grid(row=6,column=0)
MultiplyButton.grid(row=6,column=1)
DivideButton.grid(row=6,column=2)

root.mainloop()

