from tkinter import Tk ,IntVar ,Entry ,Label ,Radiobutton ,W ,Button ,END
import emoji

class class_storage:
    def __init__(self):
        self.num = None
        self.data = []

def reset():
    output.pack_forget()
    btn3.pack_forget()
    label2.pack(anchor=W)
    radio1.pack(anchor=W)
    radio2.pack(anchor=W)
    btn0.pack()

    storage.data = []
    storage.num = None

def process():
    radio1.pack_forget()
    radio2.pack_forget()
    btn0.pack_forget()
    label2.pack_forget()
    output.pack()

    if mode.get() == 1:
        auto_mode()
    else:
        manual_mode()

def auto_mode():
    result = ''
    sentense = sentense_input.get()
    words = sentense.split()

    for i in words:
        test = emoji.emojize(':' + i + ':')
        if test[0] == ':':
            result = result + i + ' '
        else:
            result = result + test + ' '

    output.delete(0,END)
    output.insert(0,result)
    btn3.pack()

def manual_mode():
    result = []
    sentense = sentense_input.get()
    words = sentense.split()

    for i in words:
        test = emoji.emojize(':' + i + ':')
        if test[0] == ':':
            result.append(i)
        else:
            result.append([i,test])

    storage.data = result
    storage.num = 0
    btn1.pack()
    btn2.pack()
    continue_assignment()

def change():
    storage.data[storage.num-1] = storage.data[storage.num-1][1]
    continue_assignment()

def dont_change():
    storage.data[storage.num-1] = storage.data[storage.num-1][0]
    continue_assignment()

def continue_assignment():
    if storage.num >= len(storage.data):
            output.delete(0,END)

            for word in storage.data[::-1]:
                output.insert(0,word + ' ')
            btn1.pack_forget()
            btn2.pack_forget()
            btn3.pack()

    else:
        while type(storage.data[storage.num])!=list:
            storage.num += 1
            if storage.num >= len(storage.data):
                continue_assignment()
                break
            
        else:
            output.delete(0,END)
            data = storage.data[storage.num]
            output.insert(0,str(data[0]) + " -> " + str(data[1]))
            storage.num += 1

storage = class_storage()
Window = Tk()
Window.title("Emojify")

sentense_input = Entry(width=50)
sentense_input.pack()

output = Entry(width=50)

label2 = Label(Window,text="\nSelect any mode of operation:", padx = 42, font="none 9 bold")
label2.pack()

mode = IntVar()
mode.set(1)
radio1 = Radiobutton(Window,text="Auto mode",padx = 20,variable=mode,value=1)
radio2 = Radiobutton(Window,text="Manual mode",padx = 20,variable=mode,value=2)
radio1.pack(anchor=W)
radio2.pack(anchor=W)

btn0 = Button(master=Window,text="Select",command=process)
btn1 = Button(master=Window,text="Yes",command=change)
btn2 = Button(master=Window,text="No",command=dont_change)
btn3 = Button(master=Window, width=8,text="Reset",command=reset)
btn0.pack()

Window.mainloop()

# Test sentence
# boy and girl were going to school
#
# expected output
# 👦 👧 were going to 🏫