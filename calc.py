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
    # If the user presses equals, we evaluate the expression and check for
    # an error
    if char == "E":
        try:
            result = str(eval(line))
            equation.set(result)
        except:
            equation.set("Invalid")
    # If the user presses a button other than equals, we modify the equation
    # accordingly
    else:
        if char == "C":
            equation.set("Calculate!")
        else:
            line += char
            equation.set(line)
            return
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
                 bg="red",command = lambda:  click("C"))
    zero = Button(calc,text = "0",width = 3,
                  bg="gray",command = lambda:  click("0"))
    decimal = Button(calc,text = ".", width = 3,
                     bg="white",command = lambda:  click("."))
    equal = Button(calc,text = "=", width = 3,
                   bg="white",command = lambda:  click("E"))
    plus = Button(calc,text = "+", width = 3,
                  bg="white",command = lambda:  click("+"))
    one = Button(calc,text = "1", width = 3,
                 bg="gray",command = lambda:  click("1"))
    two = Button(calc,text = "2", width = 3,
                  bg="gray",command = lambda:  click("2"))
    three = Button(calc,text = "3", width = 3,
                   bg="gray",command = lambda:  click("3"))
    minus = Button(calc,text = "-", width = 3,
                    bg="white",command = lambda:  click("-"))
    four = Button(calc,text = "4", width = 3,
                  bg="gray",command = lambda:  click("4"))
    five = Button(calc,text = "5", width = 3,
                  bg="gray",command = lambda:  click("5"))
    six = Button(calc,text = "6", width = 3,
                 bg="gray",command = lambda:  click("6"))
    multiply = Button(calc,text = "*", width = 3,
                      bg="white",command = lambda:  click("*"))
    seven = Button(calc,text = "7", width = 3,
                   bg="gray",command = lambda:  click("7"))
    eight = Button(calc,text = "8", width = 3,
                   bg="gray",command = lambda:  click("8"))
    nine = Button(calc,text = "9", width = 3,
                  bg="gray",command = lambda:  click("9"))
    divide = Button(calc,text = "/", width = 3,
                    bg="white",command = lambda:  click("/"))

    #Placing the buttons
    cle.grid(row = 0, column = 3 )
    zero.grid(row = 4, column = 0 )
    decimal.grid(row = 4, column = 1 )
    equal.grid(row = 4, column = 2 )
    plus.grid(row = 4, column = 3 )
    one.grid(row = 3, column = 0 )
    two.grid(row = 3, column = 1 )
    three.grid(row = 3, column = 2 )
    minus.grid(row = 3, column = 3 )
    four.grid(row = 2, column = 0 )
    five.grid(row = 2, column = 1)
    six.grid(row = 2, column = 2 )
    multiply.grid(row = 2, column = 3 )
    seven.grid(row = 1, column = 0 )
    eight.grid(row = 1, column = 1 )
    nine.grid(row = 1, column = 2 )
    divide.grid(row = 1, column = 3 )

    # Starting the GUI
    calc.mainloop()
