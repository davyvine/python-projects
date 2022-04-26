# Tkinter - to build GUI - built in python lib
from tkinter import *  # import/load all Tkinter objects

# create window
window = Tk()  # will create empty window

# functions


def km_to_miles():
    # multiply the user input value by 1.6 to get miles
    miles = float(e1_value.get())*1.6

    # insert the value to the text widget
    t1.insert(END, miles)


# build/create widgets, window first followed by other params

# button widget - command option takes in a reference function (without () ) that will be executed once button is clicked
b1 = Button(window, text="Execute", command=km_to_miles)
# grid () or pack() can be used to reflect the widget in the window
# grid() have more control in the positions of your widgets
b1.grid(row=0, column=0)

# input widget
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# display text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


# allows you to close the window always at the end of the code
window.mainloop()
