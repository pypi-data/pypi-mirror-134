import glob
from keras.preprocessing.image import img_to_array, load_img

def resize_file(file, new_size):
    """
    Resize an image to the new size

    file: The location of the file to be saved
    new_size: The image size example: (64, 64)
    """

    #1. Load image with PIL
    img = load_img(file)  # this is a PIL image

    #2. Resize to new size
    img = img.resize(new_size, resample=0)

    img.save(file)

def resize_folder(folder_path, new_size):
    """
    Resize all images in the given folder

    file: The Glob path to the files
    new_size: The image size example: (64, 64)
    """

    all_files = glob.glob(folder_path)
    for item in all_files:
        resize_file(item, new_size)
