import barcode
import csv
from barcode.writer import ImageWriter
from PIL import Image
import os, PIL, glob
from docx import Document
from docx.shared import Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL

def generateDocx(file):
    print("  "+file)
    document = Document("VZOR.docx")

    table = document.tables[0]

    for sRow in table.rows:
        for sCell in sRow.cells:
            sCell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            paragraph = sCell.paragraphs[0]
            run = paragraph.add_run()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run.add_picture("cache/"+file+".png", width=Cm(4.74), height=Cm(2.41))
    #
    document.save(file+".docx")

def generatePNG(number):
    # Generate barcode
    ean = barcode.get('ean13', number, writer=ImageWriter())

    filename = ean.save("cache/"+number, {"module_width":0.4,"module_height":13, "font_size": 20, "text_distance": 1, "quiet_zone": 2})
    # Resize
    image = Image.open(filename)
    resized = image.resize((226,100))
    resized.save(filename)

def clearCache():
    print("\nMažu cache..")
    for filename in os.listdir("cache"):
        os.remove("cache/"+filename)

# Main
fields = []
rows = []
with open('togen.csv', 'r', encoding="UTF8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
print("Generuji EANY..")

for row in rows:
    generatePNG(row[1])
    generateDocx(row[1])

clearCache()
print("  Hotovo!")

