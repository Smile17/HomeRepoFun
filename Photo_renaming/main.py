# import required module
import os
import shutil

# assign directory
directory = 'input'
dest_directory = 'output'

# iterate over files in
# that directory
old_names = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        old_names.append(filename)

old_names = [x for x in old_names if not("thumb" in x)]
print(old_names)

for i, filename in enumerate(old_names):
    f_old = os.path.join(directory, filename)
    name = filename.split('@')[1]
    ext = name.split('.')[-1]
    date_name = name.split('_')[0]
    m, d, y = date_name.split('-')
    f_new = os.path.join(dest_directory, y + "_" + m + "_" + d)
    f = f_new + "." + ext
    check_file = os.path.isfile(f)
    if not check_file:
        os.rename(f_old, f)
    else:
        while True:
            i = 1
            f = f_new + "0" + i + "." + ext
            check_file = os.path.isfile(f)
            if not check_file:
                #shutil.copy(f_old, f)
                os.rename(f_old, f)
                break
