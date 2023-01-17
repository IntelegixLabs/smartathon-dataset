import cv2

def plot_one_box(x, img, color=None, label=None, line_thickness=None, Inverted=False):
    # Plots one bounding box on image img
    tl = line_thickness or 2 # line thickness
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl)
    if label:
        tf = tl # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 2, thickness=tf)[0]
    if Inverted == True:
        c1 = c2
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    else:
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1) # filled
        cv2.putText(
        img,
        label,
        (c1[0], c1[1] - 2),
        0,
        tl / 2,
        [225, 255, 255],
        thickness=tf,
        lineType=cv2.LINE_AA,
        )

# Using readlines()

Lines = [[1,"1.jpg","GRAFFETI",925,537,1056,660]]

count = 0
# Strips the newline character
for line in Lines:


    # if count == 100:
    #     break

    print(line)

    file_id_path = line[1]
    print(file_id_path)
    # open image in cv2
    img = cv2.imread(file_id_path)
    h, w, c = img.shape
    cat = line[2]
    xmax = int(float(line[3]))
    xmin = int(float(line[4]))
    ymax = int(float(line[5]))
    ymin = int(float(line[6]))
    # plot the box
    plot_one_box([xmax, xmin, ymax, ymin], img, color=(0, 255, 0), label=cat, line_thickness=2)
    # save the image
    # you might need to create the folder "drawn" first!
    cv2.imwrite("drawn/" + file_id_path, img)

    count += 1