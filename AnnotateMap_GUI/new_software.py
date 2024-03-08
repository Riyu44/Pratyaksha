import cv2
import numpy as np
import pandas as pd
from tkinter import Tk, filedialog

# Global variables
drawing = False  # True if the mouse is pressed
ix, iy = -1, -1
contours = []
img_display = None
scale_factor = 1.0

def resize_image(image, max_height=800, max_width=1200):
    """
    Resize the image to fit within max_height and max_width while maintaining aspect ratio.
    """
    global scale_factor
    height, width = image.shape[:2]
    if height > max_height or width > max_width:
        scale = min(max_height / height, max_width / width)
        image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        scale_factor = scale
    return image

# Mouse callback function
def draw_contour(event, x, y, flags, param):
    global ix, iy, drawing, contours

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        contours.append([(int(x / scale_factor), int(y / scale_factor))])

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img_display, (ix, iy), (x, y), (0, 255, 0), 2)
            ix, iy = x, y
            contours[-1].append((int(x / scale_factor), int(y / scale_factor)))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img_display, (ix, iy), (x, y), (0, 255, 0), 2)
        contours[-1].append((int(x / scale_factor), int(y / scale_factor)))

def save_contours_to_csv(contours, file_name):
    flat_list = [item for sublist in contours for item in sublist]
    df = pd.DataFrame(flat_list, columns=['x', 'y'])
    df.to_csv(file_name, index=False)

def select_image():
    global img_display, contours
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        img = cv2.imread(file_path)
        if img is None:
            print("Error: Image not found.")
            return
        contours = []  # Clear existing contours when a new image is loaded
        img_display = resize_image(img.copy())
        cv2.namedWindow('Image')
        cv2.setMouseCallback('Image', draw_contour)

# Load the image
select_image()

while True:
    cv2.imshow('Image', img_display)
    key = cv2.waitKey(20) & 0xFF
    if key == 27:
        break
    elif key == ord('s'):
        save_contours_to_csv(contours, 'contours.csv')
        print("Contours saved to contours.csv")
    elif key == ord('o'):
        select_image()

cv2.destroyAllWindows()
