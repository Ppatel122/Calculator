from tkinter import *
line = ""
class Calculator(Tk):
    def __init__(self):
        # Setting up the GUI
        super().__init__()
        self.title("Calculator App")
        self.geometry("125x131")
        self.equation = StringVar()
        self.equation.set("Calculate!")
        self.expressionline = Entry(self, textvariable=self.equation)
        self.expressionline.grid(columnspan = 4)
        self.widgetsetup()

    def widgetsetup(self):
        #Setting up the Buttons
        cle = Button(self,text = "Clear", width = 3,
                     bg="red",command = lambda:  self.click("C"))
        zero = Button(self,text = "0",width = 3,
                      bg="gray",command = lambda:  self.click("0"))
        decimal = Button(self,text = ".", width = 3,
                         bg="white",command = lambda:  self.click("."))
        equal = Button(self,text = "=", width = 3,
                       bg="white",command = lambda:  self.click("E"))
        plus = Button(self,text = "+", width = 3,
                      bg="white",command = lambda:  self.click("+"))
        one = Button(self,text = "1", width = 3,
                     bg="gray",command = lambda:  self.click("1"))
        two = Button(self,text = "2", width = 3,
                      bg="gray",command = lambda:  self.click("2"))
        three = Button(self,text = "3", width = 3,
                       bg="gray",command = lambda:  self.click("3"))
        minus = Button(self,text = "-", width = 3,
                        bg="white",command = lambda:  self.click("-"))
        four = Button(self,text = "4", width = 3,
                      bg="gray",command = lambda:  self.click("4"))
        five = Button(self,text = "5", width = 3,
                      bg="gray",command = lambda:  self.click("5"))
        six = Button(self,text = "6", width = 3,
                     bg="gray",command = lambda:  self.click("6"))
        multiply = Button(self,text = "*", width = 3,
                          bg="white",command = lambda:  self.click("*"))
        seven = Button(self,text = "7", width = 3,
                       bg="gray",command = lambda:  self.click("7"))
        eight = Button(self,text = "8", width = 3,
                       bg="gray",command = lambda:  self.click("8"))
        nine = Button(self,text = "9", width = 3,
                      bg="gray",command = lambda:  self.click("9"))
        divide = Button(self,text = "/", width = 3,
                        bg="white",command = lambda:  self.click("/"))

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

    def click(self,char):
        global line
        # If the user presses equals, we evaluate the expression and check for
        # an error
        if char == "E":
            try:
                result = str(eval(line))
                self.equation.set(result)
            except:
                self.equation.set("Invalid")
        # If the user presses a button other than equals, we modify the equation
        # accordingly
        else:
            if char == "C":
                self.equation.set("Calculate!")
            else:
                line += char
                self.equation.set(line)
                return
        line = ""

if __name__ == "__main__":
    # Starting the GUI
    calc = Calculator()
    calc.mainloop()
