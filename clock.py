import tkinter as tk
from tkinter import PhotoImage
import time
from datetime import datetime
from PIL import Image, ImageTk

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%B %d, %Y')
    current_day = datetime.now().strftime('%A')

    clock_label.config(text=f"{current_time}\n{current_day}, {current_date}")
    clock_label.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Load and resize the background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((500, 300), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label to display the time, date, and day
clock_label = tk.Label(window, font=('Helvetica', 50), fg='Red', bg='black', justify='center')
clock_label.pack(padx=50, pady=150)

# Load and resize the clock icon
clock_icon = Image.open("clock_icon.png")
clock_icon = clock_icon.resize((100, 100), Image.ANTIALIAS)
clock_image = ImageTk.PhotoImage(clock_icon)

# Create a label to display the clock icon
clock_icon_label = tk.Label(window, image=clock_image, bg='black')
clock_icon_label.place(x=30, y=30)

# Configure the label to automatically update every second
update_time()

# Start the main event loop
window.mainloop()
