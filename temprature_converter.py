'''Task 5 : Temperature converter Create a program that allows the user to convert temperatures between Fahrenheit and Celsius.'''


from tkinter import *
def convertval():
    com = float(valueentry.get())
    if clicked.get() == options[0]:
        Label(root, text=f"The celcious is {(com-32)*5/9}", font="lucido 30 bold").place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
       Label(root, text=f"The fehrenhit is {com*(9/5)+32}", font="lucido 30 bold").place(relx=0.5, rely=0.8, anchor=CENTER)
root = Tk()
root.geometry("1000x1000")  #455x345
root.title("Temprature converter")

can_widget = Canvas(root, height=500, width=500)

Label(can_widget, text="Temprature \nconverter", font="lucido 33 bold", pady=10).grid(row=0, column = 1, columnspan=3, pady=15)

type = Label(can_widget, text="Choose the type of conversion", font="lucido 10 bold")
type.grid(row = 1, column = 1)

value = Label(can_widget, text="Enter the value which you want \nto convert", font="lucido 10 bold")
value.grid(row=2, column=1, pady=20)

Button(can_widget, text="convert", command=convertval, font="lucido 10 bold", anchor=W).grid(row=4, column=1, columnspan=3)

options = [
    "fehrenhit to celscius", 
    "celcius to fehrenhit"]
clicked = StringVar()
clicked.set("fehrenhit to celscius")
drop = OptionMenu(can_widget, clicked, *options)
drop.grid(row = 1, column=3)
drop.config(font="lucido 10 bold")

valueVal = StringVar()
valueentry = Entry(can_widget, textvariable=valueVal, width=23, font="lucido 10 bold")
valueentry.grid(row=2, column=3)
can_widget.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()