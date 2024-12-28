import sys
from PIL import Image, ExifTags
slika = Image.open(sys.argv[1])

exif_detalji = {ExifTags.TAGS.get(tag): value for tag, value in slika.getexif().items()}
print(exif_detalji)
#