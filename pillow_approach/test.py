import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

Image.MAX_IMAGE_PIXELS = None
class ImageViewer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Image Viewer")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.bind("<MouseWheel>", self.zoom)
        self.bind("<ButtonPress-1>", self.start_pan)
        self.bind("<B1-Motion>", self.pan)

        self.image = None
        self.image_id = None
        self.file_path = ""

        self.open_image()

    def open_image(self):
        self.file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
        )
        if self.file_path:
            image = Image.open(self.file_path)
            self.image = ImageTk.PhotoImage(image)
            self.canvas.config(scrollregion=(0, 0, image.width, image.height))
            self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def zoom(self, event):
        if self.image:
            factor = 1.1 if event.delta > 0 else 0.9
            self.canvas.scale(tk.ALL, event.x, event.y, factor, factor)

    def start_pan(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def pan(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

if __name__ == "__main__":
    app = ImageViewer()
    app.mainloop()
