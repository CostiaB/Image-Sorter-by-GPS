import os
import shutil
from utils.exif_utils import get_exif_data, get_coordinates
from utils.location_utils import get_location_name, haversine
from geopy.geocoders import Nominatim


def copy_and_group_jpg_files(src_dir, dest_dir, min_size_kb=40, max_distance_km=200):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    no_coords_dir = os.path.join(dest_dir, 'no_coordinates')
    os.makedirs(no_coords_dir, exist_ok=True)

    files_with_coords = []
    files_without_coords = []

    geolocator = Nominatim(user_agent="geo_locator")

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                file_path = os.path.join(root, file)
                file_size_kb = os.path.getsize(file_path) / 1024

                if file_size_kb > min_size_kb:
                    exif_data = get_exif_data(file_path)
                    gps_info = exif_data.get("GPSInfo")
                    coordinates = get_coordinates(gps_info)
                    if coordinates:
                        files_with_coords.append((file_path, coordinates))
                    else:
                        files_without_coords.append(file_path)

    groups = []

    for file_path, coords in files_with_coords:
        placed = False
        for group in groups:
            if haversine(group[0], coords) <= max_distance_km:
                group.append(coords)
                group.append(file_path)
                placed = True
                break
        if not placed:
            groups.append([coords, file_path])

    for i, group in enumerate(groups):
        location_name = get_location_name(geolocator, group[0])
        group_dir = os.path.join(dest_dir, location_name)
        os.makedirs(group_dir, exist_ok=True)
        for file_path in group[1::2]:
            shutil.copy(file_path, group_dir)
            print(f"Copied: {file_path} to {group_dir}")

    for file_path in files_without_coords:
        shutil.copy(file_path, no_coords_dir)
        print(f"Copied: {file_path} to {no_coords_dir}")


# Usage:
source_directory = 'SOURCE_FOLDER'
destination_directory = 'OUTPUT_FOLDER'
copy_and_group_jpg_files(source_directory, destination_directory)
