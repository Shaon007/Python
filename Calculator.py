from tkinter import *

class MyWindow:
    def __init__(self, win):
       #overall background
        win.configure(bg='black')

        # Headlines
        self.lbl1 = Label(win, text='First Number:', font=('Arial', 12), fg='white', bg='black')
        self.lbl2 = Label(win, text='Second Number:', font=('Arial', 12), fg='white', bg='black')
        self.lbl3 = Label(win, text='Result:', font=('Arial', 12), fg='white', bg='black')

        # Input fields
        self.t1 = Entry(win, bd=3,bg='lavender', font=('Arial', 12))
        self.t2 = Entry(win, bd=3, bg='lavender', font=('Arial', 12))
        self.t3 = Entry(win, bd=3, font=('Arial', 12), state='readonly')

        # Buttons
        self.btn1 = Button(win, text='Add', font=('Arial', 10, 'bold'), bg='lightgreen', command=self.add)
        self.btn2 = Button(win, text='Subtract', font=('Arial', 10, 'bold'), bg='lightblue')
        self.btn3 = Button(win, text='Multiply', font=('Arial', 10, 'bold'), bg='lightyellow')
        self.btn4 = Button(win, text='Divide', font=('Arial', 10, 'bold'), bg='lightcoral')

        # Event bindings
        self.btn2.bind('<Button-1>', self.sub)
        self.btn3.bind('<Button-1>', self.mul)
        self.btn4.bind('<Button-1>', self.div)

        # Placement of elements
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=250, y=50, width=200)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=250, y=100, width=200)
        self.btn1.place(x=100, y=160, width=100)
        self.btn2.place(x=210, y=160, width=100)
        self.btn3.place(x=320, y=160, width=100)
        self.btn4.place(x=430, y=160, width=100)
        self.lbl3.place(x=100, y=220)
        self.t3.place(x=250, y=220, width=200)

    # Arithmetic operations
    def add(self):
        self.t3.config(state=NORMAL)  # Allow editing
        self.t3.delete(0, 'end')
        try:
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 + num2
            self.t3.insert(END, str(result))
        except ValueError:
            self.t3.insert(END, "Invalid input")
        self.t3.config(state='readonly')  # Set back to readonly

    def sub(self, event):
        self.t3.config(state=NORMAL)
        self.t3.delete(0, 'end')
        try:
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 - num2
            self.t3.insert(END, str(result))
        except ValueError:
            self.t3.insert(END, "Invalid input")
        self.t3.config(state='readonly')

    def mul(self, event):
        self.t3.config(state=NORMAL)
        self.t3.delete(0, 'end')
        try:
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 * num2
            self.t3.insert(END, str(result))
        except ValueError:
            self.t3.insert(END, "Invalid input")
        self.t3.config(state='readonly')

    def div(self, event):
        self.t3.config(state=NORMAL)
        self.t3.delete(0, 'end')
        try:
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            if num2 == 0:
                self.t3.insert(END, "Cannot divide by zero")
            else:
                result = num1 / num2
                self.t3.insert(END, str(result))
        except ValueError:
            self.t3.insert(END, "Invalid input")
        self.t3.config(state='readonly')

# Create window
window = Tk()
mywin = MyWindow(window)
window.title('Arithmetic Operations with Tkinter')
window.geometry("600x350+10+10")
window.mainloop()
