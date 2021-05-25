import barcode
import csv
from barcode.writer import ImageWriter
from PIL import Image
import os, PIL, glob

def generatePNG(number):
    # Generate barcode
    ean = barcode.get('ean13', number, writer=ImageWriter())

    filename = ean.save(number, {"module_width":0.4,"module_height":13, "font_size": 20, "text_distance": 1, "quiet_zone": 2})
    # Resize
    image = Image.open(filename)
    resized = image.resize((226,100))
    resized.save(filename)

fields = []
rows = []
with open('togen.csv', 'r', encoding="UTF8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print("EANY")

for row in rows:
    # for col in row:
    #     print("col: "+col)
    print(row[1])
    generatePNG(row[1])

