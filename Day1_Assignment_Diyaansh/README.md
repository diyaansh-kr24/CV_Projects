# Pencil Sketch Generator

**Computer Vision Assignment**

This project converts standard digital images into realistic black-and-white
pencil sketches using classical image processing techniques. The implementation
is done entirely in Python using OpenCV and NumPy, with a focus on manual control
over each processing step.

---

## 📁 Repository Structure

```
Day1_Assignment_Diyaansh/
│
├── test_images/
│   ├── test1.jpg
│   ├── test2.jpg
│   └── test3.jpg
│
├── output_sketches/
│   ├── test1_sketch.png
│   ├── test2_sketch.png
│   └── test3_sketch.png
│
├── pencil_sketch.py
└── README.md
```

---

## 🚀 Features

- Converts color images into pencil-style sketches
- Manual implementation of Color Dodge blending
- Grayscale conversion and Gaussian blurring
- User-defined blur kernel size for shading control
- Side-by-side visualization of original and sketch images
- Automatic saving of outputs to a dedicated folder
- Robust file existence and input validation

---

## 🛠️ Requirements

The following Python libraries are required:

```bash
pip install opencv-python numpy matplotlib
=======
**Computer Vision Assignment**

---

## Overview

This Python script converts standard digital photos (JPG/PNG) into realistic 
black-and-white pencil sketches. It utilizes OpenCV and Numpy to perform 
image processing techniques including grayscale conversion, Gaussian blurring, 
and inversion.

---

## Project Requirements

The project fulfills the following requirements:

- Loads an image and converts it into a pencil sketch
- Implements Color Dodge blending manually
- Bonus: Allows user-defined Gaussian blur kernel size
- Handles file I/O errors robustly (checks if files exist)
- Automatically saves the output to a dedicated folder

---

## Folder Structure
```
Day1_Assignment_Diyaansh/
├── pencil_sketch.py # Main Python script
├── test_images/ # Folder containing input images
│ ├── test1.jpg
│ ├── test2.jpg
│ └── test3.jpg
├── output_sketches/ # Folder where results are saved
│ ├── test1_sketch.png
│ ├── test2_sketch.png
│ └── test3_sketch.png
└── README.md # Project documentation
>>>>>>> f27df00f7ccc6a28738b93ae4a2e6a6b44407811
```

---

## ▶️ How to Run

1. Open a terminal or command prompt.
2. Navigate to the project root directory.
3. Run the script:

```bash
python pencil_sketch.py
```

4. Follow the on-screen prompts:
   - Enter the image filename (located inside `test_images/`)
     ```
     test1.jpg
     ```
   - Enter an odd integer for the Gaussian blur kernel size
     ```
     21
     ```

---

## 🖼️ Output

For each input image, the script generates:

### Pencil Sketch Image
- File name format: `<image_name>_sketch.png`
- Saved inside the `output_sketches/` folder
- Displays smooth shading and pencil-like outlines

### Visualization
- Side-by-side display of:
  - Original image
  - Generated pencil sketch

---

## 📊 Example Usage

### User Input

```
Enter your file name (in test_images folder): test1.jpg
Enter the dimensions of blur kernel: 21
```

### Output Behavior

- Displays original and sketch images side by side
- Saves the result automatically to:
  ```
  output_sketches/test1_sketch.png
  ```

---

## ⚙️ Core Processing Steps

- Convert image to grayscale
- Invert grayscale image
- Apply Gaussian blur
- Perform Color Dodge blending manually
- Normalize and display output

---

## 📌 Challenges and Solutions

### BGR vs RGB Color Space

**Problem:**  
Displayed images appeared blue-tinted.

**Cause:**  
OpenCV loads images in BGR format, while Matplotlib expects RGB.

**Solution:**
```python
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

---

### Saving Blank Images

**Problem:**  
Saved output images were completely white.

**Cause:**  
`plt.savefig()` was called after `plt.show()`, which clears the plot.

**Solution:**  
Moved `plt.savefig()` before calling `plt.show()`.

---

### Blur Kernel Sensitivity

**Problem:**  
Small kernels produced harsh lines; large kernels created washed-out sketches.

**Solution:**  
Allowed the user to control the Gaussian blur kernel size for better adaptability.

---

## 👤 Author

Diyaansh K  
Day 1 Assignment - Computer Vision
30-12-2025
=======
## Dependencies

The following Python libraries are required to run the script:

- opencv-python
- numpy
- matplotlib

---

## Installation

pip install opencv-python numpy matplotlib

---

## How to Run

1. Open your terminal or command prompt  
2. Navigate to the project directory  
3. Run the script:
4. Follow the on-screen prompts:
   - Enter filename: Name of the image inside the test_images folder (e.g., cat.jpg)
   - Enter blur kernel: An odd integer (e.g., 21). Higher values result in softer shading.

---

## Example Usage

### User Input

Enter your file name (in test_images folder): test1.jpg
Enter the dimensions of blur kernel: 21

### Output

- Displays a side-by-side comparison of the Original Image and the Pencil Sketch
- Saves the final image to: output_sketches/cat_sketch.png

---

## Challenges Faced and Solutions

### BGR vs RGB Color Space

#### Problem:  
The original image appeared blue-tinted during visualization.

#### Cause:  
OpenCV loads images in BGR format, while Matplotlib expects RGB.

#### Solution:
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

### Saving Blank Images

#### Problem:  
Saved output images appeared completely white.

#### Cause:  
plt.savefig() was called after plt.show(), which clears the plot from memory.

#### Solution:  
Moved plt.savefig() before calling plt.show().

### Blur Kernel Sensitivity

#### Problem:  
Small kernels produced overly sharp images, while large kernels resulted in foggy sketches.

#### Solution:  
Added user input to adjust the blur kernel size for different images.

---

## Author

Diyaansh K  
30-12-2025


>>>>>>> f27df00f7ccc6a28738b93ae4a2e6a6b44407811
