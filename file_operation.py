import os
file_dir = "/home/wyj/0000/none/11/"


if not os.path.exists(file_dir) or len(os.listdir(file_dir)) == 0:
    print("the folder is empty !")

folder = os.listdir("/home/wyj/0000/none/")
print(len(folder))
if len(folder) > 0:
    print("the folder is not empty")
else:
    print("the folder is empty ")
