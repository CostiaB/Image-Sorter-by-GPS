# Image-Sorter-by-GPS

Image Sorter by GPS is a Python-based project designed to organize and manage image files based on their GPS metadata. The project contains two main scripts that perform complementary tasks: copying and grouping images based on geographical proximity and renaming folders based on the most common GPS locations in the pictures within them. This tool is especially useful for photographers, travelers, and anyone working with large collections of images that contain location data.

Features
Copy and Group Images by Location:

Copies .jpg images from a specified source directory to a destination directory.
Filters images by file size, ensuring only images larger than a specified threshold (e.g., 10 KB) are processed.
Groups images based on their geographical proximity (e.g., within 100 kilometers of each other).
Creates new folders named after the nearest city or island, and places the grouped images into these folders.
Handles images without GPS data by copying them into a separate "no_coordinates" folder.
Rename Folders Based on GPS Data:

Renames existing folders containing images based on the most common GPS location found within the images.
Extracts GPS data from the images, determines the nearest city or island using reverse geocoding, and renames the folder accordingly.
Ensures that the new folder names are unique and avoids conflicts by checking for existing folders with the same name.
Project Structure
rename_folders.py: The script responsible for renaming existing folders of images based on the GPS data extracted from the images.
copy_and_group_images.py: The script that handles copying images from a source directory, grouping them by location, and organizing them into folders named after the nearest city or island.
utils/: A utility module containing helper functions for extracting EXIF data, handling GPS coordinates, and performing geolocation tasks.
exif_utils.py: Contains functions for working with EXIF data, such as extracting GPS information from images.
location_utils.py: Provides functions for reverse geocoding and calculating distances between geographical coordinates.
requirements.txt: Lists the Python packages required to run the project, including Pillow for image processing and geopy for geolocation services.
README.md: A comprehensive guide on how to set up the project, install dependencies, and use the scripts.
Use Cases
Photographers: Automatically organize photos by location after a shoot, making it easier to create location-based albums.
Travelers: Sort and group travel photos into folders based on the cities or islands visited, creating a neatly organized photo archive.
Archivists: Manage large collections of images by sorting them into location-based folders and ensuring folders are correctly named.
Installation and Usage
Setup:

Clone the repository and navigate to the project directory.
Install the required dependencies using:
bash
Copy code
pip install -r requirements.txt
Usage:

To copy and group images by location, run:
bash
Copy code
python copy_and_group_images.py
To rename existing folders based on GPS data, run:
bash
Copy code
python rename_folders.py
Both scripts can be customized by editing the paths and parameters within the scripts to match your specific use case.

This project is ideal for anyone looking to automate the organization of their image collections based on geographical data, making it easier to manage and access images by location.
