# Color Palette Generator

A desktop application built with Python and Tkinter that extracts the most common colors from an image and presents them in a neat palette with their HEX codes. Perfect for designers, artists, and anyone working with color schemes.

---

## Overview
The app provides a simple way to:
- Select any image file from your computer.
- Visually preview the image.
- Generate a color palette showing the **10 most frequent colors** in that image.
- View both the color swatches and their corresponding HEX codes for easy use in design tools.

---

## How It Works

### 1. Selecting an Image
- When you launch the app, you’ll see a clean interface with an **"Input Image"** button.
- Clicking this opens a file dialog allowing you to select images in formats like `.png`, `.jpg`, `.jpeg`, `.gif`, or `.bmp`.
- The selected image is displayed in the interface, resized proportionally so it fits nicely on the screen.

### 2. Generating the Palette
- Once the image is loaded, the **"Generate Palette"** button becomes active.
- Clicking it runs the palette extraction process:
  1. **Resizing the Image**  
     The image is scaled down (halved) to make processing faster without significantly losing color accuracy.
  2. **Extracting Pixel Colors**  
     The image is converted into a NumPy array, and every pixel’s RGB value is recorded.
  3. **Converting to HEX Codes**  
     Each RGB triplet is converted into a HEX code (e.g., `#ff5733`).
  4. **Counting Color Frequencies**  
     The most common HEX codes are found using Python’s `collections.Counter`.
  5. **Selecting the Top Colors**  
     Up to 10 unique colors are chosen; if fewer are found, black (`#000000`) fills the remaining slots.
  6. **Drawing the Palette**  
     The colors are drawn into a grid (5 on top, 5 on the bottom) with labels showing their HEX codes.

### 3. Displaying the Palette
- The generated palette image is displayed below the original image in the app.
- Each swatch is clearly labeled, making it easy to use the colors in your own projects.

---

## Requirements

You’ll need Python 3.x and the following Python libraries:
- **Pillow** – for image processing
- **NumPy** – for numerical array handling

Install them via pip:
```bash
pip install pillow numpy
```

You’ll also need the `OpenSans-Regular.ttf` font file in the project directory for drawing text labels on the palette.

---

## Running the App
1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Run:
   ```bash
   python main.py
   ```
4. The application window will open.
5. Click **"Input Image"** to load an image, then **"Generate Palette"** to view its colors.

---

## Example
**Input Image:**  
<img src="./image.png" alt="test image" />

**Generated Palette:**  
A 500×240 image containing 10 swatches, each with its HEX code, like:
```
#c1440e  #f4a261  #e9c46a  #2a9d8f  #264653
#ffb703  #fb8500  #8ecae6  #219ebc  #023047
```

---

## Behind the Scenes
- **Interface:** Built with Tkinter for a simple, scrollable GUI.
- **Palette Logic:** Implemented in `palette.py`.
- **Main App Control:** Implemented in `main.py`.
- **Color Counting:** Uses `collections.Counter` to quickly find the most common colors.
- **Cross-Platform:** Works on Windows, macOS, and Linux (as long as Tkinter is available).
