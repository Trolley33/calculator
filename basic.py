import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        # misc
        self.font = "Verdana"
        self.size = 14
        # Maths
        self.expression = []
        self.display_exp = []
        # Main buttons
        self.display = tk.Label(font=(self.font, self.size), text="", anchor='e')

        self.cancel = tk.Button(text="C", width=3, font=(self.font, self.size), command=lambda: self.click('c'))
        self.back = tk.Button(text="<-", width=3, font=(self.font, self.size), command=lambda: self.click('b'))

        self.div = tk.Button(text="÷", width=3, font=(self.font, self.size), command=lambda: self.click('/', "÷"))
        self.mult = tk.Button(text="×", width=3, font=(self.font, self.size), command=lambda: self.click('*', "×"))
        self.sub = tk.Button(text="-", width=3, font=(self.font, self.size), command=lambda: self.click('-'))
        self.add = tk.Button(text="+", width=3, font=(self.font, self.size), command=lambda: self.click('+'))
        self.equal = tk.Button(text="=", width=3, font=(self.font, self.size), command=self.equal)

        self.nums = []

        for i in range(3):
            for j in range(3):
                if i == 0:
                    x = j+7
                if i == 1:
                    x = j+4
                if i == 2:
                    x = j+1
                self.nums.append(tk.Button(text=x, width=3, font=(self.font, self.size), command=lambda y=x: self.click(y)))
        self.nums.append(tk.Button(text="0", width=3, font=(self.font, self.size), command=lambda: self.click(0)))

        self.period = tk.Button(text=".", width=3, font=(self.font, self.size), command=lambda: self.click('.'))

        self.draw()
        self.root.mainloop()

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
            res = eval(''.join([str(x) for x in self.expression]))
            # turn ints with decimal points into ints
            if res - int(res) == 0:
                res = int(res)
            res = str(res)
            self.expression = []
            self.display_exp = []
            self.expression += list(res)
            self.display_exp += list(res)
            self.display.configure(text=res)
        except SyntaxError:
            self.display.configure(text="Syntax error!")
            self.expression = []
            self.display_exp = []
        except Exception as e:
            raise e

    def draw(self):
        self.display.grid(column=0, row=0, columnspan=4, sticky="NEWS")
        self.cancel.grid(column=2, row=1)
        self.back.grid(column=0, row=1, columnspan=2, sticky="NEWS")

        self.div.grid(column=3, row=1)
        self.mult.grid(column=3, row=2)
        self.sub.grid(column=3, row=3)
        self.add.grid(column=3, row=4)
        self.equal.grid(column=3, row=5)

        for i, j in enumerate(self.nums):
            if i < 3:
                j.grid(column=i, row=2)
            if 3 <= i < 6:
                j.grid(column=i-3, row=3)
            if 6 <= i < 9:
                j.grid(column=i-6, row=4)
            if 9 <= i:
                j.grid(column=i-9, row=5, columnspan=2, sticky="NEWS")

        self.period.grid(column=2, row=5)

app = App()
