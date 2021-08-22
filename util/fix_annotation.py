import os
import json

def remake_annotation(origin_path, target_path):
    for file_name in os.listdir(origin_path):
        print("Processing: ", file_name)
        new_name = file_name.replace("gt_", "000")
        old_path = os.path.join(origin_path, file_name)
        new_path = os.path.join(target_path, new_name)
        # print('old path: ', old_path)
        # print('new path: ', new_path)

        old_fi = open(old_path, 'r')
        new_fi = open(new_path, 'w')
        line = old_fi.readline()
        while line != "":
            # print('line: ', line)
            coordinates = line.split(",")[:8]
            # print("coordinates: ", coordinates)
            rec =  line.split(",")[-1]
            new_rec = '####' + rec
            new_line = "{},{},{},{},{},{},{},{},{}".format(coordinates[0], coordinates[1],
                                                            coordinates[2], coordinates[3],
                                                            coordinates[4], coordinates[5],
                                                            coordinates[6], coordinates[7],
                                                            new_rec
                                                            )
            # print('new line: ', new_line)
            new_fi.write(new_line)
            line = old_fi.readline()
        old_fi.close()
        new_fi.close()



origin_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/VinText/vietnamese/test_labels"
target_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/evaluation/annotation_val_vintext"
remake_annotation(origin_path, target_path)
