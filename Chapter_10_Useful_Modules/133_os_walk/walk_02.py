import os

print(1)

for folder, sub_folders, files in os.walk("Chapter_10_Useful_Modules/133_os_walk"):
    print("--------------------------------------------")
    print("Currently we are looking at folder " + folder)
    print("The subfolders in current directory are:")
    for sub in sub_folders:
        print(sub)
    print("The files in current directory are:")
    for f in files:
        print(f)