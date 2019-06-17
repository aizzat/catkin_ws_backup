# move files from one directory to another
# if files alrady exist there, they will be overwritten
# retains original file date/time
import os
import shutil
# make sure that these directories exist
root_src_dir = "/home/irovlab/catkin_ws"
root_target_dir = "/media/irovlab/New Volume/insync/UMP TEACHING/SUBJEK (NEW)/BFM4523 - Autonomous Robotic System/catkin_ws"


operation = 'copy'  # 'copy' or 'move'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_target_dir)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        if operation is 'copy':
            shutil.copy(src_file, dst_dir)
        elif operation is 'move':
            shutil.move(src_file, dst_dir)