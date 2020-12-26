from tkinter import *
line = " "

def click(x):
    pass

def main():
    # Setting up the GUI
    calc = Tk()
    calc.title("Calculator App")
    calc.geometry("300x200")
    equation = StringVar()
    equation.set("Calculate!")
    expressionline = Entry(calc, textvariable=equation)
    expressionline.grid(columnspan = 5)

    #Setting up the Buttons
    zero = Button(calc,text = "0",height = 1, width = 3,command = click(0))
    zero.grid(row = 4, column = 0 )
    one = Button(calc,text = "1",height = 1, width = 3,command = click(1))
    one.grid(row = 3, column = 0 )
    two = Button(calc,text = "2",height = 1, width = 3,command = click(2))
    two.grid(row = 3, column = 1 )
    three = Button(calc,text = "1",height = 1, width = 3,command = click(3))
    three.grid(row = 3, column = 2 )

    calc.mainloop()
if __name__ == "__main__":
    main()
