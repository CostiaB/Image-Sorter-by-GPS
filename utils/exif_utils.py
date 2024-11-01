from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    exif_data = {}
    try:
        img = Image.open(image)
        info = img._getexif()
        if info:
            for tag, value in info.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "GPSInfo":
                    gps_data = {}
                    for gps_tag in value:
                        gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                        gps_data[gps_tag_name] = value[gps_tag]
                    exif_data[tag_name] = gps_data
                else:
                    exif_data[tag_name] = value
    except Exception as e:
        print(f"Error getting EXIF data from {image}: {e}")
    return exif_data

def get_coordinates(gps_info):
    if not gps_info:
        return None

    def to_degrees(value):
        if not value or len(value) < 3:
            return None
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])
        return d + (m / 60.0) + (s / 3600.0)

    lat = to_degrees(gps_info.get("GPSLatitude"))
    if lat is not None and gps_info.get("GPSLatitudeRef") == 'S':
        lat = -lat

    lon = to_degrees(gps_info.get("GPSLongitude"))
    if lon is not None and gps_info.get("GPSLongitudeRef") == 'W':
        lon = -lon

    if lat is not None and lon is not None:
        return (lat, lon)
    else:
        return None

