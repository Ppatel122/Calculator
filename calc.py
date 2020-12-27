from tkinter import *
line = ""

def click(char):
    """
    Registers inputs from the buttons and then changes the expression
    accordingly

    Arguments:
      char(str): the character being added to the expression
    """
    global line
    if char != "E":
        if char == "C":
            equation.set("Calculate!")
        else:
            line += char
            equation.set(line)
            return
    else:
        try:
            result = str(eval(line))
            equation.set(result)
        except:
            equation.set("Invalid")
    line = ""

if __name__ == "__main__":
    # Setting up the GUI
    calc = Tk()
    calc.title("Calculator App")
    calc.geometry("125x131")
    equation = StringVar()
    equation.set("Calculate!")
    expressionline = Entry(calc, textvariable=equation)
    expressionline.grid(columnspan = 4)

    #Setting up the Buttons
    cle = Button(calc,text = "Clear", width = 3,
                 bg="white",command = lambda:  click("C"))
    cle.grid(row = 0, column = 3 )
    zero = Button(calc,text = "0",width = 3,
                  bg="gray",command = lambda:  click("0"))
    zero.grid(row = 4, column = 0 )
    decimal = Button(calc,text = ".", width = 3,
                     bg="gray",command = lambda:  click("."))
    decimal.grid(row = 4, column = 1 )
    equal = Button(calc,text = "=", width = 3,
                   bg="gray",command = lambda:  click("E"))
    equal.grid(row = 4, column = 2 )
    plus = Button(calc,text = "+", width = 3,
                  bg="gray",command = lambda:  click("+"))
    plus.grid(row = 4, column = 3 )
    one = Button(calc,text = "1", width = 3,
                 bg="gray",command = lambda:  click("1"))
    one.grid(row = 3, column = 0 )
    two = Button(calc,text = "2", width = 3,
                  bg="gray",command = lambda:  click("2"))
    two.grid(row = 3, column = 1 )
    three = Button(calc,text = "3", width = 3,
                   bg="gray",command = lambda:  click("3"))
    three.grid(row = 3, column = 2 )
    minus = Button(calc,text = "-", width = 3,
                    bg="gray",command = lambda:  click("-"))
    minus.grid(row = 3, column = 3 )
    four = Button(calc,text = "4", width = 3,
                  bg="gray",command = lambda:  click("4"))
    four.grid(row = 2, column = 0 )
    five = Button(calc,text = "5", width = 3,
                  bg="gray",command = lambda:  click("5"))
    five.grid(row = 2, column = 1 )
    six = Button(calc,text = "6", width = 3,
                 bg="gray",command = lambda:  click("6"))
    six.grid(row = 2, column = 2 )
    multiply = Button(calc,text = "*", width = 3,
                      bg="gray",command = lambda:  click("*"))
    multiply.grid(row = 2, column = 3 )
    seven = Button(calc,text = "7", width = 3,
                   bg="gray",command = lambda:  click("7"))
    seven.grid(row = 1, column = 0 )
    eight = Button(calc,text = "8", width = 3,
                   bg="gray",command = lambda:  click("8"))
    eight.grid(row = 1, column = 1 )
    nine = Button(calc,text = "9", width = 3,
                  bg="gray",command = lambda:  click("9"))
    nine.grid(row = 1, column = 2 )
    divide = Button(calc,text = "/", width = 3,
                    bg="gray",command = lambda:  click("/"))
    divide.grid(row = 1, column = 3 )

    # Starting the GUI
    calc.mainloop()
