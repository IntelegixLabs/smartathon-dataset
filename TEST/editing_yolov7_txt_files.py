import glob

txtfiles = []
for file in glob.glob("POTHOLES/*.txt"):
    txtfiles.append(file)

for each in txtfiles:
    with open(each) as f:
        lines = f.readlines()
        new_list = []
        for line in lines:
            x = " ".join(line.split(" ")).replace("\n", "").split(" ")
            if x[0] != '2':

                print(x)
                continue
                print("Error")
                exit(0)
            x[0] = 0
            new_list.append(x)
        print(new_list)
        print(each)
        filename = each.split("\\""")[1]
        print(filename)

        with open("NEW_POTHOLES/"+filename, 'w') as f:
            for sublist in new_list:
                line = "{} {} {} {} {}\n".format(sublist[0], sublist[1], sublist[2], sublist[3], sublist[4])
                f.write(line)


