from tkinter import *
from operations import *

line = " "

def main():
    # Setting up the GUI
    calc = Tk()
    calc.title("Calculator App")
    calc.geometry("125x131")
    equation = StringVar()
    equation.set("Calculate!")
    expressionline = Entry(calc, textvariable=equation)
    expressionline.grid(columnspan = 5)

    #Setting up the Buttons
    clear = Button(calc,text = "Clear", width = 3, bg="gray",command = click(3))
    clear.grid(row = 0, column = 3 )
    zero = Button(calc,text = "0",width = 3, bg="gray",command = click("0"))
    zero.grid(row = 4, column = 0 )
    decimal = Button(calc,text = ".", width = 3, bg="gray",command = click("."))
    decimal.grid(row = 4, column = 1 )
    equal = Button(calc,text = "=", width = 3, bg="gray",command = equals())
    equal.grid(row = 4, column = 2 )
    plus = Button(calc,text = "+", width = 3, bg="gray",command = click("+"))
    plus.grid(row = 4, column = 3 )
    one = Button(calc,text = "1", width = 3, bg="gray",command = click("1"))
    one.grid(row = 3, column = 0 )
    two = Button(calc,text = "2", width = 3, bg="gray",command = click("2"))
    two.grid(row = 3, column = 1 )
    three = Button(calc,text = "3", width = 3, bg="gray",command = click("3"))
    three.grid(row = 3, column = 2 )
    minus = Button(calc,text = "-", width = 3, bg="gray",command = click("-"))
    minus.grid(row = 3, column = 3 )
    four = Button(calc,text = "4", width = 3, bg="gray",command = click("4"))
    four.grid(row = 2, column = 0 )
    five = Button(calc,text = "5", width = 3, bg="gray",command = click("5"))
    five.grid(row = 2, column = 1 )
    six = Button(calc,text = "6", width = 3, bg="gray",command = click("6"))
    six.grid(row = 2, column = 2 )
    multiply = Button(calc,text = "*", width = 3, bg="gray",command = click("*"))
    multiply.grid(row = 2, column = 3 )
    seven = Button(calc,text = "7", width = 3, bg="gray",command = click("7"))
    seven.grid(row = 1, column = 0 )
    eight = Button(calc,text = "8", width = 3, bg="gray",command = click("8"))
    eight.grid(row = 1, column = 1 )
    nine = Button(calc,text = "9", width = 3, bg="gray",command = click("9"))
    nine.grid(row = 1, column = 2 )
    divide = Button(calc,text = "/", width = 3, bg="gray",command = click("/"))
    divide.grid(row = 1, column = 3 )

    calc.mainloop()
if __name__ == "__main__":
    main()
