import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def pencil_sketch(image_path, blur_kernel=21):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not find image at {image_path}")
        return None, None
    else:
        print(f"Loaded image: {image.shape}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (blur_kernel, blur_kernel), 0)
    inverted_blurred = 255 - blurred
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

    return image, sketch

def display_result(image_path, original, sketch, output_folder):
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    axes = axes.ravel()
    
    axes[0].imshow(original_rgb)
    axes[0].set_title("Original Image")

    axes[1].imshow(sketch, cmap='gray')
    axes[1].set_title("Pencil Sketch")
    
    for ax in axes:
        ax.axis('off')

    plt.tight_layout()

    filename = os.path.basename(image_path)
    base, ext = os.path.splitext(filename)
    save_path = os.path.join(output_folder, f"{base}_sketch.jpg")
    
    plt.savefig(save_path)
    print(f"Saved sketch to: {save_path}")
    plt.show()

def main():
    input_folder = 'Day1_Assignment_Diyaansh/test_images'
    output_folder = 'Day1_Assignment_Diyaansh/output_sketches'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    while True:
        file_name = input(f"Enter your file name (in {input_folder} folder): ")
        image_path = os.path.join(input_folder, file_name)

        if not os.path.exists(image_path):
            print(f"Error: File '{image_path}' not found. Retry.")
        else:
            break

    blur_kernel = int(input("Enter blur kernel (Odd integer, Recommended: 21): "))
    if blur_kernel % 2 == 0:
        blur_kernel += 1
        print(f"Even blur kernel size detected. Modified to {blur_kernel}")

    initial_image, final_sketch = pencil_sketch(image_path, blur_kernel)
    
    if initial_image is not None and final_sketch is not None:
        display_result(image_path, initial_image, final_sketch, output_folder)
    else:
        print("Error: Converting image to sketch failed.")

if __name__ == '__main__':
    main()