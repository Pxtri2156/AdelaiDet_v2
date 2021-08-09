import os
import sys
import  cv2
import  numpy as np

input_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/custom_data/totaltext_txt_example/labels/0000003.txt"
image_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/custom_data/totaltext_txt_example/images/0000003.jpg" 


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
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(0,255,255))
cv2.imwrite("./draff_image.jpg", img)
    # print('pts: ', pts)

# print('data: ', data)