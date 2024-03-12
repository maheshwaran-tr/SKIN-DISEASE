from PIL import Image
import os
import cv2

def process_image(input_folder,output_folder):
    # Create a new folder for output images if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for image_file in image_files:
        # Load an image
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply a Gaussian blur to the image
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Detect edges in the image using Canny edge detection
        edges = cv2.Canny(blurred_image, 50, 150)

        # Save the processed image to the output folder
        output_image_path = os.path.join(output_folder, "processed_" + image_file)
        cv2.imwrite(output_image_path, edges)

    cv2.destroyAllWindows()

def resize_images(input_folder, output_folder, new_size=(256, 256)):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image (you might want to add more file format checks)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as img:
                # Resize the image
                resized_img = img.resize(new_size)
                
                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

if __name__ == "__main__":
    
    # Replace 'input_folder' and 'output_folder' with your actual folder paths
    input_folder = 'input_images'
    resized_images = 'resized_images'
    
    # Call the function to resize images
    resize_images(input_folder, resized_images)

    # Call the function to process images
    output_folder = 'output_images'
    process_image(resized_images,output_folder)