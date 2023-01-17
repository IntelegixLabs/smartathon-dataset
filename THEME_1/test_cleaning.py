import csv
import shutil
from PIL import Image
import pybboxes as pbx
import json


i = 0

with open('test.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        i += 1
        if i == 1:
            continue
        # if i > 100:
        #     exit(0)




        shutil.copy("images/" + lines[0], "Test_Dataset/" + lines[0])

