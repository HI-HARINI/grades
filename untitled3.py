from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
root.title("Percentage")
label1=Label(root)
label1.place(relx=0.5, rely=0.2,anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5, rely=0.4,anchor=CENTER)
label3=Label(root)
label3.place(relx=0.5, rely=0.6,anchor=CENTER)

class gr3():
    def __init__(self,LA,Math,Science,Social):
        self.LA=LA
        self.Math=Math
        self.Science=Science
        self.Social=Social
    
    def percent(self):
        average=(self.LA+self.Math+self.Science+self.Social)/4
        label1["text"]=average
        
class gr5():
    def __init__(self,LA,Math,Science,Social):
        self.LA=LA
        self.Math=Math
        self.Science=Science
        self.Social=Social
    
    def percent(self):
        average=(self.LA+self.Math+self.Science+self.Social)/4
        label2["text"]=average

class gr10():
    def __init__(self,LA,Math,Science,Social):
        self.LA=LA
        self.Math=Math
        self.Science=Science
        self.Social=Social
    
    def percent(self):
        average=(self.LA+self.Math+self.Science+self.Social)/4
        label3["text"]=average
        
Peter=gr3(53,97,45,78)
button1=Button(root,text="Grade 3",command=Peter.percent)
button1.place(relx=0.5, rely=0.1,anchor=CENTER)

Alina=gr5(98,94,87,91)
button2=Button(root,text="Grade 5",command=Alina.percent)
button2.place(relx=0.5, rely=0.3,anchor=CENTER)

Zenbob=gr10(8,13,32,6)
button3=Button(root,text="Grade 10",command=Zenbob.percent)
button3.place(relx=0.5, rely=0.5,anchor=CENTER)

root.mainloop()