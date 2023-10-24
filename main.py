import tkinter as tk
from PIL import Image, ImageTk
import time
import subprocess


def open_program():
    root = tk.Tk()
    root.title("Break from PC")
    root.iconbitmap(r'C:\coffee.ico')
    root.attributes('-fullscreen', True)

    my_img = ImageTk.PhotoImage(Image.open(r'C:\img21.jpg'))

    my_label = tk.Label(image=my_img)
    my_label.pack()

    # Set the size of the window (width x height)
    root.geometry("800x600")  # Change the values as needed

    button_quit = tk.Button(root, text="Quit", command=root.quit)
    button_quit.pack()

    root.mainloop()


# Initial run
open_program()

# Schedule to run the program every hour (3600 seconds)
while True:
    time.sleep(3600)  # Sleep for an hour
    open_program()
