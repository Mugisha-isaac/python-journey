import os

try:
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("File does not exists")

except:
    print("Issue occurred while removing the file")
