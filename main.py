import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

# Global Variables
bgColor = "black"  # background color
fgColor = "white"  # foreground color


class SlideshowApp:
    def __init__(self, image_files):
        self.root = tk.Tk()
        self.root.title("Time for sport")
        self.root.iconbitmap(r'C:\coffee.ico')  # icon of the application

        self.root.configure(bg=bgColor)
        label = tk.Label(self.root, text="Welcome to your first Training", font=('Arial', 16), bg=bgColor, fg=fgColor)
        label.pack(padx=22)
        self.image_files = image_files
        self.slide_label = tk.Label(self.root, bg=bgColor)
        self.slide_label.pack()

        self.image_index = 0
        self.slide_timer = 20  # seconds for each slide
        self.total_timer = len(image_files) * self.slide_timer  # total time for slideshow
        self.root.geometry("800x600")  # Change the values as needed
        # show the slides
        self.show_slide()
        self.update_timers()
        # quit button

        # ShutDown Button
        image_path = "images\\shutdown.png"
        image = Image.open(image_path)
        resize_image = image.resize((60, 60))
        photo = ImageTk.PhotoImage(resize_image)
        button = tk.Button(self.root, image=photo, command=self.root.quit, bg=bgColor, highlightthickness=0, bd=0)
        button.photo = photo
        button.pack(side=tk.BOTTOM)  # display the button

    def show_slide(self):
        image = Image.open(self.image_files[self.image_index])
        photo = ImageTk.PhotoImage(image)
        self.slide_label.config(image=photo)
        self.slide_label.image = photo  # keep a reference!

        self.image_index = (self.image_index + 1) % len(self.image_files)
        self.root.after(self.slide_timer * 1000, self.show_slide)

    def update_timers(self):
        # Here you can update your timers, currently, it just prints the countdown
        text1 = f"Time remaining for this slide: {self.slide_timer} seconds"
        text2 = f"Total slideshow time remaining: {self.total_timer} seconds"
        print(text1)
        print(text2)
        label = tk.Label(self.root, text=text1, font=('Arial', 16))
        label.pack()
        # tk.Label(text2)
        '''
        The next code is counting each slide count down, once it reach zero the count down is reset to its first value.
        if both total timer and slide timer are 0 then the program shuts down.
        
        '''
        self.total_timer -= 1
        self.slide_timer -= 1
        if self.total_timer <= 0 and self.slide_timer <= 0:
            self.end()  # Shut down the program when both timers reach 0
        else:
            self.root.after(1000, self.update_timers)  # Schedule the next update
        if self.slide_timer <= 0:
            self.slide_timer = 20  # Reset slide timer to 20 when it reaches 0 or below


    def start(self):
        self.root.mainloop()

    def end(self):
        self.root.quit()


def run_slideshow():
    # List of image paths
    images = ["images\\IMG1.PNG", "images\\IMG2.PNG", "images\\IMG3.PNG"]
    app = SlideshowApp(images)
    app.start()


# Run the slideshow in a separate thread
threading.Thread(target=run_slideshow).start()

# Main loop that triggers the slideshow every hour
while True:
    time.sleep(3)  # Wait for 1 hour
    run_slideshow()
