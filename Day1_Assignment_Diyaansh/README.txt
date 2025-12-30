==========================================================================
PENCIL SKETCH GENERATOR (Computer Vision Assignment)
Day 1 Assignment - Diyaansh
==========================================================================

DESCRIPTION
-----------
This Python script converts standard digital photos (JPG/PNG) into realistic 
black-and-white pencil sketches. It utilizes OpenCV and Numpy to perform 
image processing techniques including grayscale conversion, Gaussian blurring, 
inversion, and Color Dodge blending.

The project meets the following requirements:
1. Loads an image and converts it to a pencil sketch.
2. Implements a "Color Dodge" blend mode logic manually.
3. [BONUS] Includes adjustable blur kernel parameter via user input.
4. Handles file I/O errors robustly (checks if file exists).
5. Saves the final output automatically to a dedicated folder.

FOLDER STRUCTURE
----------------
Day1_Assignment_[YourName]/
|-- pencil_sketch.py        # The main Python script
|-- test_images/            # Folder containing input images
|   |-- test1.jpg
|   |-- test2.jpg
|   +-- test3.jpg
|-- output_sketches/        # Folder where results are saved
|   |-- test1_sketch.png
|   |-- test2_sketch.png
|   +-- test3_sketch.png
+-- README.txt              # This documentation file

DEPENDENCIES
------------
To run this script, the following Python libraries are required:

* opencv-python (cv2)
* numpy
* matplotlib

You can install them using pip:
$ pip install opencv-python numpy matplotlib

HOW TO RUN
----------
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:
   $ python pencil_sketch.py

4. Follow the on-screen prompts:
   - Enter filename: Provide the name of the file inside 'test_images' (e.g., cat.jpg).
   - Enter blur kernel: Choose an odd integer (e.g., 21). Higher numbers = softer shading.

EXAMPLE USAGE
-------------
User Input:
> Enter your file name (in test_images folder): cat.jpg
> Enter the dimensions of blur kernel: 31

Output:
- Displays a side-by-side comparison of the Original vs. Sketch.
- Saves the result to 'output_sketches/cat_sketch.png'.

ALGORITHM DETAILS
-----------------
The sketch effect is achieved through the following pipeline:
1. Grayscale: Converts BGR image to single-channel gray.
2. Invert: Creates a negative of the grayscale image (255 - gray).
3. Gaussian Blur: Smooths the inverted negative to reduce details.
4. Color Dodge: Blends the grayscale image with the blurred negative using:
   Sketch = Gray / (255 - Blurred_Inverted) * 256

CHALLENGES FACED & SOLUTIONS
----------------------------
1. **BGR vs RGB Color Space:**
   Initially, the "Original Image" appeared with a blue tint. I learned that OpenCV loads images in BGR format while Matplotlib displays them in RGB. I fixed this by converting the channels using `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` before plotting.

2. **Saving Blank Images:**
   My saved output files were initially blank white squares. This was because I called `plt.savefig()` after `plt.show()`. I learned that `plt.show()` clears the plot from memory, so I moved the save command before the show command.

3. **Blur Kernel Sensitivity:**
   Finding the right blur amount was difficult. Small kernels (e.g., 5) produced sharp edges with no shading, while large kernels (e.g., 51) looked too foggy. I added the user input feature to allow dynamic testing of different kernel sizes for different images.

AUTHOR
------
Diyaansh K
30-12-2025