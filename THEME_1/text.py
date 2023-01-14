


lst = [[7, 0.526495, 0.487755, 0.354620, 0.755102], [7, 0.526495, 0.487755, 0.354620, 0.755102], [7, 0.526495, 0.487755, 0.354620, 0.755102]]

filename = 'test.txt'

with open(filename, 'w') as f:
     for sublist in lst:
          line = "{} {} {} {} {}\n".format(sublist[0], sublist[1], sublist[2], sublist[3], sublist[4])
          f.write(line)