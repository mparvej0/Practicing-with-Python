import os
print("Hello world from ...")
os.system("Python --version")

# Os Module through making 100 folders.
import os
if(not os.path.exists("data")):
 os.mkdir("data")
for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")

# Rename a folder.
import os 
for i in range(0, 100):
   os.rename(f"data/Tutorial{i+1}",f"data/Tutorial {i+1}")


