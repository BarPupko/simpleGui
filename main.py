import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

class SlideshowApp:

    def __init__(self, image_files):
        self.root = tk.Tk()
        self.root.iconbitmap(r'C:\coffee.ico')

        self.root.title("Slideshow")

        self.image_files = image_files
        self.slide_label = tk.Label(self.root)
        self.slide_label.pack()
        self.root.geometry("880x600"); #screen size
        self.image_index = 0
        self.slide_timer = 20  # seconds for each slide
        self.total_timer = len(image_files) * self.slide_timer  # total time for slideshow

        self.show_slide()
        self.update_timers()

    def show_slide(self):
        image = Image.open(self.image_files[self.image_index])
        photo = ImageTk.PhotoImage(image)
        self.slide_label.config(image=photo)
        self.slide_label.image = photo  # keep a reference!

        self.image_index = (self.image_index + 1) % len(self.image_files)
        self.root.after(self.slide_timer * 1000, self.show_slide)

    def update_timers(self):
        # Here you can update your timers, currently, it just prints the countdown
        print(f"Time remaining for this slide: {self.slide_timer} seconds")
        print(f"Total slideshow time remaining: {self.total_timer} seconds")
        self.total_timer -= 1
        self.root.after(1000, self.update_timers)

    def start(self):
        self.root.mainloop()

def run_slideshow():
    # List of image paths
    images = ["images\\IMG1.PNG", "images\\IMG2.PNG", "images\\IMG3.PNG"]
    app = SlideshowApp(images)
    app.start()

# Run the slideshow in a separate thread
threading.Thread(target=run_slideshow).start()

# Main loop that triggers the slideshow every hour
while True:
    time.sleep(3600)  # Wait for 1 hour
    run_slideshow()
