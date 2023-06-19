import os
import shutil

def move_image_to_folder(image_path, folder):
    filename = os.path.basename(image_path)
    destination = os.path.join(folder, filename)

    shutil.copy(image_path, destination)