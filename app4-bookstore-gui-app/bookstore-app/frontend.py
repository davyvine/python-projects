#
# A program that stores this book information:
# Title, Author
# Year, ISBN

# User can:
# View all records
# Search an entry
# Add an entry
# Update an entry
# Delete an entry
# Close Program

# Note: make a sketch with a grid to visualize how the GUI will look like
#

from tkinter import *
import backend

window = Tk()

# title of te window
window.wm_title("Bookstore")

# wrapper functions


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass  # means do nothing


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)  # empty the display list
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                       year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())


# Create 4 label objects
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Create 4 input box
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Create list box - to display data
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# bind the selected item in the list
# <<>> is the event
list1.bind('<<ListboxSelect>>', get_selected_row)

# Create 6 buttons
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b1 = Button(window, text="Search entry", width=12, command=search_command)
b1.grid(row=3, column=3)

b1 = Button(window, text="Add entry", width=12, command=add_command)
b1.grid(row=4, column=3)

b1 = Button(window, text="Update", width=12, command=update_command)
b1.grid(row=5, column=3)

b1 = Button(window, text="Delete", width=12, command=delete_command)
b1.grid(row=6, column=3)

b1 = Button(window, text="Close", width=12, command=window.destroy)
b1.grid(row=7, column=3)

window.mainloop()
