from tkinter import *

root = Tk() #create an object that is a blank window

topFrame = Frame(root) #make invisible container and put it in the main window (root)
topFrame.pack() #place somewhere in main window
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="white")
button3 = Button(topFrame, text="Button 3", fg = "green")
button4 = Button(bottomFrame, text = "Button 4", fg = "purple")

#display button on screen
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

one = Label(root, text="One", bg = "red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

label_1= Label(root, text="Name")
label_2= Label(root, text="Password")
label_3= Label(root, text="Name")

root.mainloop() #put in inifinite loop so it never ends. Window will continue to display until you close it.








