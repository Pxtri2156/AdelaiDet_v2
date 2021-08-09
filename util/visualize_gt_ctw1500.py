import os

import sys 
import json 
import cv2

import sys
sys.path.append("./")
from util.decode_encode import decode_recs

# check argv 

if  len(sys.argv) < 4:
    print("Missing argv")

imgs_path = sys.argv[1]
annot_path = sys.argv[2]
output_path = sys.argv[3]
annot_fi = open(annot_path, "r")
data = json.load(annot_fi)
isClosed = True
# Blue color in BGR
color = (0, 255, 0)
# Line thickness of 2 px
thickness = 2

annotations = data['annotations']
for img_info in  data['images']:
    img_name = img_info['file_name']
    img_path = os.path.join(imgs_path, img_name)
    img = cv2.imread(img_path)
    for annot in annotations:
        if annot['image_id'] == img_info["id"]:
            bbox = annot['bbox']
            recs = annot['rec']
            recs = decode_recs(recs)
            # print("bbox: ", bbox)
            # print("rec: ", recs)
            x_min, y_min = bbox[0], bbox[1]
            x_max, y_max = x_min + bbox[2], y_min + bbox[3] 
            start_point = (int(x_min), int(y_min))
            end_point = (int(x_max), int(y_max))
            img = cv2.rectangle(img, start_point, end_point, color, thickness)
            cv2.putText(img, recs, (int(x_min), int(y_min-5)), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,0,0), 1 )
        else:
            continue
    img_visualize = os.path.join(output_path, img_name)
    cv2.imwrite(img_visualize, img)
    # break


'''
python util/visualize_gt_ctw1500.py \
    datasets/CTW1500/ctwtest_text_image \
    datasets/CTW1500/annotations/test_ctw1500_maxlen100.json \
    datasets/CTW1500/visualize_test_gt 

'''






