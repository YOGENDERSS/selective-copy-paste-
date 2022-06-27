import os
import shutil
import pathlib

src_dir = '/home/prekshak/Desktop/new_annotation/images/test' 
dst_dir = '/home/prekshak/Desktop/new_annotation/common/test/images'

n = sorted(os.listdir(src_dir))

files_list = sorted(n, key=lambda x: int(os.path.splitext(x)[0]))

t = range(0, len(files_list),25)

for order in t:
	print(order)
	files = files_list[order] # getting 1 image after 25 images
	print(files)
	shutil.copyfile(os.path.join(src_dir, files), os.path.join(dst_dir, files))  # copying images to destination folder