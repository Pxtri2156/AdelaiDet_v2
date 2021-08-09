import os 
import shutil

root_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/datasets/VinText/vietnamese" 

test_labels = os.path.join(root_path, "test_labels")
unseen_test_labels = os.path.join(root_path, "unseen_test_labels")
train_labels = os.path.join(root_path, "train_labels")

if not os.path.isdir(test_labels):
    os.mkdir(test_labels)
    print("Created folder: ", test_labels)

if not os.path.isdir(unseen_test_labels):
    os.mkdir(unseen_test_labels)
    print("Created folder: ", unseen_test_labels)

if not os.path.isdir(train_labels):
    os.mkdir(train_labels)
    print("Created folder: ", train_labels)

root_labels_path = os.path.join(root_path, "labels")

test_img_path = os.path.join(root_path, 'test_image')
train_img_path = os.path.join(root_path, "train_images")
unseen_test_img_path = os.path.join(root_path, "unseen_test_images") 

for img_name in  os.listdir(test_img_path):
    img_id = int(img_name.split(".")[0].split("m")[-1])
    label_name = "gt_" + str(img_id) + ".txt"

    old_path = os.path.join(root_labels_path, label_name)
    new_path = os.path.join(test_labels, label_name)
    shutil.copyfile(old_path, new_path)

for img_name in  os.listdir(train_img_path):
    img_id = int(img_name.split(".")[0].split("m")[-1])
    label_name = "gt_" + str(img_id) + ".txt"
    old_path = os.path.join(root_labels_path, label_name)
    new_path = os.path.join(train_labels, label_name)
    shutil.copyfile(old_path, new_path)

for img_name in  os.listdir(unseen_test_img_path):
    img_id = int(img_name.split(".")[0].split("m")[-1])
    label_name = "gt_" + str(img_id) + ".txt"
    old_path = os.path.join(root_labels_path, label_name)
    new_path = os.path.join(unseen_test_labels, label_name)
    shutil.copyfile(old_path, new_path)




