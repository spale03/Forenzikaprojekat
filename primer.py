
import sys
from PIL import Image
from PIL.ExifTags import TAGS


ulazni_argument = sys.argv[1]
slika = Image.open(ulazni_argument)

exif_recnik = {}
if slika._getexif() is not None:
    for tag, value in slika._getexif().items():
        if tag in TAGS:
            if not isinstance(value, bytes):
                exif_recnik[TAGS[tag]] = value

def printaj_exif_podatke(recnik):
    for key, value in recnik.items():
        print(f"{key} : {value}")

if "GPSInfo" in exif_recnik and len(exif_recnik["GPSInfo"]) > 0:
    gps_info = exif_recnik["GPSInfo"]
    # print(exif_recnik)

    print("Podatci Pronadjeni")
    printaj_exif_podatke(exif_recnik)

    def prebaci_u_stepene(value):
        stepeni = float(value[0])
        minuti = float(value[1])
        sekunde = float(value[2])
        return stepeni + (minuti / 60.0) + (sekunde / 3600.0)


    lat = prebaci_u_stepene(gps_info[2])
    lon = prebaci_u_stepene(gps_info[4])
    lat_ref = gps_info[1]
    lon_ref = gps_info[3]

    if lat_ref != "N":
        lat = -lat
    if lon_ref != "E":
        lon = -lon

    geo_coordinate = "{0}° {1}, {2}° {3}".format(lat, lat_ref, lon, lon_ref)
    google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    # print(exif_recnik["MakerNote"])
    print(f"\nGoogle Maps link: {google_maps_link}")
else:
    print("Nema GPS Podataka za sliku.")