import os
import shutil
import sys

def move_files_with_keyword(keyword, target_directory):
    # Check if the target directory exists, if not, create it
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Walk through the current directory and its subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if keyword in file:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(target_directory, file)
                
                # Move the file to the target directory
                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} to {destination_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python move_files.py keyword target_directory")
        sys.exit(1)

    keyword = sys.argv[1]
    target_directory = sys.argv[2]

    move_files_with_keyword(keyword, target_directory)
    print(f"All files containing '{keyword}' have been moved to '{target_directory}'")
