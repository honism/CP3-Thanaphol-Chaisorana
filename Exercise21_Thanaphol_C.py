from tkinter import *


def Click(event):
    new_height = float(textboxHeight.get())
    new_weight = float(textboxWeight.get())
    BMI = new_weight/((new_height/100)**2)
    if BMI > 30.0:
        result.configure(text="BMI = %f = %s"%(BMI,"อ้วนมาก"))
    elif 25.0<=BMI<=29.9:
        result.configure(text="BMI = %f = %s" % (BMI, "อ้วน"))
    elif 23.0<=BMI<=24.9:
        result.configure(text="BMI = %f = %s" % (BMI, "น้ำหนักเกิน"))
    elif 18.6<=BMI<=22.9:
        result.configure(text="BMI = %f = %s" % (BMI, "น้ำหนักเปกติ เหมาะสม"))
    else:
        result.configure(text="BMI = %f = %s" % (BMI, "ผอมเกินไป"))


window = Tk()
window.title("Body Mass Index Calculate")
Height = Label(window,text = "ส่วนสูง(cm):")
Height.grid(row=0,column=0)
textboxHeight = Entry(window)
textboxHeight.grid(row=0,column=1)


Weight = Label(window,text = "น้ำหนัก(Kg):")
Weight.grid(row=1,column=0)
textboxWeight = Entry(window)
textboxWeight.grid(row=1,column=1)


calculatebutton = Button(window,text="Calculate")
calculatebutton.bind("<Button-1>",Click)
calculatebutton.grid(column=0)


result = Label(window,text="ผลลัพธ์")
result.grid(row=2,column=1)


window.mainloop()

