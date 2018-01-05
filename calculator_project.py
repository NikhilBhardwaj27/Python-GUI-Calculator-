from tkinter import *
from tkinter import ttk

class calculator():

  def __init__(self,root):

    self.root = root

    self.counter = 0

    self.val = 0

    self.p = 0

    self.root.resizable(width=False,height=False)

    self.frame = Frame(self.root,width=410,height=370,bg='gray15') #creating frame

    self.frame.propagate(0)

    self.style  =  ttk.Style()

    self.style.configure('TButton',foreground='gray15',font=('Times',-40,'bold'))

    self.style.configure('TEntry',width=50)

    self.style.theme_use('vista')

    self.Entry = ttk.Entry(self.frame,width=50,font=('Times',-40,'bold'))

    self.b1 = ttk.Button(self.frame,text='1',cursor='hand2',command=lambda:self.click('1')) #button 1

    self.b2 = ttk.Button(self.frame,text='2',cursor='hand2',command=lambda:self.click('2')) #button 2

    self.b3 = ttk.Button(self.frame,text='3',cursor='hand2',command=lambda:self.click('3')) #button 3

    self.b4 = ttk.Button(self.frame,text='4',cursor='hand2',command=lambda:self.click('4')) #button 4

    self.b5 = ttk.Button(self.frame,text='5',cursor='hand2',command=lambda:self.click('5')) #button 5

    self.b6 = ttk.Button(self.frame,text='6',cursor='hand2',command=lambda:self.click('6')) #button 6

    self.b7 = ttk.Button(self.frame,text='7',cursor='hand2',command=lambda:self.click('7')) #button 7

    self.b8 = ttk.Button(self.frame,text='8',cursor='hand2',command=lambda:self.click('8')) #button 8

    self.b9 = ttk.Button(self.frame,text='9',cursor='hand2',command=lambda:self.click('9')) #button 9

    self.b10 = ttk.Button(self.frame,text='.',cursor='hand2',command=lambda:self.click('10')) #button 10

    self.c = ttk.Button(self.frame,text='C',cursor='hand2',command=lambda:self.click('11')) #button c

    self.b0 = ttk.Button(self.frame,text='0',cursor='hand2',command=lambda:self.click('0')) #button 0

    self.plus = ttk.Button(self.frame,text='+',cursor='hand2',command=lambda:self.cal('plus')) #button +

    self.minus = ttk.Button(self.frame,text='-',cursor='hand2',command=lambda:self.cal('minus')) #button -

    self.mul = ttk.Button(self.frame,text='*',cursor='hand2',command=lambda:self.cal('mul')) #button *

    self.div = ttk.Button(self.frame,text='/',cursor='hand2',command=lambda:self.cal('div')) #button div

    self.eql = ttk.Button(self.frame,text='=',cursor='hand2',command=lambda:self.eq(self.k)) #button =

    # Packing and Layouts

    self.frame.pack()

    self.b1.place(x=10,y=65,width=90,height=50)

    self.b2.place(x=120,y=65,width=90,height=50)

    self.b3.place(x=230,y=65,width=90,height=50)

    self.b4.place(x=10,y=125,width=90,height=50)

    self.b5.place(x=120,y=125,width=90,height=50)

    self.b6.place(x=230,y=125,width=90,height=50)

    self.b7.place(x=10,y=185,width=90,height=50)

    self.b8.place(x=120,y=185,width=90,height=50)

    self.b9.place(x=230,y=185,width=90,height=50)

    self.b10.place(x=340,y=185,width=60,height=49)

    self.c.place(x=340,y=65,width=60,height=49)

    self.b0.place(x=340,y=125,width=60,height=49)

    self.Entry.place(x=10,y=5,width=390,height=50)

    self.plus.place(x=10,y=245,width=90,height=50)

    self.minus.place(x=120,y=245,width=90,height=50)

    self.mul.place(x=10,y=305,width=90,height=50)

    self.div.place(x=120,y=305,width=90,height=50)

    self.eql.place(x=230,y=250,width=170,height=100)
  # function to insert values
  def click(self,n):
    k = int(n)
    if k<=10:
      if k!=10:
        self.Entry.insert(str(self.counter),n)
      else:
        self.Entry.insert(str(self.counter),'.')
    elif k==11:
      self.Entry.delete('0','end')
      counter=0
      self.val=0
      self.p=0
    self.counter+=1
  # function to fetch entries in entry widget
  def cal(self,n):
    if n=='plus':
        self.val+=float(self.Entry.get())
        self.Entry.delete('0','end')
        self.k = 'plus'
    if n=='minus':
        self.val=float(self.Entry.get())
        self.Entry.delete('0','end')
        self.k = 'minus'
    if n=='mul':
        self.val=float(self.Entry.get())
        self.Entry.delete('0','end')
        self.k = 'mul'
    if n=='div':
        self.val=float(self.Entry.get())
        self.Entry.delete('0','end')
        self.k = 'div'
  # function for equal button
  def eq(self,n):
    if self.p==0:
        self.temp = float(self.Entry.get())
        self.p+=1
    if n=='plus':
        self.val+=self.temp
        self.Entry.delete('0','end')
        self.Entry.insert('0',self.val)

    if n=='minus':
        self.val-=self.temp
        self.Entry.delete('0','end')
        self.Entry.insert('0',self.val)

    if n=='mul':
        self.val*=self.temp
        self.Entry.delete('0','end')
        self.Entry.insert('0',self.val)

    if n=='div':
        self.val/=temp
        self.Entry.delete('0','end')
        self.Entry.insert('0',self.val)

#create root window
root = Tk()
root.title('Calculator')
root.geometry('410x370+400+100')
obj = calculator(root) #creating object
root.mainloop()
