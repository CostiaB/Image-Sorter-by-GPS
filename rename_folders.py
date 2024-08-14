import os
from utils.exif_utils import get_exif_data, get_coordinates
from utils.location_utils import get_location_name
from collections import Counter
from geopy.geocoders import Nominatim

def rename_folders_based_on_gps(root_directory):
    geolocator = Nominatim(user_agent="geo_locator")

    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)

        if os.path.isdir(folder_path):
            location_names = []

            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith('.jpg'):
                    file_path = os.path.join(folder_path, file_name)
                    exif_data = get_exif_data(file_path)
                    gps_info = exif_data.get("GPSInfo")
                    coordinates = get_coordinates(gps_info)

                    if coordinates:
                        location_name = get_location_name(geolocator, coordinates)
                        location_names.append(location_name)

            if location_names:
                most_common_location = Counter(location_names).most_common(1)[0][0]
                if most_common_location:
                    new_folder_name = most_common_location.replace(" ", "_").replace("/", "_")
                    new_folder_path = os.path.join(root_directory, new_folder_name)

                    if not os.path.exists(new_folder_path):
                        os.rename(folder_path, new_folder_path)
                        print(f"Renamed folder: {folder_name} -> {new_folder_name}")
                    else:
                        print(f"Folder with name {new_folder_name} already exists. Skipping rename.")
            else:
                print(f"No GPS data found in images in folder: {folder_name}")

# Example usage:
root_directory = '/path/to/root_directory'
rename_folders_based_on_gps(root_directory)
