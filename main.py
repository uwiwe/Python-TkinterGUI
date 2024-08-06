from tkinter import *


def convert():
    miles = float(miles_input.get())
    result = miles * 1.609344
    label_4.config(text=result)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=60, pady=30)

# Label
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)
label_2 = Label(text="is equal to:")
label_2.grid(column=0, row=1)
label_3 = Label(text="Km")
label_3.grid(column=2, row=1)
label_4 = Label(text="")
label_4.grid(column=1, row=1)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
