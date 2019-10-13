import os

for maindir, subdir, file_name_list in os.walk("./chapter"):
    t_list = file_name_list

t_list.sort()

for name in t_list:
    print("* ["+name.split(".")[0]+"](chapter/"+name+")")