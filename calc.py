from tkinter import *
line = " "

def click(x):
    pass

def main():
    # Setting up the GUI
    calc = Tk()
    calc.title("Calculator App")
    calc.geometry("200x150")
    equation = StringVar()
    equation.set("Calculate!")
    expressionline = Entry(calc, textvariable=equation)
    expressionline.grid(columnspan = 5)

    #Setting up the Buttons
    clear = Button(calc,text = "Clear",height = 1, width = 7,
                    command = click(3))
    clear.grid(row = 1, column = 1 )
    zero = Button(calc,text = "0",height = 1, width = 3,command = click(0))
    zero.grid(row = 5, column = 0 )
    decimal = Button(calc,text = ".",height = 1, width = 3,command = click(2))
    decimal.grid(row = 5, column = 1 )
    equal = Button(calc,text = "=",height = 1, width = 3,command = click(3))
    equal.grid(row = 5, column = 2 )
    one = Button(calc,text = "1",height = 1, width = 3,command = click(1))
    one.grid(row = 4, column = 0 )
    two = Button(calc,text = "2",height = 1, width = 3,command = click(2))
    two.grid(row = 4, column = 1 )
    three = Button(calc,text = "3",height = 1, width = 3,command = click(3))
    three.grid(row = 4, column = 2 )
    four = Button(calc,text = "4",height = 1, width = 3,command = click(4))
    four.grid(row = 3, column = 0 )
    five = Button(calc,text = "5",height = 1, width = 3,command = click(5))
    five.grid(row = 3, column = 1 )
    six = Button(calc,text = "6",height = 1, width = 3,command = click(6))
    six.grid(row = 3, column = 2 )
    seven = Button(calc,text = "7",height = 1, width = 3,command = click(1))
    seven.grid(row = 2, column = 0 )
    eight = Button(calc,text = "8",height = 1, width = 3,command = click(2))
    eight.grid(row = 2, column = 1 )
    nine = Button(calc,text = "9",height = 1, width = 3,command = click(3))
    nine.grid(row = 2, column = 2 )

    calc.mainloop()
if __name__ == "__main__":
    main()
