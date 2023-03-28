# import os to delete file 
import os


# create a file for refine data 
# refine = open ("Refine_data.txt", "x")

if os.path.exists ("Refine_data.txt"):
    os.remove("Refine_data.txt")
else:
    print ("The file is not exist")
