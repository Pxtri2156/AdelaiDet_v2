import os



def convert_result(folder_path, out_path):

    for file_name in os.listdir(folder_path):
        extention = file_name.split(".")[-1]
        if extention == "jpg":
            continue
        file_path = os.path.join(folder_path, file_name)
        fi = open(file_path, "r")
        new_path = os.path.join(out_path, file_name)
        new_fi = open(new_path, "w")

        line = fi.readline()
        while line != "":
            print("line: ", line)
            data = line.split(",") 
            coordinates = data[:8]
            int_coordinates = [round(float(coordinate)) for coordinate in coordinates]
            rec = data[-1]
            new_string = "{},{},{},{},{},{},{},{},{}".format(int_coordinates[0],int_coordinates[1],
                                                            int_coordinates[2],int_coordinates[3],
                                                            int_coordinates[4],int_coordinates[5],
                                                            int_coordinates[6],int_coordinates[7],
                                                            rec
             )
            print("new string: ", new_string)
            new_fi.write(new_string)
            line = fi.readline()
        fi.close()
        new_fi.close()
        # break

folder_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/output/batext/vintext"
out_path = "/mlcv/WorkingSpace/SceneText/tripx/AdelaiDet/output/batext/vintext_convert"
convert_result(folder_path, out_path)