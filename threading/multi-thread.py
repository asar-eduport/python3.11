import os
from multiprocessing import Pool
from PIL import Image

def process_image(image_path):
    """
    Function to convert an image to grayscale and save it.
    """
    try:
        img = Image.open(image_path)
        grayscale_img = img.convert("L")  # Convert image to grayscale
        # Save the grayscale image
        new_path = os.path.splitext(image_path)[0] + "_grayscale.jpg"
        grayscale_img.save(new_path)
        print(f"Processed {image_path}")
    except Exception as e:
        print(f"Failed to process {image_path}: {e}")

def process_images_in_parallel(image_paths, num_processes):
    """
    Function to process multiple images in parallel.
    """
    with Pool(num_processes) as pool:
        pool.map(process_image, image_paths)

if __name__ == "__main__":
    # List of image paths to be processed
    image_folder = "images"
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))]
    
    # Number of processes to run in parallel
    num_processes = 4  # Set this to the number of CPU cores available
    
    # Process images in parallel
    process_images_in_parallel(image_paths, num_processes)
    
    print("All images processed.")
