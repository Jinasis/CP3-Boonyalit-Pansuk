from tkinter import *

def leftClickButton(event):
    result = float(textBoxWeight.get()) / (float(textBoxHight.get()) / 100) ** 2
    print(float(textBoxWeight.get())/(float(textBoxHight.get())/100)**2)
    if result >= 30:
        labelResult.configure(text="อ้วนมาก")
    elif result >= 25:
        labelResult.configure(text="อ้วน")
    elif result >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif result >= 18.6:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text="ผอมเกินไป")
#    labelResult.configure(text=float(textBoxWeight.get())/(float(textBoxHight.get())/100)**2)

MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง (ซม.)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (กก.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculatorButton = Button(MainWindow,text="คำนวณ")
calculatorButton.grid(row=2)
calculatorButton.bind('<Button-1>',leftClickButton)
labelResult = Label(MainWindow,text="ค่า BMI")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()