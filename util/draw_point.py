import os
import sys
import  cv2
import  numpy as np

input_path = "datasets/VinText/vietnamese/test_labels/gt_1201.txt"
image_path = "datasets/VinText/vietnamese/test_image/im1201.jpg" 


annot_fi = open(input_path, "r")

data = annot_fi.readlines()
img = cv2.imread(image_path)

for anno in data:
    coordinates = anno.split(",")[:-1]
    label = anno.split(",")[-1]
    # print('coordinates: ', coordinates)
    print('label: ', label)
    if label == "#":
        continue
    pts = []
    pts = np.array([[int(coordinates[i]), int(coordinates[i+1])]  for i in range(0, len(coordinates), 2)])
    i = 3
    img = cv2.circle(img, (pts[i][0], pts[i][1]), 2, (0, 255, 0), 1)
    break

cv2.imwrite("./draff_image.jpg", img)
    # print('pts: ', pts)

# print('data: ', data)
'''
/mlcv/Databases/VinText/
unzip /mlcv/Databases/VinText/vietnamese_original.zip -d datasets/VinText

'''