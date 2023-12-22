import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.attributes('-fullscreen', True)
window.configure(background='black')  # Set background color to black

image = Image.open('photo.jpg')
photo = ImageTk.PhotoImage(image)

# Create a label with the image and pack it to fill the entire screen
label = tk.Label(window, image=photo)
label.pack(fill=tk.BOTH, expand=True)

window.mainloop()