import os
import shutil

# Function to split images and annotations
def split_images_and_annotations(source_folder, dest_image_folder, dest_annotation_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(source_folder, filename)
            annotation_filename = os.path.splitext(filename)[0] + ".xml"
            annotation_path = os.path.join(source_folder, annotation_filename)

            if os.path.exists(annotation_path):
                # Move image and annotation files to separate folders
                shutil.move(image_path, os.path.join(dest_image_folder, filename))
                shutil.move(annotation_path, os.path.join(dest_annotation_folder, annotation_filename))

# Paths to the train, test, and valid folders
train_folder = "F://Data Split//train"
test_folder = "F://Data Split//test"
valid_folder = "F://Data Split//valid"

# Paths to the new image and annotation folders
train_image_folder = "trainimage"
train_annotation_folder = "trainanno"
test_image_folder = "testimage"
test_annotation_folder = "testanno"
valid_image_folder = "validimage"
valid_annotation_folder = "validanno"

# Create new folders for images and annotations
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_annotation_folder, exist_ok=True)
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(test_annotation_folder, exist_ok=True)
os.makedirs(valid_image_folder, exist_ok=True)
os.makedirs(valid_annotation_folder, exist_ok=True)

# Split images and annotations for train folder
split_images_and_annotations(os.path.join(train_folder), train_image_folder, train_annotation_folder)

# Split images and annotations for test folder
split_images_and_annotations(os.path.join(test_folder), test_image_folder, test_annotation_folder)

# Split images and annotations for valid folder
split_images_and_annotations(os.path.join(valid_folder), valid_image_folder, valid_annotation_folder)
