import csv
import shutil
from PIL import Image
import pybboxes as pbx
import json

image_class = {'GRAFFITI': 0, 'FADED_SIGNAGE': 1, 'POTHOLES': 2, 'GARBAGE': 3,
               'CONSTRUCTION_ROAD': 4, 'BROKEN_SIGNAGE': 5, 'BAD_STREETLIGHT': 6,
               'BAD_BILLBOARD': 7, 'SAND_ON_ROAD': 8, 'CLUTTER_SIDEWALK': 9,
               'UNKEPT_FACADE': 10}

i = 0
# opening the CSV file

prev_image = ""
array = []
dataset = ""
with open('train.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        i += 1
        if i == 1:
            continue
        # if i > 100:
        #     exit(0)
        print(i, lines)


        img = Image.open("images/" + lines[1])

        # get width and height
        width = img.width
        height = img.height

        print(width, height)


        xmax = int(float(lines[3]) * 2)
        xmin = int(float(lines[4]) * 2)
        ymax = int(float(lines[5]) * 2)
        ymin = int(float(lines[6]) * 2)

        if xmin < 0:
            xmin = 0
        if ymin < 0:
            ymin = 0

        if xmax > width:
            xmax = width
        if ymax > height:
            ymax = height



        x1, y1, x2, y2 = pbx.convert_bbox([xmin, ymin, xmax, ymax], from_type="voc", to_type="yolo", image_size=(width, height))

        if prev_image == "":
            prev_image = lines[1]
            array = [[int(float(lines[0])), x1, y1, x2, y2]]
            dataset = lines[2]
        elif prev_image != lines[1]:

            shutil.copy("images/" + prev_image, "Dataset/" + str(dataset) + "/" + prev_image)
            filename = "Dataset/" + str(dataset) + "/" + prev_image.split(".")[0] + ".txt"

            print(array)

            with open(filename, 'w') as f:
                for sublist in array:
                    line = "{} {} {} {} {}\n".format(sublist[0], sublist[1], sublist[2], sublist[3], sublist[4])
                    f.write(line)

            prev_image = lines[1]
            array = [[int(float(lines[0])), x1, y1, x2, y2]]
            dataset = lines[2]

        elif prev_image == lines[1]:
            array.append([int(float(lines[0])), x1, y1, x2, y2])



        # print(x1, y1, x2, y2)
        #
        # json_data = {
        #     "userid": str("raj713335"),
        #     "image_url": str("Data/Saved_Images/"+lines[1]),
        #     "w_cord": float(x1),
        #     "x_cord": float(y1),
        #     "y_cord": float(x2),
        #     "z_cord": float(y2),
        #     "latitude": float(22.5626),
        #     "longitude": float(88.363),
        #     "class_of_image": int(float(lines[0])),
        #     "auto": "Yes",
        #     "uploaded": "Yes"
        # }
        #
        # print(json_data)
        #
        # with open('sample.json', 'r+') as openfile:
        #     # Reading from json file
        #     json_object = json.load(openfile)
        #     json_object["data"].append(json_data)
        #     openfile.seek(0)
        #     json.dump(json_object, openfile, indent=4)
