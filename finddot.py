import cv2
import numpy as np
import os

def preprocess_image(image_path, target_size=(500, 500)):
    """
    Load, resize, and prepare the image for processing.
    Handles grayscale and color preprocessing.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    resized_img = cv2.resize(img, target_size)
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    return resized_img, gray_img

def enhance_edges(gray_img):
    """
    Enhance edges to better detect thin or faint dots.
    """
    blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges

def detect_dots(image, edge_img, min_area=5, max_area=5000):
    """
    Detect dots using contours and handle merged dots with watershed.
    """
    # Convert edges to binary
    _, binary = cv2.threshold(edge_img, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area
    dot_contours = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]

    # For merged dots, apply distance transform and watershed
    kernel = np.ones((3, 3), np.uint8)
    sure_bg = cv2.dilate(binary, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(binary, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Apply the watershed algorithm
    markers = cv2.connectedComponents(sure_fg)[1]
    markers = markers + 1
    markers[unknown == 255] = 0
    cv2.watershed(image, markers)

    # Add watershed-separated contours
    for i in range(2, markers.max() + 1):
        mask = (markers == i).astype(np.uint8)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        dot_contours.extend(contours)

    return dot_contours

def draw_dots(image, contours):
    """
    Draw red circles around detected dots.
    """
    for contour in contours:
        # Get the bounding circle for each contour
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius * 1.2)  # Slightly enlarge the circle for better visibility

        # Draw the circle in red
        cv2.circle(image, center, radius, (0, 0, 255), 2)
    return image

def process_image(image_path, output_path, target_size=(500, 500), min_area=5, max_area=5000):
    """
    Full pipeline to process an image: detect dots, draw circles, and save the result.
    """
    # Preprocess the image
    original_img, gray_img = preprocess_image(image_path, target_size)

    # Enhance edges for better detection of thin dots
    edge_img = enhance_edges(gray_img)

    # Detect dots
    dot_contours = detect_dots(original_img, edge_img, min_area, max_area)

    # Draw detected dots on the original image
    output_img = draw_dots(original_img, dot_contours)
    
    # Count the number of detected dots (contours)
    num_dots = len(dot_contours)
    print(f"Number of dots detected: {num_dots}")

    # Save the result
    cv2.imwrite(output_path, output_img)
    print(f"Processed image saved to: {output_path}")


