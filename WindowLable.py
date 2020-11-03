from tkinter import*

window = Tk()

label1=Label(window,text="Cookbook~~Python을")
label2=Label(window,text="열심히",font=("궁서",30),fg="blue")
label3=Label(window,text="공부 중입니다",bg="megenta",width=20,height=5,anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop() 