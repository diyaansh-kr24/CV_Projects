import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    """
    Load an preprocess image for circle detection.

    Args:
        image_path (str): Path to the input image.
    
    Returns:
        tuple: (original_color, preprocessed_gray) or (None, None)
    """
   
    try:
        if not isinstance(image_path, str):
            print("Error: image_path must be a string.")
            return (None, None)
        
        original_color = cv2.imread(image_path)
        
        if original_color is None:
            print(f"Error: Unable to load image at {image_path}")
            return (None, None)
        
        gray_image = cv2.cvtColor(original_color, cv2.COLOR_BGR2GRAY)
        
        preprocessed_gray = cv2.GaussianBlur(gray_image, (21, 21), 2)
        
        return (original_color, preprocessed_gray)
    except Exception as e:
        print(f"Error occurred while preprocessing image: {e}")
        return (None, None)

def detect_circles(gray_image, dp = 1.2, minDist = 10, param1=100, 
                   param2=35, minRadius = 10, maxRadius = 100):
    """
    Detect circles using Hough Circle Transform.

    Args:
        gray_image (numpy.ndarray): Preprocessed grayscale image.
        dp (float): Inverse ratio of the accumulator resolution to the image resolution.
        minDist (int): Minimum distance between detected centers.
        param1 (int): Upper threshold for the Canny edge detector.
        param2 (int): Threshold for center detection.
        minRadius (int): Minimum circle radius.
        maxRadius (int): Maximum circle radius.
    
    Returns:
        numpy array of circles or None
    """
    if gray_image is None:
        print("Error: detect_circles received a NoneType image. Ensure preprocessing was successful.")
        return None
    
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1,
                               param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        return circles
    else:
        return None

def visualize_circles(image, circles, save_path = None):
    """
    Draw detected circles on the image, label ID/radius and display side-by-side.

    Args:
        image: Original color image
        circles: Array of detected circles
        save_path: Optional Path to save annotated image
    """
    if image is None:
        print("Error: No image provided for visualization.")
        return None
    
    annotated_image = image.copy()
    
    if circles is not None:

        for idx, circle in enumerate(circles[0, :]):
            cx, cy, radius = circle

            cv2.circle(annotated_image, (cx, cy), radius, (0, 255, 0), 2)
            cv2.circle(annotated_image, (cx, cy), 2, (0, 0, 255), 3)

            label = f"ID:{idx+1} R:{radius}"
            cv2.putText(annotated_image, label, (cx + 10, cy - 10), 
                         cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    annotated_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    ax1.imshow(original_rgb)
    ax1.set_title("Original Image")
    ax1.axis('off')
    
    ax2.imshow(annotated_rgb)
    ax2.set_title("Annotated Results (ID & Radius)")
    ax2.axis('off')
    
    plt.tight_layout()
    if save_path is not None:
        plt.savefig(save_path)
        print(f"Side-by-side plot saved to {save_path}")

    plt.show()


def calculate_statistics(circles, export_path=None):
    """
    Calculate and display statistics of detected circles.

    Args:
        circles: Array of detected circles
    
    Returns:
        dict: Statistics dictionary
    """
    if circles is None:
        print("No circles detected.")
        return {}

    radii = [circle[2] for circle in circles[0, :]]
    stats = {
        "total_circles": len(radii),
        "min_radius": np.min(radii),
        "max_radius": np.max(radii),
        "mean_radius": np.mean(radii),
    }

    output_lines = []
    print("-------- Circle Detection Statistics --------")
    for key, value in stats.items():
        print(f"{key}: {value}")
        output_lines.append(f"{key}: {value}")    
    
    print("-------- Individual Circle Statistics --------")
    for circle in circles[0, :]:
        cx, cy, radius = circle
        print(f"Circle ID: {circle[0]}, Center: ({cx}, {cy}), Radius: {radius}")
        output_lines.append(f"Circle ID: {circle[0]}, Center: ({cx}, {cy}), Radius: {radius}")

    if export_path:
        with open(export_path, "w") as f:
            f.write("\n".join(output_lines))
        print(f"Statistics exported to {export_path}")
    return stats

def main():
    """ Main function to execute circle detection pipeline."""
    while True:
        image_path = input("Enter the path to the image(Eg: test1.jpg): ")

        if not image_path.strip():
            print("Error: Image path cannot be empty. Please try again.")
            continue

        if not os.path.exists(image_path):
            print(f"Error: The file at {image_path} does not exist. Please try again.")
            continue

        break
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    save_folder_name = input("Enter save folder (press Enter for default 'results'): ").strip()
    if not save_folder_name:
        save_folder_name = "results"
    
    save_folder = os.path.join(script_dir, save_folder_name)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"Created folder: {save_folder}")

    base_name = os.path.splitext(os.path.basename(image_path))[0]
    save_img_path = os.path.join(save_folder, f"result_{base_name}.jpg")
    save_stats_path = os.path.join(save_folder, f"statistics_{base_name}.txt")
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return    

    original_color, preprocessed_gray = preprocess_image(image_path)
    circles = detect_circles(preprocessed_gray)
    visualize_circles(original_color, circles, save_img_path if save_img_path.strip() else None)
    calculate_statistics(circles, export_path=save_stats_path if save_stats_path.strip() else None) 
    
if __name__ == "__main__":
    main()

