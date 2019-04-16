import random
import os
import os.path
import io

fil = open(
    "/home/vishal.sharma.17csc/Vishal/food_detection/food100/test.txt", "w+")
for i in range(1, 101):
    path, dirs, files = os.walk(
        "/home/vishal.sharma.17csc/Vishal/food_detection/UECFOOD100/"+str(i)).__next__()
    file_count = len(files)
    print(file_count)
    count = 0
    for k in range(20000, 1, -1):
        if count == int(file_count*0.2):
            break
        exists = os.path.isfile(
            "/home/vishal.sharma.17csc/Vishal/food_detection/UECFOOD100/"+str(i)+"/"+str(k)+".jpg")
        if exists:
            s = "/home/vishal.sharma.17csc/Vishal/food_detection/UECFOOD100/" + \
                str(i)+"/"+str(k)+".jpg\n"
            fil.write(s)
            count = count+1
            print("/home/vishal.sharma.17csc/Vishal/food_detection/UECFOOD100/" +
                  str(i)+"/"+str(k)+".jpg")
        else:
            continue
fil.close()
