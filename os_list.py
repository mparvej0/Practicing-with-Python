# Print a all folder
import os
folders = os.listdir("data")
print(folders)

# Change Directory
# print(os.getcwd())
# os.chdir("/Users")
# print(os/getcwd())

# print a folder
for folder in folders:
    print(folder)

# print file inside in folder.
for folder in folders:
      print(folder)
      print(os.listdir(f"data/{folder}"))

