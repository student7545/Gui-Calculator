import tkinter as tk

title = "My first Graphic calculator"
dim = "900x900"

#widget creator
class widgets_creator:
    calculationvalue=""

    def __init__(self):
        self.win=tk.Tk()
        self.win.title(title)
        self.win.geometry(dim)
        self.str_var=tk.StringVar()
        #buttons
        self.win.columnconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        self.win.columnconfigure(2,weight=1)
        self.win.columnconfigure(3,weight=1)

        self.win.rowconfigure(0,weight=1)
        self.win.rowconfigure(1,weight=1)
        self.win.rowconfigure(2,weight=1)
        self.win.rowconfigure(3,weight=1)
        self.win.rowconfigure(4,weight=1)
        self.win.rowconfigure(5,weight=1)


        self.button0 = tk.Button(self.win, text="0",command=lambda:self.calculationfunction("0"))
        self.button0.grid(row=5,column=0,sticky="NEWS")

        self.buttonclear = tk.Button(self.win, text="clear",command=lambda:self.calculationfunction("clear"))
        self.buttonclear.grid(row=5, column=1, columnspan=2,sticky="NEWS")

        self.button1 = tk.Button(self.win,text="1",command=lambda:self.calculationfunction("1"))
        self.button1.grid(row=4,column=0,sticky="NEWS")

        self.button2 = tk.Button(self.win,text="2",command=lambda:self.calculationfunction("2"))
        self.button2.grid(row=4,column=1,sticky="NEWS")

        self.button3 = tk.Button(self.win,text="3",command=lambda:self.calculationfunction("3"))
        self.button3.grid(row=4,column=2,sticky="NEWS")

        self.button4 = tk.Button(self.win,text="4",command=lambda:self.calculationfunction("4"))
        self.button4.grid(row=3,column=0,sticky="NEWS")

        self.button5 = tk.Button(self.win,text="5",command=lambda:self.calculationfunction("5"))
        self.button5.grid(row=3,column=1,sticky="NEWS")

        self.button6 = tk.Button(self.win,text="6",command=lambda:self.calculationfunction("6"))
        self.button6.grid(row=3,column=2,sticky="NEWS")

        self.button = tk.Button(self.win,text="7",command=lambda:self.calculationfunction("7"))
        self.button.grid(row=2,column=0,sticky="NEWS")

        self.button = tk.Button(self.win,text="8",command=lambda:self.calculationfunction("8"))
        self.button.grid(row=2,column=1,sticky="NEWS")

        self.button = tk.Button(self.win,text="9",command=lambda:self.calculationfunction("9"))
        self.button.grid(row=2,column=2,sticky="NEWS")

        self.displaybox=tk.Label(self.win,height=5,font="bold 14",textvariable=self.str_var,relief="groove",borderwidth=4,bg="white")
        self.displaybox.grid(row=0,column=0,columnspan=3,sticky="NSWE")

        self.resultsbox=tk.Label(self.win,height=5,font="bold 14",relief="groove",borderwidth=4,bg="white")
        self.resultsbox.grid(row=1,column=0,columnspan=3,sticky="NEWS")

        self.buttonadd=tk.Button(self.win,text="+",command=lambda:self.calculationfunction("+"))
        self.buttonadd.grid(row=0,column=3,sticky="NEWS")

        self.buttontakeaway=tk.Button(self.win,text="-",command=lambda:self.calculationfunction("-"))
        self.buttontakeaway.grid(row=1,column=3,sticky="NEWS")

        self.buttondivid=tk.Button(self.win,text="/",command=lambda:self.calculationfunction("/"))
        self.buttondivid.grid(row=2,column=3,sticky="NEWS")

        self.buttonmuliple=tk.Button(self.win,text="*",command=lambda:self.calculationfunction("*"))
        self.buttonmuliple.grid(row=3,column=3,sticky="NEWS")

        self.buttonequal=tk.Button(self.win,text="=",command=lambda:self.calculationfunction("="))
        self.buttonequal.grid(row=4,rowspan=5,column=3,sticky="NEWS")

    def calculationfunction(self, x):
        if x == "=":
            try:
                result = eval(widgets_creator.calculationvalue)
            except ZeroDivisionError:
                result = "Error: Division by zero"
            except Exception as e:
                result = "Error: " + str(e)

            widgets_creator.calculationvalue = str(result)
            self.resultsbox.config(text=result)
        elif x=="clear":
            widgets_creator.calculationvalue=""
            return self.str_var.set(widgets_creator.calculationvalue)
        else:
            widgets_creator.calculationvalue+=x
            print(widgets_creator.calculationvalue,x)
            return self.str_var.set(widgets_creator.calculationvalue)


#buttons integration class
class Calculator(widgets_creator):
    def __init__(self):
        super().__init__()
        self.win.mainloop()

ob = Calculator()
