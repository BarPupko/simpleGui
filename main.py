from tkinter import *
from PIL import ImageTK,Image

root = Tk()
root.title("Break from PC")
root.iconbitmap('C:\coffee.ico')


button_quit = Button(root,text="Quit",command=root.quit)
button_quit.pack()
def myClick():
    myLabel = Label(root,text="Look I clicked the button")
    myLabel.pack()
# creating a label widget
# myLabel1 = Label(root, text="hello world").grid(row=0,column=1)
# myLabel2 = Label(root, text="my name is bar").grid(row=1,column=1)

myButton = Button(root,text="Click me",command=myClick,fg="red")
myButton.pack()
# shoving it onto the screen


# will loop constantly
root.mainloop()
