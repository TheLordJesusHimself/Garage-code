import os

# Define the path to your folder (using raw string to prevent escape sequence issues)
folder_path = r"C:\ProgramData\GarageCalc\Data"  # Replace with the correct folder path

# Check if the folder exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Iterate over the files in the folder
    for file_name in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            print(file_name)
else:
    print(f"The folder {folder_path} does not exist or is not a directory.")
