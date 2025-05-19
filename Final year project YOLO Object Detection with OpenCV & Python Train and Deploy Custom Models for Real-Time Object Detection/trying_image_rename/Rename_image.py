import os

def rename_images(directory):
    # Get a list of files in the directory
    files = os.listdir(directory)
    
    # Filter out non-image files (optional, adjust as needed)
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    images = [file for file in files if file.lower().endswith(image_extensions)]
    
    # Sort files to ensure consistent renaming
    images.sort()

    # Rename each image file
    for index, filename in enumerate(images):
        # Generate new filename with leading zeros
        new_filename = f"{index+1:05d}{os.path.splitext(filename)[1]}"
        
        # Get full file paths
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        
        # Rename file
        os.rename(old_file_path, new_file_path)
        
        print(f"Renamed '{filename}' to '{new_filename}'")

# Specify the directory containing the images
image_directory = r'D:\Final year project\trying_image_rename\no order img'

# Call the function to rename images
rename_images(image_directory)
