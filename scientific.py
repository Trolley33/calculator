import tkinter as tk
import math


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        # misc
        self.font = "Verdana"
        self.size = 14
        # Maths
        self.expression = []
        self.display_exp = []
        self.res = 0
        self.last_res = 0
        # Main buttons
        self.display = tk.Label(font=(self.font, self.size), width=20, text="", anchor='e')

        self.cancel = tk.Button(text="C", width=4, font=(self.font, self.size), command=lambda: self.click('c'))
        self.back = tk.Button(text="<-", width=4, font=(self.font, self.size), command=lambda: self.click('b'))

        self.div = tk.Button(text="÷", width=4, font=(self.font, self.size), command=lambda: self.click('/', "÷"))
        self.mult = tk.Button(text="×", width=4, font=(self.font, self.size), command=lambda: self.click('*', "×"))
        self.sub = tk.Button(text="-", width=4, font=(self.font, self.size), command=lambda: self.click('-'))
        self.add = tk.Button(text="+", width=4, font=(self.font, self.size), command=lambda: self.click('+'))
        self.ans = tk.Button(text="ANS", width=4, font=(self.font, self.size),
                             command=lambda: self.click("self.last_res", "ANS"))
        self.equal = tk.Button(text="=", width=4, font=(self.font, self.size), command=self.equal)
        # SCIENCE
        self.o_bracket = tk.Button(text="(", width=4, font=(self.font, self.size), command=lambda: self.click('('))
        self.c_bracket = tk.Button(text=")", width=4, font=(self.font, self.size), command=lambda: self.click(')'))

        self.sin = tk.Button(text="sin", width=4, font=(self.font, self.size),
                             command=lambda: self.click('self.sine(', 'sin('))
        self.cos = tk.Button(text="cos", width=4, font=(self.font, self.size),
                             command=lambda: self.click('self.cosine(', 'cos('))
        self.tan = tk.Button(text="tan", width=4, font=(self.font, self.size),
                             command=lambda: self.click('self.tangent(', 'tan('))
        self.pi = tk.Button(text="π", width=4, font=(self.font, self.size),
                            command=lambda: self.click('math.pi', 'π'))
        self.e = tk.Button(text="e", width=4, font=(self.font, self.size),
                           command=lambda: self.click('math.e', 'e'))

        self.isin = tk.Button(text="asin", width=4, font=(self.font, self.size),
                              command=lambda: self.click('self.isine(', 'asin('))
        self.icos = tk.Button(text="acos", width=4, font=(self.font, self.size),
                              command=lambda: self.click('self.icosine(', 'acos('))
        self.itan = tk.Button(text="atan", width=4, font=(self.font, self.size),
                              command=lambda: self.click('self.itangent(', 'atan('))
        self.pow = tk.Button(text="x^y", width=4, font=(self.font, self.size), command=lambda: self.click('**', '^'))
        self.root = tk.Button(text="√", width=4, font=(self.font, self.size),
                              command=lambda: self.click('math.sqrt(', '√('))

        self.nums = []

        for i in range(3):
            for j in range(3):
                if i == 0:
                    x = j+7
                if i == 1:
                    x = j+4
                if i == 2:
                    x = j+1
                self.nums.append(tk.Button(text=x, width=4, font=(self.font, self.size),
                                           command=lambda y=x: self.click(y)))
        self.nums.append(tk.Button(text="0", width=4, font=(self.font, self.size), command=lambda: self.click(0)))

        self.period = tk.Button(text=".", width=4, font=(self.font, self.size), command=lambda: self.click('.'))

        self.draw()
        self.root.mainloop()

    def sine(self, ang):
        return math.sin(math.radians(ang))

    def cosine(self, ang):
        return math.cos(math.radians(ang))

    def tangent(self, ang):
        return math.tan(math.radians(ang))

    def isine(self, num):
        return math.degrees(math.asin(num))

    def icosine(self, num):
        return math.degrees(math.acos(num))

    def itangent(self, num):
        return math.degrees(math.atan(num))

    def click(self, op, sym=''):
        print(len(self.display.cget('text')))
        if op not in ['b', 'c']:
            if len(self.display.cget('text')) == 14:
                return
            self.expression.append(op)
            if sym:
                self.display_exp.append(sym)
            else:
                self.display_exp.append(op)
        elif op == 'b':
            if len(self.expression):
                del self.expression[-1]
                del self.display_exp[-1]
        elif op == 'c':
            self.expression = []
            self.display_exp = []

        text = ''.join([str(x) for x in self.display_exp])
        self.display.configure(text=text)

    def equal(self):
        try:
            self.res = eval(''.join([str(x) for x in self.expression]))
            self.last_res = self.res
            # turn ints with decimal points into ints
            if self.res - int(self.res) == 0:
                self.res = int(self.res)
            self.res = str(self.res)
            self.expression = []
            self.display_exp = []
            self.expression += list(self.res)
            self.display_exp += list(self.res)
            self.display.configure(text=self.res)
        except SyntaxError:
            self.display.configure(text="Syntax error!")
            self.expression = []
            self.display_exp = []
        except Exception as e:
            raise e

    def draw(self):
        self.display.grid(column=0, row=0, columnspan=6, sticky="NEWS")
        self.cancel.grid(column=2, row=1)
        self.back.grid(column=0, row=1, columnspan=2, sticky="NEWS")

        self.sin.grid(column=0, row=2)
        self.cos.grid(column=1, row=2)
        self.tan.grid(column=2, row=2)
        self.pi.grid(column=3, row=2)
        self.e.grid(column=4, row=2)

        self.isin.grid(column=0, row=3)
        self.icos.grid(column=1, row=3)
        self.itan.grid(column=2, row=3)
        self.pow.grid(column=3, row=3)
        self.root.grid(column=4, row=3)

        self.o_bracket.grid(column=3, row=4)
        self.c_bracket.grid(column=4, row=4)

        self.div.grid(column=3, row=5)
        self.mult.grid(column=4, row=5)

        self.sub.grid(column=3, row=6)
        self.add.grid(column=4, row=6)

        self.ans.grid(column=3, row=7)
        self.equal.grid(column=4, row=7)

        for i, j in enumerate(self.nums):
            if i < 3:
                j.grid(column=i, row=4)
            if 3 <= i < 6:
                j.grid(column=i-3, row=5)
            if 6 <= i < 9:
                j.grid(column=i-6, row=6)
            if 9 <= i:
                j.grid(column=i-9, row=7, columnspan=2, sticky="NEWS")

        self.period.grid(column=2, row=7)

app = App()
