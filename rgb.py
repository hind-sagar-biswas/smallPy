from tkinter import *

root = Tk()
root.title("HexCode Generator")


red = "00"
green = "00"
blue = "00"

x = 100
y = 100

hex = sorted(['aa', 'ba', 'ca', 'da', 'ea', 'fa', '0a', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', 'ab', 'bb', 'cb', 'db', 'eb', 'fb', '0b', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', 'ac', 'bc', 'cc', 'dc', 'ec', 'fc', '0c', '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'ad', 'bd', 'cd', 'dd', 'ed', 'fd', '0d', '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'ae', 'be', 'ce', 'de', 'ee', 'fe', '0e', '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '9e', 'af', 'bf', 'cf', 'df', 'ef', 'ff', '0f', '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f', '9f', 'a0', 'b0', 'c0', 'd0', 'e0', 'f0', '00', '10', '20', '30', '40', '50', '60', '70', '80', '90', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', '01', '11', '21', '31', '41', '51', '61', '71', '81', '91', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', '02', '12', '22', '32', '42', '52', '62', '72', '82', '92', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', '03', '13', '23', '33', '43', '53', '63', '73', '83', '93', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', '04', '14', '24', '34', '44', '54', '64', '74', '84', '94', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', '05', '15', '25', '35', '45', '55', '65', '75', '85', '95', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', '06', '16', '26', '36', '46', '56', '66', '76', '86', '96', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', '07', '17', '27', '37', '47', '57', '67', '77', '87', '97', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', '08', '18', '28', '38', '48', '58', '68', '78', '88', '98', 'a9', 'b9', 'c9', 'd9', 'e9', 'f9', '09', '19', '29', '39', '49', '59', '69', '79', '89', '99'])


final = "#" + red + green + blue

label = Label(root, padx=x, pady=y, bg = final)

def ar(r):
    global red
    global label
    global status
    red = (hex[int(r)])
    final = "#" + red + green + blue
    label.destroy()
    #status.destroy()
    label = Label(root, padx=x, pady=y, bg = final)
    label.grid(row=0, column=0, columnspan=3, sticky=W+E)
    status = Label(root, text="Hex Code:  " + final, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def ge(g):
    global green
    global label
    global status
    green=(hex[int(g)])
    final = "#" + red + green + blue
    label.destroy()
    #status.destroy()
    label = Label(root, padx=x, pady=y, bg = final)
    label.grid(row=0, column=0, columnspan=3, sticky=W+E)
    status = Label(root, text="Hex Code:  " + final, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    
def be(b):
    global blue
    global label
    global status
    blue = (hex[int(b)])
    final = "#" + red + green + blue
    label.destroy()
    #status.destroy()
    label = Label(root, padx=x, pady=y, bg = final)
    label.grid(row=0, column=0, columnspan=3, sticky=W+E)
    status = Label(root, text="Hex Code:  " + final, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

r = Scale(root, from_=0, to= 226, command=ar)
g = Scale(root, from_=0, to= 226, command=ge)
b = Scale(root, from_=0, to= 226, command=be)


label.grid(row=0, column=0, columnspan=3, sticky=W+E)
status = Label(root, text="Hex Code:  " + final, bd=1, relief=SUNKEN, anchor=E, bg="#fff")


r.grid(row=1, column = 0, padx = 40)
g.grid(row=1, column= 1, padx = 40)
b.grid(row=1, column= 2, padx = 40)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop()


'''FILE DIALOGUE BOX POPUP:
    
tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File box")

def open():
	root.filename = filedialog.askopenfilename( title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label = Label(root, text=root.filename).pack()
	
my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
'''

'''MESSAGE DIALOGUE BOX:
    
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Learn To Code at Codemy.com')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup1():
	response = messagebox.showinfo("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
	#if response == "yes":
	#	Label(root, text="You Clicked Yes!").pack()
	#else:
	#	Label(root, text="You Clicked No!!").pack()

def popup2():
	response = messagebox.showwarning("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
def popup3():
	response = messagebox.showerror("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
def popup4():
	response = messagebox.askquestion("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
def popup5():
	response = messagebox.askokcancel("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
def popup6():
	response = messagebox.askyesno("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()

Button(root, text="Info..", command=popup1).pack()
Button(root, text="Warn", command=popup2).pack()
Button(root, text="Error", command=popup3).pack()
Button(root, text="Ques", command=popup4).pack()
Button(root, text="Canc", command=popup5).pack()
Button(root, text="Yesn", command=popup6).pack()

mainloop()
'''
