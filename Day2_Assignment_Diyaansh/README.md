# Circle Detection using Hough Transform

This project implements an image processing pipeline to detect circles in images using the **Hough Circle Transform** in OpenCV.  
It preprocesses images, detects circular objects, visualizes results, and exports statistical data.

---

## 📁 Repository Structure

```
Day2_Assignment_Diyaansh/
│
├── test_images/
│   ├── test1.jpg
│   ├── test2.png
│   ├── test3.jpg
│
├── results/
│   ├── result_test1.jpg
│   ├── result_test2.jpg
│   ├── result_test3.jpg
│   ├── statistics_test1.txt
│   ├── statistics_test2.txt
│   ├── statistics_test3.txt
│
├── circle_detector.py
└── README.md
```

---

## 🚀 Features

- Image preprocessing using grayscale conversion and Gaussian blur
- Circle detection using Hough Circle Transform
- Visualization of detected circles with ID and radius labels
- Side-by-side display of original and annotated images
- Export of detection statistics to text files

---

## 🛠️ Requirements

Ensure the following Python libraries are installed:

```bash
pip install opencv-python numpy matplotlib
```

---

## ▶️ How to Run

1. Clone or download this repository.
2. Place input images inside the `test_images/` directory.
3. Run the script from the project root directory:

```bash
python circle_detector.py
```

4. Follow the prompts:
   - Enter the image path  
     Example:
     ```
     test_images/test1.jpg
     ```
   - Enter a results folder name or press **Enter** to use the default `results/` folder.

---

## 🖼️ Outputs

For each image, the program generates:

### Annotated Image
- File name: `result_<image_name>.jpg`
- Displays detected circles with:
  - Center point
  - Radius
  - Circle ID

### Statistics File
- File name: `statistics_<image_name>.txt`
- Contains:
  - Total number of detected circles
  - Minimum radius
  - Maximum radius
  - Mean radius
  - Individual circle center coordinates and radius

---

## 📊 Sample Statistics Output

```
total_circles: 3
min_radius: 18
max_radius: 76
mean_radius: 44.67

Circle ID: 1, Center: (135, 92), Radius: 40
Circle ID: 2, Center: (210, 155), Radius: 76
Circle ID: 3, Center: (80, 60), Radius: 18
```

---

## ⚙️ Main Functions

- **preprocess_image()**  
  Loads the image, converts it to grayscale, and applies Gaussian blur.

- **detect_circles()**  
  Detects circles using OpenCV’s Hough Circle Transform.

- **visualize_circles()**  
  Draws circles and labels them, displays side-by-side images, and saves output.

- **calculate_statistics()**  
  Computes and exports statistical information about detected circles.

---

## 📌 Notes

- Detection parameters such as `dp`, `minDist`, `param1`, and `param2` can be modified in `detect_circles()` to improve results for different images.
- Output directories are created automatically if they do not exist.

---

## 👤 Author

Diyaansh  
Day 2 Assignment – Computer Vision
