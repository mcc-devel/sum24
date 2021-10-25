from tkinter import *
from main import calculate

def callback():
    res = calculate(eval('[' + inp1.get() + ']'), eval(inp2.get()))
    lbox.delete(0, END)
    for elem in res:
        lbox.insert(END, elem)

if __name__ == '__main__':
    frame = Tk()
    frame.geometry('700x600')
    ln1 = Frame(frame)
    lab1 = Label(ln1, text = 'Numbers, use a,b,c format')
    inp1 = Entry(ln1)
    ln2 = Frame(frame)
    lab2 = Label(ln2, text = 'Result')
    inp2 = Entry(ln2)
    btn = Button(frame, text = 'Calculate!', command = callback)
    lbox = Listbox(frame, selectmode = SINGLE, width = 75, height = 30)
    ln1.pack()
    lab1.pack(side = LEFT)
    inp1.pack(side = RIGHT)
    ln2.pack()
    lab2.pack(side = LEFT)
    inp2.pack(side = RIGHT)
    btn.pack()
    lbox.pack()
    frame.mainloop()