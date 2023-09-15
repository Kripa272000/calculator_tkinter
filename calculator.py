
from tkinter import *
root=Tk()
# root.geometry('400x400')
root.title("My window")

expression=""
def handleclick(button):
    global expression
    if len(expression)==0:
        if button.isdigit():
            if button!="0":
                expression=expression + button
                data.set(expression)
    else:
        expression=expression + button
        data.set(expression)

def handleEqual():
    global expression
    if expression[-1].isdigit():
        res=eval(expression)
        data.set(res)
        expression=""

def handleBackspace():
     global expression
     expression=expression[:-1]
     data.set(expression)
     print(expression)

data=StringVar()


input_box=Entry(root,font=28,textvariable=data)
input_box.grid(row=0,column=0,columnspan=4,pady=10)

b0=Button(root,text="0",font=24,padx=10,pady=10,command=lambda:handleclick("0"))
b0.grid(column=1,row=4,padx=10,pady=10)

b1=Button(root,text="1",font=24,padx=10,pady=10,command=lambda:handleclick("1"))
b1.grid(column=0,row=3,padx=10,pady=10)

b2=Button(root,text="2",font=24,padx=10,pady=10,command=lambda:handleclick("2"))
b2.grid(column=1,row=3,padx=10,pady=10)

b3=Button(root,text="3",font=24,padx=10,pady=10,command=lambda:handleclick("3"))
b3.grid(column=2,row=3,padx=10,pady=10)

b4=Button(root,text="4",font=24,padx=10,pady=10,command=lambda:handleclick("4"))
b4.grid(column=0,row=2,padx=10,pady=10)

b5=Button(root,text="5",font=24,padx=10,pady=10,command=lambda:handleclick("5"))
b5.grid(column=1,row=2,padx=10,pady=10)

b6=Button(root,text="6",font=24,padx=10,pady=10,command=lambda:handleclick("6"))
b6.grid(column=2,row=2,padx=10,pady=10)

b7=Button(root,text="7",font=24,padx=10,pady=10,command=lambda:handleclick("7"))
b7.grid(column=0,row=1,padx=10,pady=10)

b8=Button(root,text="8",font=24,padx=10,pady=10,command=lambda:handleclick("8"))
b8.grid(column=1,row=1,padx=10,pady=10)

b9=Button(root,text="9",font=24,padx=10,pady=10,command=lambda:handleclick("9"))
b9.grid(column=2,row=1,padx=10,pady=10)

b=Button(root,text="CL",font=24,padx=10,pady=10,command=handleBackspace)
b.grid(column=0,row=4,padx=10,pady=10)

 
button=Button(root,text="+",font=24,padx=10,pady=10,command=lambda:handleclick("+"))
button.grid(row=3,column=3,padx=10,pady=10)

 
button=Button(root,text="-",font=24,padx=10,pady=10,command=lambda:handleclick("-"))
button.grid(row=2,column=3,padx=10,pady=10)

 
button=Button(root,text="*",font=24,padx=10,pady=10,command=lambda:handleclick("*"))
button.grid(row=1,column=3,padx=10,pady=10)

 
button=Button(root,text="/",font=24,padx=10,pady=10,command=lambda:handleclick("/"))
button.grid(row=4,column=3,padx=10,pady=10)

button=Button(root,text="=",font=24,padx=10,pady=10,command=handleEqual)
button.grid(row=4,column=2,padx=10,pady=10)


root.mainloop()




