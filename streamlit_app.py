import streamlit as st
import os
from copy_and_group_images import copy_and_group_jpg_files
from rename_folders import rename_folders_based_on_gps

st.title('Image GPS Sorter')

# Helper function to prepend the container's path to the host directory
def containerize_path(path):
    return os.path.join('/mnt/host', path.lstrip('/'))

def is_valid_directory(path):
    full_path = containerize_path(path)
    if os.path.isdir(full_path):
        st.write(f"Directory exists: {full_path}")
        return True
    else:
        st.write(f"Directory does not exist: {full_path}")
        return False

# Section for copying and grouping images by location
st.header('Copy and Group Images by Location')

source_directory = st.text_input('Source Directory', value='/home/user/source_directory')
if not is_valid_directory(source_directory):
    st.error("Please enter a valid source directory.")
    st.stop()

destination_directory = st.text_input('Destination Directory', value='/home/user/destination_directory')
if not is_valid_directory(destination_directory):
    st.error("Please enter a valid destination directory.")
    st.stop()

min_size_kb = st.number_input('Minimum Size (KB)', value=10, min_value=1)
max_distance_km = st.number_input('Max Distance (KM)', value=100, min_value=1)

if st.button('Start Copying and Grouping'):
    if is_valid_directory(source_directory) and is_valid_directory(destination_directory):
        # Use the containerized paths
        copy_and_group_jpg_files(containerize_path(source_directory), containerize_path(destination_directory), min_size_kb, max_distance_km)
        st.success('Images have been copied and grouped successfully!')
    else:
        st.error("Please make sure both source and destination directories are valid.")

# Section for renaming folders based on GPS data
st.header('Rename Folders Based on GPS Data')

root_directory = st.text_input('Root Directory for Renaming Folders', value='/home/user/root_directory')
if not is_valid_directory(root_directory):
    st.error("Please enter a valid root directory.")
    st.stop()

if st.button('Start Renaming Folders'):
    if is_valid_directory(root_directory):
        # Use the containerized path
        rename_folders_based_on_gps(containerize_path(root_directory))
        st.success('Folders have been renamed successfully!')
    else:
        st.error("Please make sure the root directory is valid.")
