from tkinter import *

window = Tk()

# functions


def from_kg():
    # get user input value and multiply by 1000 to get the gram
    gram = float(e2_value.get()) * 1000

    # get user input value and multiply by 2.20462 to get pound
    pound = float(e2_value.get())*2.20462

    # get user input value and multiply by 35.274 to get ounce
    ounce = float(e2_value.get())*35.274

    # Empty the Text boxes if they had text from the previous use and fill them again
    # Deletes the content of the Text box from start to END
    t1.delete("1.0", END)
    # Fill in the text box with the value of gram variable
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)


# create widget
# Label widget
e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)  # label is placed in position 0

# Input widget
e2_value = StringVar()  # get the input value and store in e2_value variable
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# button widget
b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=0, column=2)

# 3 text display widget
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
