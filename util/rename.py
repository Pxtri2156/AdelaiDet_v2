import os
import json

path_image = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/VinTextCustom/val_image_rename"
def rename_image_folder(path):
    for file_name in os.listdir(path):
        print('Processing: ', file_name)
        new_name = file_name.replace("im", "")
        print("new name: ", new_name) 
        old_path = os.path.join(path, file_name)
        new_path = os.path.join(path, new_name)
        os.rename(old_path, new_path)

def rename_gt_folder(path):
    for file_name in os.listdir(path):
        print('Processing: ', file_name)
        new_name = file_name.replace("gt", "000")
        print("new name: ", new_name) 
        old_path = os.path.join(path, file_name)
        new_path = os.path.join(path, new_name)
        os.rename(old_path, new_path)


def rename_json(original_json_path, new_json_path):
    fi = open(original_json_path, "r")
    data = json.load(fi)
    for img in data['images']:
        # print("Before: ", img['file_name'])
        img['file_name'] = img['file_name'].replace("im", "")
        # print("After: ", img['file_name'])
    new_fi = open(new_json_path, 'w')
    json.dump(data, new_fi)
    new_fi.close
    fi.close()
    
        

original_json_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/VinTextCustom/val.json"
new_original_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/VinTextCustom/val_rename.json"

rename_json(original_json_path, new_original_path)





