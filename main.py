import finddot
import os

def main():
    if __name__ == "__main__":
        image_dir = "Images"  # Folder containing input images
        output_dir = "Processed_Images"  # Folder to save processed images
        os.makedirs(output_dir, exist_ok=True)

        # Process all images in the folder
        for image_file in os.listdir(image_dir):
            if image_file.endswith(('.jpg', '.png')):
                input_path = os.path.join(image_dir, image_file)
                output_path = os.path.join(output_dir, f"processed_{image_file}")
                finddot.process_image(input_path, output_path)

main()