import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from palette import generatePalette

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    if file_path:
        tkimage = Image.open(file_path)
        w, h = tkimage.size
        while w > 400 and h > 200:
            if w > 400:
                w = w // 2
            if h > 200:
                h = h // 2
        tkimage = tkimage.resize((w, h))

        photo = ImageTk.PhotoImage(tkimage)
        image_label.config(image=photo)
        image_label.image = photo
        palette_button.config(state=tk.NORMAL)

def paletteImage():
    image = generatePalette(file_path)
    photo = ImageTk.PhotoImage(image)
    palette_image.config(image=photo)
    palette_image.image = photo

root = tk.Tk()
root.geometry("600x500")
root.title("Color Palette Generator")

# Canvas
canvas = tk.Canvas(root, bg='white')
canvas.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Scrollable frame
scrollable_frame = tk.Frame(canvas, bg="white")
window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

# Function to update scroll region and center vertically
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    frame_height = scrollable_frame.winfo_height()
    canvas_height = canvas.winfo_height()
    y_offset = max((canvas_height - frame_height) // 2, 0)
    canvas.coords(window_id, 0, y_offset)  # move frame

# Keep frame width in sync with canvas
def on_canvas_configure(event):
    canvas.itemconfig(window_id, width=event.width)

# Bind events
scrollable_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_configure)

# Enable mouse wheel scrolling everywhere
def on_mousewheel(event):
    canvas.yview_scroll(-int(event.delta / 60), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# UI elements inside scrollable frame
tk.Label(scrollable_frame, text="Generate Color Palette", font=("bold", 24), bg="white").pack()
image_button = tk.Button(scrollable_frame, text="Input Image", command=open_file, bg="white")
image_button.pack(pady=10)

image_label = tk.Label(scrollable_frame, bg="white")
image_label.pack()

palette_button = tk.Button(scrollable_frame, text="Generate Palette", command=paletteImage, state=tk.DISABLED, bg="white")
palette_button.pack(pady=10)

palette_image = tk.Label(scrollable_frame, bg="white")
palette_image.pack()

root.mainloop()
