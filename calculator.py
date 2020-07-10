#!/usr/bin/env python3
from tkinter import *
import random
import threading
from requests import *
import time
from bs4 import *
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fCt
from numpy import *
import pandas as pd
import bs4
import class_state as cs
import tkinter.scrolledtext as sText
import pytexit
class XanderCalculator:
    def __init__(self):
        self.stack = []
        self.l_no = len(self.stack)
        self.row = 0
        self.column = 0
        self.index = 0
        self.gui()
        self.mw.mainloop()
    def entry_text(self, text):
        self.entry.insert(END, str(text))
    def gui(self):
        self.mw = Tk()
        self.mw.title('XanderCalculator')
        self.mw.resizable(False, False)
        self.entry = Entry(self.mw,
                           font =  ('TlwgTypist', 15, 'bold'),
                           bd = 4,
                           relief = GROOVE)
        self.entry.pack(fill = X)
        self.m_frame =  Frame(self.mw)
        self.m_frame.pack(side = LEFT)
        self.b1 = Button(self.m_frame,text='1',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('1'))
        self.b2 = Button(self.m_frame,text='2',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('2'))
        self.b3 = Button(self.m_frame,text='3',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('3'))
        self.o1 = Button(self.m_frame,text='+',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('+'))
        self.o2 = Button(self.m_frame,text='-',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('-'))
        self.b4 = Button(self.m_frame,text='4',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('4'))
        self.b5 = Button(self.m_frame,text='5',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('5'))
        self.b6 = Button(self.m_frame,text='6',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('6'))
        self.o3 = Button(self.m_frame,text='x',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('*'))
        self.o4 = Button(self.m_frame,text='/',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('/'))
        self.b7 = Button(self.m_frame,text='7',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('7'))
        self.b8 = Button(self.m_frame,text='8',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('8'))
        self.b9 = Button(self.m_frame,text='9',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('9'))
        self.o5 = Button(self.m_frame,text='0',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('0'))
        self.o6 = Button(self.m_frame,text='=',bd=5,relief='groove',bg='grey',fg='black',command = self.both)
        self.clr = Button(self.m_frame,text='Clr',bd=5,relief='groove',bg='grey',fg='black',command=self.clr)
        self.back = Button(self.m_frame,text='<--',bd=5,relief='groove',bg='grey',fg='black',command = self.backspace)
        self.mod = Button(self.m_frame, text='%',bd=5,relief='groove',bg='grey',fg='black',command=lambda:self.entry_text('%'))
        self.lis = [[self.b1,self.b2,self.b3,self.o1,self.o2],
               [self.b4,self.b5,self.b6,self.o3,self.o4],
               [self.b7,self.b8,self.b9,self.o5,self.o6]]
        self.lis2 = [self.clr, self.back, self.mod]
        for l in range(3):
            for j in range(5):
                self.lis[l][j]['width'] = 5
                self.lis[l][j]['font'] = ('arial', 15, 'bold')
                self.lis[l][j].grid(row = l, column = j)
        self.clr['width'] = 5
        self.clr['font'] = ('arial', 15, 'bold')
        self.clr.grid(row = 2, column = 5)
        self.back['width'] = 5
        self.back['font'] = ('arial', 15, 'bold')
        self.back.grid(row = 1, column = 5)
        self.mod['width'] = 5
        self.mod['font'] = ('arial', 15, 'bold')
        self.mod.grid(row = 0, column = 5)
        self.mw.bind('<Return>', self.both)
        self.mw.bind('<Control-s>', self.google_search)
        self.mw.bind('<Control-e>', self.solve)
        self.mw.bind('<Control-n>', self.newton_forward)
        self.mw.bind('<Control-b>', self.bisection)
        self.mw.bind('<Control-f>', self.func)
        self.mw.bind('<Control-g>', self.func_eval)
        self.mw.bind('<Control-j>', self.func_eval1)
        self.mw.bind('<Control-r>', self.roots)
        self.mw.bind('<Control-R>', self.runge_kutta)
        self.mw.bind('<Control-i>', self.eigen_vals)
        self.mw.bind('<Control-p>', self.parabola)
        self.mw.bind('<Control-F>', self.false_position)
        self.mw.bind('<Control-l>', self.straight_line)
        self.mw.bind('<Control-I>', self.inverse)
        self.mw.bind('<Control-N>', self.numerical_integration)
        self.mw.bind('<Control-P>', self.newton_raphson)
        self.mw.bind('<Control-Up>', self.undo)
        self.mw.bind('<Control-Down>', self.redo)
        self.mw.bind('<Control-k>', self.instructions)
        self.mw.bind('<Control-T>', self.truth_tables)
    def instructions(self, *args):
        self.window = Toplevel()
        self.window.config(bg = 'black')
        self.window.title('XanderCalculator')
        h1 = Label(self.window,
                   text = 'Shortcuts......',
                   font = ('URWGothic', 15, 'bold'),
                   fg = 'cyan',
                   bg = 'black')
        h1.pack()
        text = '''
Control-s
Control-e
Control-n
Control-b
Control-f
Control-g
Control-j
Control-r
Control-R
Control-i
Control-p
Control-F
Control-l
Control-I
Control-N
Control-P
Control-Up
Control-Down
'''
        text1 = '''Google Search
Equation Solver
Netwon Interpolation
Bisection Method
Function Loader
Function Evaluator(1 variable)
Function Evaluator(2 variables)
Roots of a polynomial
RungeKutta Method
EigenValues & EigenVectors
Curve Fitting into a parabola
Regula-Falsi or The False Position Method
Curve Fitting into a straight line
Inverse Of a Matrix
Numerical Integration
Newton Raphson
Previous Input
Next Input'''
        frame = Frame(self.window, bg = 'black')
        frame.pack(side = LEFT)
        Message(frame,
                text = text,
                font = ('TlwgTypist', 12, 'bold'),
                fg = 'white',
                bg = 'black').pack(side = LEFT)
        Message(frame,
                text = text1,
                font = ('TlwgTypist', 12, 'bold'),
                fg = 'white',
                bg = 'black').pack(side = LEFT)
    def both(self, *args):
        t1 = threading.Thread(target = self.validator)
##        t2 = threading.Thread(target = self.animation)
        t1.start()
##        t2.start()
    def mechanism(self):
        self.l_no = -1
        expr = self.entry.get()
        if len(self.stack) != 0:
            if self.stack[-1] != expr and expr != '': 
                self.stack.append(expr)
        else:
            self.stack.append(expr)
        self.l_no = len(self.stack)
    def validator(self, *args):
        self.mechanism()
        try:
            expr = self.entry.get()
            expr = expr.replace('^', '**')
            expr = expr.replace('rad', 'radians')
            x = round(eval(str(expr)), 4)
            self.entry.delete(0, END)
            self.entry.insert(0, x)
        except:
            self.entry.delete(0, END)
            self.entry.insert(0, 'Invalid Expression')
    def clr(self):
        self.entry.delete(0, END)
    def backspace(self):
        text = self.entry.get()
        self.entry.delete(0,END)
        self.entry.insert(0, text[:-1])
    def animation(self, *args):
        self.entry['bg'] = 'black'
        self.entry['fg'] = 'cyan'
        self.entry['font'] = ('Times', 15, 'italic')
        color = random.choice(['yellow', 'cyan', 'lightgreen', 'lightblue', 'green', 'red', 'blue', 'violet'])
        if self.row < 3 and self.column < 5:
            if self.column - 1 != -1:
                self.lis[self.row][self.column - 1]['bg'] = 'grey'
            else:
                self.lis[self.row - 1][4]['bg'] = 'grey'
            self.lis[self.row][self.column]['bg'] = color
            self.column += 1
            if self.column == 5:
                self.column = 0
                self.row += 1
            self.m_frame.after(80, self.animation)
        else:
            self.lis[2][4]['bg'] = 'black'
            self.row = 0
            self.column = 0
            self.entry['bg'] = 'white'
            self.entry['fg'] = 'black'
            self.entry['font'] = ('TlwgTypist', 15, 'bold')
    def anim2(self):
        color = random.choice(['yellow', 'cyan', 'lightgreen', 'lightblue', 'green', 'red', 'blue', 'violet'])
        if self.index < 3:
            self.lis2[self.index - 1]['bg'] = 'black'
            self.index += 1
        if self.index == 3:
            self.index = 0
        self.lis2[self.index]['bg'] = color
        self.m_frame.after(120, self.anim2)
    def google_search(self, *args):
        t1 = threading.Thread(target = self.google_search1)
        t1.start()
    def google_search1(self):
        print('Entered this')
        inp = self.entry.get().replace(' ', '+')
        proxies = {'http':'http://labasst01_cse:bhavani@10.20.3.11:3128/',
                   'https':'https://labasst01_cse:bhavani@10.20.3.11:3128/'}
        session = Session()
        session.proxies = proxies
        print(f'https://www.google.com/search?q={inp}')
        req = session.get(f'https://www.google.com/search?q={inp}')
        print(req)
        string = ''
        obj = bs4.BeautifulSoup(req.text, 'lxml')
        with open('some.html', 'w') as some:
            some.write(obj.prettify())
        for j in obj.find_all('a'):
            if 'https' in j['href'] and 'quora' in j['href']:
                req1 = session.get(j['href'][7:j['href'].find('&')])
                obj1 = bs4.BeautifulSoup(req1.text, 'lxml')
                for j in obj1.find_all('p'):
                    string += j.text + '\n'
                break
        with open('pkg.txt', 'w') as file:
            file.write(string)
        top =Toplevel()
        top.title('XanderGoogleSearch')
        st = sText.ScrolledText(top)
        st.insert('insert', string)
        st.pack(fill=BOTH, expand=1, padx=5, pady=5)
        top.mainloop()
    def search_mode(self):
        for l in range(3):
            for j in range(5):
                self.lis[l][j]['text'] = ''
        for l in self.lis2:
            l['text'] = ''
        for n in range(5):
            self.tempo1()
            time.sleep(0.5)
            self.tempo2()
            time.sleep(0.5)
        self.lis[2][4]['bg'] = self.lis[2][1]['bg'] = self.lis[2][0]['bg'] = self.lis[1][3]['bg'] = self.lis[1][2]['bg'] = self.lis[0][4]['bg'] = self.lis[0][1]['bg'] = self.lis[0][0]['bg'] = 'cyan'
        self.lis2[0]['bg'] = self.lis2[2]['bg'] = 'cyan'
        self.lis[0][2]['bg'] = self.lis[0][3]['bg'] = self.lis[1][0]['bg'] = self.lis[1][1]['bg'] =  self.lis[1][4]['bg']  = self.lis[2][2]['bg'] = self.lis[2][3]['bg'] = 'black'
        self.lis2[1]['bg'] = 'black'
        time.sleep(2)
        for l in range(3):
            for j in range(5):
                self.lis[l][j]['bg'] = 'black'
                self.lis[l][j]['text'] = 'X'
                self.lis[l][j]['fg'] = 'cyan'
                time.sleep(0.5)
        for x in range(3):
            self.lis2[x]['bg'] = 'black'
            self.lis2[x]['fg'] = 'cyan'
            self.lis2[x]['text'] = 'X'
            time.sleep(0.5)
        self.m_frame.destroy()
        self.m_frame = Frame(self.mw)
        self.m_frame.pack(fill = X)
        self.s1 = Button(self.m_frame,text='Search',bd=5,relief='groove',fg='white',bg='black', width = 10, font = ('arial', 15, 'bold'), command = lambda :self.google_search(0))
        self.s2 = Button(self.m_frame,text='Intense',bd=5,relief='groove',fg='white',bg='black', width = 10, font = ('arial', 15, 'bold'), command = lambda :self.google_search(1))
        self.s1.pack(side = LEFT, fill = X)
        self.s2.pack(side = RIGHT, fill = X)
    def tempo1(self):
        print("Hello1") 
        for l in range(3):
            for j in range(5):
                if l % 2 == 0 and j % 2 == 0:
                    self.lis[l][j]['bg'] = 'red'
                    continue
                else:
                    self.lis[l][j]['bg'] = 'cyan'
                if l % 2 !=0 and j % 2 != 0:
                    self.lis[l][j]['bg'] = 'red'
                    continue
                else:
                    self.lis[l][j]['bg'] = 'cyan'
        self.lis2[1]['bg'] = 'red'
        self.lis2[0]['bg'] = self.lis2[2]['bg'] = 'cyan'
    def tempo2(self):
        print("Hello2")
        for l in range(3):
            for j in range(5):
                if l % 2 == 0 and j % 2 != 0:
                    self.lis[l][j]['bg'] = 'red'
                    continue
                else:
                    self.lis[l][j]['bg'] = 'cyan'
                if l % 2 != 0 and j % 2 == 0:
                    self.lis[l][j]['bg'] = 'red'
                    continue
                else:
                    self.lis[l][j]['bg'] = 'cyan'
        self.lis2[0]['bg'] = self.lis2[2]['bg'] = 'red'
        self.lis2[1]['bg'] = 'cyan'
    def solve(self, *args):
        self.mechanism()
        data = self.entry.get()
        m_lis = data.split(';')
        n_lis = []
        for j in m_lis:
            temp = [float(x) for x in j.split(',')]
            n_lis.append(temp)
        eqs = n_lis[:-1]
        cons = n_lis[-1]
        try:
            solutions = linalg.solve(eqs, cons)
            string = ''
            for j in solutions:
                string += str(round(j, 4)) + '\n'
        except linalg.LinAlgError:
            string = 'No roots'
        obj = open('data.txt', 'w')
        obj.write(string)
        obj.close()
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind)
        some.insert('insert', string)
        some.pack()
        n_wind.bind('destroy', self.clr)
        n_wind.mainloop()
    def bisection(self, *args):
        self.mechanism()
        # BISECTION METHOD
        fx,a,b =  str(self.entry.get()).split(';')
        fx = fx.replace('^', '**')
        fx = fx.replace('rad', 'radians')
        a = float(round(eval(a), 3))
        b = float(round(eval(b), 3))
        df = pd.DataFrame(columns = ['Iteration', 'a', 'b', 'xr', 'f(xr)', 'Sign', 'Error'])
        it = 0
        while it < 12:
            xr = round((a + b) / 2, 4)
            fxr = round(eval(fx.replace('x', str(xr))), 4)
            try:
                data = [it + 1, a, b, xr, fxr, 'Negative' if float(fxr) < 0 else 'Positive', round(abs((xr - (df.loc[it - 1, 'xr']))/xr) * 100, 4)]
            except KeyError:
                data = [it + 1, a, b, xr, fxr, 'Negative' if float(fxr) < 0 else 'Positive', '-']
            if fxr > 0:
                b = xr
            else:
                a = xr
            s = pd.Series(data, index = ['Iteration', 'a', 'b', 'xr', 'f(xr)', 'Sign', 'Error'])
            df = df.append(s, ignore_index = True)
            it += 1
        with open('data.txt', 'w') as file:
            file.write(df.__repr__())
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind,
                                  font = ('TlwgTypist', 12, 'bold'),
                                  bg = 'black',
                                  fg = 'white')
        some.insert('insert', df.__repr__())
        some.insert('insert', '\n\nROOT:' + str(list(df['xr'])[-1]))
        some.pack()
        n_wind.bind('destroy', self.clr)
        n_wind.mainloop()
    def false_position(self, *args):
        self.mechanism()
        #REGULA_FALSI METHOD
        data = self.entry.get().split(';')
        fx = data[0]
        fx = fx.replace('^', '**')
        fx = fx.replace('rad', 'radians')
        a = float(round(eval(data[1]), 3))
        b = float(round(eval(data[2]), 3))
        df = pd.DataFrame(columns = ['Iteration', 'a', 'b', 'xr', 'fxr', 'Sign', 'Error'])
        it = 0
        while it < 13:
            fa = round(eval(fx.replace('x', str(a))), 6)
            fb = round(eval(fx.replace('x', str(b))), 6)
            xr = round((a*fb-b*fa)/(fb-fa), 6)
            fxr = round(eval(fx.replace('x', str(xr))), 6)
            try:
                data = [it + 1, a, b, xr, fxr, 'Negative' if fxr < 0 else 'Positive', round(abs((xr - (df.loc[it - 1, 'xr']))/xr) * 100, 6)]
            except KeyError:
                data = [it + 1, a, b, xr, fxr, 'Negative' if fxr < 0 else 'Positive', '-']
            if fxr < 0:
                a = xr
            else:
                b = xr
            series = pd.Series(data, index = ['Iteration', 'a', 'b', 'xr', 'fxr', 'Sign', 'Error'])
            df = df.append(series, ignore_index = True)
            it += 1
        with open('data.txt', 'w') as file:
            file.write(df.__repr__())
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind,
                                  bg = 'black',
                                  fg = 'cyan',
                                  font = ('TlwgTypist', 12, 'bold'))
        some.insert('insert', df.__repr__() + '\n\nROOT:' + str(list(df['xr'])[-1]))
        some.pack()
        n_wind.bind('destroy', self.clr)
        n_wind.mainloop()
    def func(self, *args):
        self.mechanism()
        self.fun = self.entry.get()
        self.fun = self.fun.replace('^', '**')
        self.fun = self.fun.replace('rad', 'radians')
        self.entry.delete(0, END)
    def func_eval(self, *args):
        self.mechanism()
        num = self.entry.get()
        val = round(eval(str(self.fun.replace('x', num))), 4)
        self.entry.delete(0, END)
        self.entry.insert(END, str(val))
    def func_eval1(self, *args):
        self.mechanism()
        num = self.entry.get().split(',')
        print(num[0], num[1])
        temp = str(self.fun.replace('y', num[1]))
        val = round(eval(str(temp.replace('x', num[0]))), 4)
        print(val)
        self.entry.delete(0, END)
        self.entry.insert(END, str(val))
    def newton_forward(self, *args):
        self.mechanism()
        inp = self.entry.get().split(';')
        wages = [float(x) for x in inp[0].split(',')]
        workers = [float(x) for x in inp[1].split(',')]
        new = float(inp[-1])
        df = pd.DataFrame([wages, workers])
        df = df.T
        df.columns = ['x', 'y']
        del_f = [workers]
        for j in range(len(wages) - 1):
            temp = []
            for k in range(len(del_f[-1]) - 1):
                temp.append(del_f[-1][k + 1] - del_f[-1][k])
            del_f.append(temp)
        s = 1
        for l in del_f[1:]:
            m = pd.Series(l)
            df[f"del{s}_f"] = m
            s += 1
        if wages[0] < new < wages[1]:
            a = wages[0]
        else:
            a = wages[-1]
        h = wages[1] - wages[0]
        u = (new - a) / h
        arr1 = []
        arr2 = []
        # Series Calculation
        su = 0
        array = []
        if wages[0] < new < wages[1]:
            for k in range(1, len(del_f)):
                su += (self.u_term(u, k - 1) * (df[f'del{k}_f'][0]))/ self.fact(k)
                array.append(df[f'del{k}_f'][0])
                arr1.append((self.u_term(u, k - 1) * (df[f'del{k}_f'][0]))/ self.fact(k))
                arr2.append(self.u_term(u, k - 1))
            flag = 0
        else:
            for k in range(1, len(del_f)):
                array.append(df[f'del{k}_f'][len(del_f) - k - 1])
                su += (self.u_term1(u, k - 1) * (df[f'del{k}_f'][len(del_f) - k - 1]/ self.fact(k)))
                arr1.append((self.u_term1(u, k - 1) * (df[f'del{k}_f'][len(del_f) - k - 1])/ self.fact(k)))
                arr2.append(self.u_term1(u, k - 1))
            flag = 1
        df = df.fillna('')
        with open('some.txt', 'w') as file:
            file.write(df.__repr__())
            if flag == 0:
                file.write('\n' + str(su + workers[0]))
            else:
                file.write('\n' + str(su + workers[-1]))
        n_wind = Toplevel()
        n_wind.title = 'Newton Interpolation Table'
        label = Label(n_wind)
        label.pack(fill = X)
        fig = matplotlib.figure.Figure(figsize = (20, 4), dpi = 100)
        self.ax = fig.add_subplot(111)
        self.canvas = fCt(fig, master = label)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        some = sText.ScrolledText(n_wind,
                                  bg = 'black',
                                  fg = 'white',
                                  font = ('TlwgTypist', 12, 'bold'))
        some.insert('insert', df.__repr__() + '\n\n\n' + 'f({})='.format(new) + (str(su + workers[0]) if flag == 0 else str(su + workers[-1])))
        some.pack()
        if flag == 0:
            self.newton_formula(a, u, h, array, workers[0], arr1, arr2, su, new, flag)
        else:
            self.newton_formula(a, u, h, array, workers[-1], arr1, arr2, su, new, flag)
        n_wind.bind('destroy', self.clr)
        n_wind.mainloop()
    def newton_formula(self, a, u, h, array, fa, arr1, arr2, tot, new, flag):
        if flag == 0:
            formula = '$f(a + hu) = f(a) + \\frac{u}{1!} \\Delta f(a)+\\frac{u(u-1)}{2!}{\\Delta^{2}}{f(a)}+\\frac{u(u-1)(u-2)}{3!}\\Delta^{3}{f(a)} + \\frac{u(u-1)(u-2)(u-3)}{4!} \\Delta^{4} f(a) + ......$'
            text1 = '$=%.2f + \\frac{%.2f}{1!}(%.2f)+\\frac{%.2f(%.2f-1)}{2!}(%.2f)+\\frac{%.2f(%.2f-1)(%.2f-2)}{3!}(%.2f)+\\frac{%.2f(%.2f-1)(%.2f-2)(%.2f-3)}{4!}(%.2f)$'%(fa, u, array[0], u, u, array[1], u, u, u, array[2], u, u, u, u, array[3])
        else:
            formula = '$f(a + hu) = f(a) + \\frac{u}{1!} \\nabla f(a)+\\frac{u(u+1)}{2!}{\\nabla^{2}}{f(a)}+\\frac{u(u+1)(u+2)}{3!}\\nabla^{3}{f(a)} + \\frac{u(u+1)(u+2)(u+3)}{4!} \\nabla^{4} f(a) + ......$'
            text1 = '$=%.2f + \\frac{%.2f}{1!}(%.2f)+\\frac{%.2f(%.2f+1)}{2!}(%.2f)+\\frac{%.2f(%.2f+1)(%.2f+2)}{3!}(%.2f)+\\frac{%.2f(%.2f+1)(%.2f+2)(%.2f+3)}{4!}(%.2f)$'%(fa, u, array[0], u, u, array[1], u, u, u, array[2], u, u, u, u, array[3])
        text2 = '$=%.2f + \\frac{%.2f}{1}(%.2f)+\\frac{%.2f}{2}(%.2f)+\\frac{%.2f}{6}(%.2f)+\\frac{%.2f}{120}(%.2f)$'%(fa, u, array[0], arr2[1], array[1], arr2[2], array[2], arr2[3], array[3])
        text3 = '$=%.2f + %.2f + %.2f + %.2f + %.2f$'%(fa, arr1[0], arr1[1], arr1[2], arr1[3])
        text4 = '$f(%.2f)=%.2f$'%(new, tot + fa)
        self.ax.text(0.01, 0.9, formula, fontsize = 13)
        self.ax.text(0.09, 0.75, text1, fontsize = 13)
        self.ax.text(0.09, 0.6, text2, fontsize = 13)
        self.ax.text(0.09, 0.45, text3, fontsize = 13)
        self.ax.text(0.01, 0.3, text4, fontsize = 13)
        self.canvas.draw()
    @staticmethod
    def u_term(u, n):
        res = 1
        for k in range(n + 1):
            res *= (u - k)
        return res
    @staticmethod
    def u_term1(u, n):
        res = 1
        for k in range(n + 1):
            res *= (u + k)
        return res
    @staticmethod
    def fact(n):
        res = 1
        for j in range(n, 1, -1):
            res *= j
        return res
    def roots(self, *args):
        self.mechanism()
        lis = [float(j) for j in self.entry.get().split(',')]
        sols = roots(lis)
        with open('some.txt', 'w') as file:
            file.write(sols.__repr__())
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind)
        some.insert('insert', sols.__repr__())
        some.pack()
        n_wind.bind('destroy', self.clr)
    def eigen_vals(self, *args):
        self.mechanism()
        data = self.entry.get()
        m_lis = data.split(';')
        n_lis = []
        for j in m_lis:
            temp = [int(x) for x in j.split(',')]
            n_lis.append(temp)
        arr = array(n_lis)
        eigvals = linalg.eig(arr)
        with open('some.txt', 'w') as file:
            file.write(eigvals.__repr__())
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind)
        some.insert('insert', eigvals.__repr__())
        some.pack()
        n_wind.bind('destroy', self.clr)
        n_wind.mainloop()
    def straight_line(self, *args):
        self.mechanism()
        # CURVE FITTING STRAIGHT LINE
        text = self.entry.get().split(';')
        x = [float(j) for j in text[0].split(',')]
        y = [float(j) for j in text[1].split(',')]
        n = int(text[2])
        df = pd.DataFrame(columns = ['x', 'y', 'xy', 'x^2'])
        for j,k in zip(x, y):
            series = pd.Series([j,k,j*k,j**2], index = ['x', 'y', 'xy', 'x^2'])
            df = df.append(series, ignore_index = True)
        sx = df['x'].sum()
        sy = df['y'].sum()
        sxy = df['xy'].sum()
        sx2 = df['x^2'].sum()
        sols = linalg.solve([[sx,n], [sx2, sx]], [sy, sxy])
        gvalues = {j:round(sols[0]*j+sols[1], 4) for j in x}
        for x in gvalues:
            print(f'{x}:{round(gvalues[x])}')
        wind = Toplevel()
        with open('line.txt', 'w') as file:
            file.write(df.__repr__())
            file.write('\nsx:{}\t\tsy:{}\t\tsxy:{}\t\tsx2:{}'.format(sx, sy, sxy, sx2))
            file.write('\nA:{1}\tB:{0}'.format(round(sols[0], 4), round(sols[1], 4)))
        stext = sText.ScrolledText(wind,
                                   bg = 'black',
                                   fg = 'white',
                                   height = 15,
                                   font = ('TlwgTypist', 13, 'bold'))
        with open('line.txt', 'r') as file:
            stext.insert('insert', file.read())
        stext.pack()
        label = Label(wind)
        label.pack(fill = X)
        fig = matplotlib.figure.Figure(figsize = (20, 4), dpi = 100)
        self.ax = fig.add_subplot(111)
        self.canvas = fCt(fig, master = label)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.straight_theory(sx,sy, sxy, sx2, round(sols[0], 4), round(sols[1], 4), n)
        plt.grid(which = 'minor')
        plt.plot(gvalues.keys(), y, 'bo', gvalues.keys(), gvalues.values(), 'r--')
        plt.title('Curve Fitting into a Straight Line')
        plt.show()
        wind.mainloop()
    def straight_theory(self, sx, sy, sxy, sx2, s1, s2, n):
        text = 'Fitting of straight line by least square method.....'
        text1 = '$ y = a + bx $'
        text2 = '$ \\Sigma y = na + b\\Sigma x $'
        tn = '$ \\Sigma xy = a\\Sigma x + b\\Sigma x^2 $'
        text3 = 'Subsituting the values....'
        text4 = '{}a + {}b = {}'.format(n, sx, sy)
        text5 = '{}a + {}b = {}'.format(sx, sx2, sxy)
        text6 = 'By solving the equations....'
        text7 = 'A = {1}        B = {0}'.format(s1, s2)
        text8 = 'The equation is :  y = {1} + {0}x'.format(s1, s2)
        self.ax.text(0.1, 0.9, text)
        self.ax.text(0.1, 0.8, text1)
        self.ax.text(0.1, 0.7, text2)
        self.ax.text(0.1, 0.6, tn)
        self.ax.text(0.1, 0.5, text3)
        self.ax.text(0.1, 0.4, text4)
        self.ax.text(0.1, 0.3, text5)
        self.ax.text(0.1, 0.2, text6)
        self.ax.text(0.1, 0.1, text7)
        self.ax.text(0.1, 0.01, text8)
        self.canvas.draw()
    def parabola(self, *args):
        self.mechanism()
        # CURVE FITTING PARABOLA
        text = self.entry.get().split(';')
        x = [float(j) for j in text[0].split(',')]
        y = [float(k) for k in text[1].split(',')]
        n = int(text[-1])
        x2 = [j ** 2 for j in x]
        x3 = [j ** 3 for j in x]
        xy = [j * k for j,k in zip(x, y)]
        x4 = [j ** 4 for j in x]
        x2y = [j * k for j,k in zip(x2, y)]
        dt = pd.DataFrame([x,y,x2,x3,xy,x4,x2y])
        dt = dt.T
        dt.columns = ['x', 'y', 'x2', 'x3', 'xy', 'x4', 'x2y']
        print(dt)
        sx = round(dt['x'].sum(), 4)
        sy = round(dt['y'].sum(), 4)
        sx2 = round(dt['x2'].sum(), 4)
        sx3 = round(dt['x3'].sum(), 4)
        sxy = round(dt['xy'].sum(), 4)
        sx4 = round(dt['x4'].sum(), 4)
        sx2y = round(dt['x2y'].sum(), 4)
        print(sx, sy, sx2, sx3, sxy, sx4, sx2y)
        arr1 = array([[sx2, sx, n], [sx3, sx2, sx], [sx4, sx3, sx2]])
        arr2 = array([sy, sxy, sx2y])
        soles = linalg.solve(arr1, arr2)
        print('a:{}\nb:{}\nc:{}'.format(soles[0], soles[1], soles[2]))
        with open('some.txt', 'w') as file:
            file.write(dt.__repr__() + '\n')
            file.write('sx:{}\t\tsy:{}\t\tsx2{}\t\tsx3:{}\t\tsxy:{}\t\tsx4:{}\t\tsx2y:{}\n'.format(sx,sy,sx2,sx3,sxy,sx4,sx2y))
            file.write('a:{}\nb:{}\nc:{}'.format(round(soles[0], 4), round(soles[1], 4), round(soles[2], 4)))
        gvalues = {j:round(soles[0] * (j**2) + (soles[1] * j) + soles[2], 4) for j in x}
        print(gvalues)
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind,
                                  font = ('TlwgTypist', 12, 'bold'),
                                  bg = 'black',
                                  fg = 'white',
                                  height = 15)
        with open('some.txt', 'r') as file:
            some.insert('insert', file.read())
        some.pack()
        label = Label(n_wind)
        label.pack(fill = X)
        fig = matplotlib.figure.Figure(figsize = (20, 4), dpi = 100)
        self.ax = fig.add_subplot(111)
        self.canvas = fCt(fig, master = label)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.parabola_theory(sx, sy, sxy, sx2, sx2y, sx3, sx4, round(soles[0], 4), round(soles[1], 4), round(soles[2], 4), n)
        plt.grid()
        plt.plot(gvalues.keys(), y, 'bo', gvalues.keys(), gvalues.values(), 'r--')
        plt.title('Curve Fitting into a Parabola')
        plt.show()
        plt.plot(gvalues.keys(), gvalues.values(), 'ro', gvalues.keys(), gvalues.values(), 'b--')
        plt.title('Curve Fitting into a Parabola')
        plt.grid()
        plt.show()
        n_wind.bind('destroy', self.clr)
    def parabola_theory(self, sx, sy, sxy, sx2, sx2y, sx3, sx4, s1, s2, s3, n):
        text = 'Fitting of parabola by least square method.....'
        text1 = '$ y = a + bx + c x^2 $'
        text2 = '$ \\Sigma y = na + b\\Sigma x + c\\Sigma x^2$'
        tn = '$ \\Sigma xy = a\\Sigma x + b\\Sigma x^2 + c\\Sigma x^3$'
        tn1 = '$ \\Sigma {x^2}y = a\\Sigma x^2 + b\\Sigma x^3 + c\\Sigma x^4$'
        text3 = 'Subsituting the values....'
        text4 = '{}a + {}b + {}c = {}'.format(n, sx, sx2, sy)
        text5 = '{}a + {}b + {}c = {}'.format(sx, sx2, sx3, sxy)
        text51 = '{}a + {}b + {}c = {}'.format(sx2, sx3, sx4, sx2y)
        text6 = 'By solving the equations....'
        text7 = 'A = {2}        B = {1}      C = {0}'.format(s1, s2, s3)
        text8 = 'The equation is :  y = {2} + {1}x + {0}x^2'.format(s1, s2, s3)
        self.ax.text(0.1, 0.9, text)
        self.ax.text(0.1, 0.8, text1)
        self.ax.text(0.1, 0.7, text2)
        self.ax.text(0.1, 0.6, tn)
        self.ax.text(0.1, 0.5, tn1)
        self.ax.text(0.1, 0.4, text3)
        self.ax.text(0.1, 0.3, text4)
        self.ax.text(0.1, 0.2, text5)
        self.ax.text(0.1, 0.1, text51)
        self.ax.text(0.5, 0.9, text6)
        self.ax.text(0.5, 0.8, text7)
        self.ax.text(0.5, 0.7, text8)
        self.canvas.draw()
    def inverse(self, *args):
        self.mechanism()
        data = self.entry.get().split(';')
        new = []
        for k in data:
            temp = [float(j) for j in k.split(',')]
            new.append(temp)
        arr = array(new)
        with open('some.txt', 'w') as file:
            file.write(linalg.inv(arr).__repr__())
        n_wind = Toplevel()
        some = sText.ScrolledText(n_wind)
        some.insert('insert', linalg.inv(arr).__repr__())
        some.pack()
        plt.plot(gvalues.keys(), gvalues.values(), 'ro', gvalues.keys(), gvalues.values(), 'b--')
        plt.title('Curve Fitting into a Parabola')
        plt.grid()
        plt.show()
        n_wind.bind('destroy', self.clr)
    def runge_kutta(self, *args):
        self.mechanism()
        # Runge Kutta Method
        string = ''
        f, x0, y0, h, x = self.entry.get().split(';')
        f = f.replace('^', '**')
        f = f.replace('rad', 'radians')
        h = float(round(eval(h), 3))
        x0 = float(round(eval(x0), 3))
        y0 = float(round(eval(y0), 3))
        x = float(round(eval(x), 3))
        count = 0
        while x0 != x:
            k1 = f"{h} * ({f})"
            k2 = f"{h} * ({f})"
            k3 = f"{h} * ({f})"
            k4 = f"{h} * ({f})"
            k1 = k1.replace('x', str(x0))
            k1 = k1.replace('y', str(y0))
            k1 = round(eval(k1),4)
            k2 = k2.replace('x', str(x0 + (h / 2)))
            k2 = k2.replace('y', str(y0 + (k1 / 2)))
            k2 = round(eval(k2), 4)
            k3 = k3.replace('x', str(x0 + (h / 2)))
            k3 = k3.replace('y', str(y0 + (k2 / 2)))
            k3 = round(eval(k3), 4)
            k4 = k4.replace('x', str(x0 + h))
            k4 = k4.replace('y', str(y0 + k3))
            k4 = round(eval(k4), 4)
            y0 = f'{y0} + ((1/6)*({k1} + (2 * {k2}) + (2 * {k3}) + ({k4})))'
            x0 = f'{x0} + {h}'
            y0 = round(eval(y0), 4)
            x0 = round(eval(x0), 4)
            print('k1:', k1)
            print('k2:', k2)
            print('k3:', k3)
            print('k4:', k4)
            print(f'x{count}:', x0)
            print(f'y{count}:', y0)
            count += 1;
            print("-"*100)
            string += f'k1:{k1}\nk2:{k2}\nk3:{k3}\nk4:{k4}\nx{count}:{x0}\ny{count}:{y0}\n{"-"*80}\n'
        with open('some.txt', 'w') as file:
            file.write(string)
        x = Toplevel()
        s_text = sText.ScrolledText(x,
                                    bg = 'black',
                                    fg = 'white',
                                    font = ('TlwgTypist', 12, 'bold'))
        s_text.insert('insert', string)
        s_text.pack()
        x.mainloop()
    def numerical_integration(self, *args):
        self.mechanism()
        # NUMERICAL INTERGRATION
        f, a, b, n = self.entry.get().split(';')
        f = f.replace('^', '**')
        f = f.replace('rad', 'radians')
        self.b = b = float(round(eval(b), 3))
        self.a1 = a = float(round(eval(a), 3))
        n = int(n)
        self.h = round((b - a)/n, 5)
        string = ""
        if ('sin' in f) or ('cos' in f) or ('tan' in f):
            f.replace('x', 'x*(pi/180)')
        self.df = pd.DataFrame()
        self.df['x'] = around(linspace(a, b, n + 1), 5)
        self.df['y'] = around(eval(f.replace('x', "self.df['x']")), 5)
        self.s1 = sum(self.df['y'][1:-1])
        self.a = array(self.df['y'])
        self.s2 = (self.df['y'][0] + self.a[-1]) / 2
        self.total = self.h * (self.s1 + self.s2)
        print(self.df)
        print('Total', self.total)
        self.s2 *= 2
        self.simp1 = 4 * sum(self.df['y'][1:-1][self.df.index[1:-1] % 2 != 0])
        self.simp2 = 2 * sum(self.df['y'][1:-1][self.df.index[1:-1] % 2 == 0])
        print(self.simp1)
        print(self.simp2)
        self.total1 = (self.h / 3) * (self.simp1 + self.simp2 + self.s2)
        print('Total', self.total1)
        self.simp31 = 3 * sum(self.df['y'][1:-1][self.df.index[1:-1] % 3 != 0])
        self.simp32 = 2 * sum(self.df['y'][1:-1][self.df.index[1:-1] % 3 == 0])
        self.total2 = ((3 * self.h) / 8) * (self.simp31 + self.simp32 + self.s2)
        print('Total', self.total2)
        string += f'Numerical Integration:\n{self.df}\nTrapezoidal rule:{self.total}\nSimpsons 1/3 rule:{self.total1}\nSimpsons 3/8 rule:{self.total2}'
        with open('some.txt', 'w') as file:
            file.write(string)
        new = Toplevel()
        new.title = 'Numerical Integration'
        label = Label(new)
        label.pack(fill = X)
        fig = matplotlib.figure.Figure(figsize = (20, 4), dpi = 100)
        self.ax = fig.add_subplot(111)
        self.canvas = fCt(fig, master = label)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        frame = Frame(new)
        frame.pack()
        b1 = Button(frame,
                    text = 'Trapezoidal Rule',
                    command = lambda :self.graph(f))
        b1.pack(side = LEFT)
        b2 = Button(frame,
                    text = 'Simpson\'s 1/3 Rule',
                    command = lambda :self.graph1(f))
        b2.pack(side = LEFT)
        b3 = Button(frame,
                    text = 'Simpson\'s 3/8 Rule',
                    command = lambda :self.graph2(f))
        b3.pack(side = LEFT)
        widget = sText.ScrolledText(new,
                                    bg = 'black',
                                    fg = 'white',
                                    font = ('TlwgTypist', 12, 'bold'))
        widget.pack()
        widget.insert('insert', string)
        self.graph(f)
        new.mainloop()
    def graph(self, f):
        tmptext = pytexit.py2tex(f)
        sec = '$ \int^{%.2f}_{%.2f}'%(self.b, self.a1) + tmptext[2:-2] + ' = h( \\frac{ y_0 + y_n }{2} + y_1 + y_2 + y_3 + .... + y_{n - 1})$'
        print(sec)
        arr = array2string(around(self.a[1:-1], 3), separator = '+')[1:-1]
        sec1 = '$ = %.2f( \\frac{ %.2f + %.2f }{2} + '%(self.h, self.df['y'][0], self.a[-1]) + arr + ')$'
        sec2 = '$ = %.2f(%.3f + %.2f)$'%(self.h, self.s2/2, self.s1)
        print(self.s2)
        sec3 = '$ \int^{%.2f}_{%.2f}'%(self.b, self.a1) + tmptext[2:-2] + ' = %.4f$'%(self.total)
        self.ax.clear()
        self.ax.text(0.1, 0.9, 'Trapezoidal Rule:', fontsize = 13)
        self.ax.text(0.1, 0.73, sec, fontsize = 13)
        self.ax.text(0.168, 0.57, sec1, fontsize = 13)
        self.ax.text(0.168, 0.42, sec2, fontsize = 13)
        self.ax.text(0.1, 0.27, sec3, fontsize = 13)
        self.canvas.draw()
    def graph1(self, f):
        tmptext = pytexit.py2tex(f)
        str2 = array2string(around(self.a[1:-1][self.df.index[1:-1] % 2 != 0], 3), separator = '+')[1:-1]
        str3 = array2string(around(self.a[1:-1][self.df.index[1:-1] % 2 == 0], 3), separator = '+')[1:-1]
        sec = '$ \int^{%.2f}_{%.2f}'%(self.b, self.a1) + tmptext[2:-2] + ' = \\frac{h}{3}(y_0 + y_n + 4(y_1 + y_3 + ....) + 2(y_2 + y_4 + ....))$'
        sec1 = '$ = \\frac{%.2f}{3}(%.2f + %.2f + '%(self.h, self.a[0], self.a[-1]) + ' 4(' + str2 + ') + 2( ' + str3 + ' ))$'
        sec2 = '$ = %.2f(%.2f + %.2f + %.2f)$'%(self.h / 3, self.s2, self.simp1, self.simp2)
        sec3 = '$ \int^{%.2f}_{%.2f}'%(self.b, self.a1) + tmptext[2:-2] + ' = %.4f$'%(self.total1)
        self.ax.clear()
        self.ax.text(0.1, 0.9, 'Simpson\'s 1/3rd Rule:', fontsize = 13)
        self.ax.text(0.1, 0.75, sec, fontsize = 13)
        self.ax.text(0.168, 0.6, sec1, fontsize = 13)
        self.ax.text(0.168, 0.45, sec2, fontsize = 13)
        self.ax.text(0.1, 0.3, sec3, fontsize = 13)
        self.canvas.draw()

    def graph2(self, f):
        tmptext = pytexit.py2tex(f)
        str3 = array2string(around(self.a[1:-1][self.df.index[1:-1] % 3 != 0], 3), separator = '+')[1:-1]
        str2 = array2string(around(self.a[1:-1][self.df.index[1:-1] % 3 == 0], 3), separator = '+')[1:-1]
        sec = '$ \int^{%.2f}_{%.2f}'%(self.b, self.a1) + tmptext[2:-2] + ' = \\frac{3h}{8}(y_0 + y_n + 3(y_1 + y_2 + y_4 + ...) + 2(y_3 + y_6 + ...))$'
        sec1 = '$ = %.3f(%.2f + %.2f + '%((3 * self.h)/8, self.a[0], self.a[-1]) + ' 3(' + str3 + ') + 2(' + str2 + '))$'
        sec2 = '$ = %.3f(%.3f + %.3f + %.3f)$'%((3 * self.h)/8, self.s2, self.simp31, self.simp32)
        sec3 = '$ \int^{%.2f}_{%.2f}'%(self.b, self.a1) + tmptext[2:-2] + ' = %.4f$'%(self.total2)
        self.ax.clear()
        self.ax.text(0.1, 0.9, 'Simpson\'s 3/8 Rule:', fontsize = 13)
        self.ax.text(0.1, 0.75, sec, fontsize = 13)
        self.ax.text(0.168, 0.6, sec1, fontsize = 13)
        self.ax.text(0.168, 0.45, sec2, fontsize = 13)
        self.ax.text(0.1, 0.3, sec3, fontsize = 13)
        self.canvas.draw()
    def newton_raphson(self, *args):
        self.mechanism()
        # NEWTON RAPHSON
        count = 0
        string = ''
        f, f1, x0 = self.entry.get().split(';')
        f = f.replace('^', '**')
        f1 = f1.replace('^', '**')
        f = f.replace('rad', 'radians')
        f1 = f1.replace('rad', 'radians')
        x0 = float(eval(x0))
        y0 = round(eval(f.replace('x', str(x0))), 4)
        y10 = round(eval(f1.replace('x', str(x0))), 4)
        columns = ['Iteration', 'x', 'f(x)',  'root']
        df = pd.DataFrame(columns = columns)
        while count < 12:
            x = round(x0 - (y0 / y10), 6)
            y0 = round(eval(f.replace('x', str(x))), 4)
            y10 = round(eval(f1.replace('x', str(x))), 4)
            new_sers = pd.Series([count, x0, y0, x], index = columns)
            df = df.append(new_sers, ignore_index = True)
            count += 1
            x0 = x
        string = df.__repr__()
        with open('some.txt', 'w') as file:
            file.write(string)
        new = Toplevel()
        widget = sText.ScrolledText(new,
                                    bg = 'black',
                                    fg = 'white',
                                    font = ('TlwgTypist', 12, 'bold'))
        widget.pack()
        widget.insert('insert', string + '\n\nROOT:' + str(list(df['root'])[-1]))
        new.mainloop()
    def undo(self, *args):
        self.entry.delete(0, END)
        if self.l_no == 0:
            self.l_no = len(self.stack)
        self.l_no -= 1
        try:
            self.entry.insert(END, self.stack[self.l_no])
        except IndexError:
            self.l_no = len(self.stack)
    def redo(self, *args):
        self.entry.delete(0, END)
        if self.stack == len(self.stack):
            self.l_no = 0
        self.l_no += 1
        try:
            self.entry.insert(END, self.stack[self.l_no])
        except IndexError:
            self.l_no = 0

    def truth_tables(self, *args):
        inp = self.entry.get().split(';')
        expr1 = expr = inp[0].lower()
        l = int(inp[1])
        l1 = 2 ** l
        cols = ['p', 'q', 'r', 'b', 'x']
        df = pd.DataFrame(columns = cols[:l])
        pre_var = 1
        for i in range(l):
            array = zeros(l1)
            array = array.astype(int8)
            for j in range(2 ** i):
        ##        print('PreVar:', pre_var)
        ##        print('J', j)
        ##        print(f"{int(j * (l1/pre_var))}:{int((l1/(2**(i+1)))*(2 * j + 1))}")
                array[int(j * (l1/pre_var)):int((l1/(2**(i+1)))*(2 * j + 1))] = 1
            pre_var = (2 ** (i + 1))
            df[cols[i]] = array
        expr = expr.replace('p', "cs.Statement(df['p'])")
        expr = expr.replace('q', "cs.Statement(df['q'])")
        expr = expr.replace('T', "cs.Statement.T(l1)")
        expr = expr.replace('F', "cs.Statement.F(l1)")
        expr = expr.replace('r', "cs.Statement(df['r'])")
        expr = expr.replace('b', "cs.Statement(df['b'])")
        expr = expr.replace('x', "cs.Statement(df['x'])")
        print(expr)
        df[expr1] = eval(expr).get_np()
        print(df)
        new = Toplevel()
        box = sText.ScrolledText(new,
                    bg = 'black',
                    fg = 'white',
                    font = ('TlwgTypist', 12, 'bold'))
        box.insert('insert', 'Truth Table'.center(60, '*'))
        box.insert('insert', '\n' + df.__repr__())
        if df[expr1].all():
            print("The expression is a tautology.")
            box.insert('insert', '\nThe expression is a tautology.')
        elif not df[expr1].all() and not df[expr1].any():
            print("The expression is a contradiction.")
            box.insert('insert', '\nThe expression is a contradiction.')
        else:
            print("The expression is a contingency.")
            box.insert('insert', '\nThe expression is a contingency.')
        box.pack()
        new.mainloop()
obj = XanderCalculator()
