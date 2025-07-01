import os

for root, dirs, files in os.walk("Chapter_10_Useful_Modules/133_os_walk"):
    print("Root:", root)
    for f in files:
        filename, filetype = os.path.splitext(f)
        if filetype == '.html':
            os.remove(os.path.join(root, f))