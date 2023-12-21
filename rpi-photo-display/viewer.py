import tkinter as tk
from PIL import Image, ImageTk

master = tk.Tk()
master.attributes('-fullscreen', True)
master.configure(background='black')  # Set background color to black

image = Image.open('photo.jpg')
photo = ImageTk.PhotoImage(image)

# Create a label with the image and pack it to fill the entire screen
label = tk.Label(master, image=photo)
label.image = photo
label.pack(fill=tk.BOTH, expand=True)

master.mainloop()