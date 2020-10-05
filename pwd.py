import string
from random import *
from tkinter import *

root = Tk()
root.configure(bg="Black")

letters = string.ascii_letters 
digits = string.digits 
symbols = string.punctuation
chars = letters + digits + symbols


def myClick():
    global chars
    global myLabel
    length = int (e.get())
    password = "".join(choice(chars) for x in range(length))
    myLabel.destroy()
    myLabel = Label(root, text=password, bg="#fff")
    myLabel.grid(row=3, column=1, pady=10, sticky=W+E)
    e.delete(0, 'end')
    
def end():
    root.quit()
    
    
myLabel = Label(root, pady=10, text="PASSWORD GENERATOR", fg="#fff", bg="Green", font=('Helvetica', 11, "bold"))
myLabel.grid(row=0, column=0, pady=0, columnspan=3, sticky=W+E)



e = Entry(root, width=10, font=('Helvetica', 30))
e.grid(row=1, column=0, columnspan=3, padx=0, pady=10)


myButton = Button(root, text="Generate Password", fg="#fff", bg="Green", command=myClick)
myButton.grid(row=2, column=1, pady=15)


myLabel = Label(root, text="PASSWORD", bg="#fff")
myLabel.grid(row=3, column=1, pady=10, sticky=W+E)


#endButton = Button (root, text="End Program", padx=14, pady=10, fg="#fff", bg="Red", command=end)
#endButton.grid(row=4, column=1, padx=0, pady=5)


name = Label(root, text="\n\n", bg="#000", fg = "#fff")
version = Label(root, text="version 1.0\n", bg="#000", fg="#fff")
copyright = Label(root, text="© copyright\nAll rights reserved by @hind_biswas", fg="#fff", bg="#000")


name.grid(row=5, column=0, columnspan=3)
version.grid(row=6, column=0, columnspan=3)
copyright.grid(row=7, column=0, columnspan=3)



root.mainloop()