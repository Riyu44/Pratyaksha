import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab

# global variables
WIDTH = 750
HEIGHT = 560
file_path = ""
pen_size = 3
pen_color = "black"

#function to open the image file
def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Select the 'fullres' tissue sample", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
    if file_path:
        global photo_image  # Maintain a global reference
        image = Image.open(file_path)
        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
        # image = Image.open(file_path)
        # new_width = int((WIDTH/2))
        # image=image.resize((new_width, HEIGHT), Image.LANCZOS)
        # image=ImageTk.PhotoImage(image)
        # canvas.create_image(0, 0, anchor="nw", image=image)
        # canvas.image = image

root = ttk.Window(themename="lumen")
root.title("Pratyaksha")
root.geometry("510x580+300+110")
# root.resizable(0, 0)
icon = ttk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)

# the left frame to contain the 4 buttons
left_frame = ttk.Frame(root, width=200, height=600)
left_frame.pack(side="left", fill="y")

# the right canvas for displaying the image
canvas = ttk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# label
filter_label = ttk.Label(left_frame, text="Select Mode:", background="white")
filter_label.pack(padx=0, pady=2)

# a list of filters
image_filters = ["Manual","Auto-extract"]

# combobox for the filters
filter_combobox = ttk.Combobox(left_frame, values=image_filters, width=15)
filter_combobox.pack(padx=10, pady=5)

# loading the icons for the 4 buttons
image_icon = ttk.PhotoImage(file = 'add.png').subsample(6, 6)
hand_icon = ttk.PhotoImage(file = 'hand.png').subsample(6, 6)
pen_icon = ttk.PhotoImage(file = 'pen.png').subsample(6, 6)
circle_icon = ttk.PhotoImage(file = 'circle.png').subsample(6, 6)
color_icon = ttk.PhotoImage(file = 'color.png').subsample(6, 6)
erase_icon = ttk.PhotoImage(file = 'erase.png').subsample(6, 6)
save_icon = ttk.PhotoImage(file = 'saved.png').subsample(6, 6)

# button for adding/opening the image file
image_button = ttk.Button(left_frame, image=image_icon, bootstyle="light", command=open_image)
image_button.pack(pady=(0,5))
# button for hand instead of cursor
hand_button = ttk.Button(left_frame, image=hand_icon, bootstyle="light")
hand_button.pack(pady=(0,5))
# button for pen tool
pen_button = ttk.Button(left_frame, image=pen_icon, bootstyle="light")
pen_button.pack(pady=(0,5))
# button for circle tool
circle_button = ttk.Button(left_frame, image=circle_icon, bootstyle="light")
circle_button.pack(pady=(0,5))
# button for choosing pen color
color_button = ttk.Button(left_frame, image=color_icon, bootstyle="light")
color_button.pack(pady=(0,5))
# button for erasing the lines drawn over the image file
erase_button = ttk.Button(left_frame, image=erase_icon, bootstyle="light")
erase_button.pack(pady=(0,5))
# button for saving the image file
save_button = ttk.Button(left_frame, image=save_icon, bootstyle="light")
save_button.pack(pady=(0,5))

root.mainloop()