import os
import shutil

imagenumber = 0
pics_dir = 'myfootage'
pics_dir_proper = "..\\" + pics_dir
new_dir = "..\\timelapsefootage\\"
outputname = '..\\timelapse.mp4'

cmd = "mkdir ..\\timelapsefootage" 
os.system(cmd)
for filename in os.listdir(pics_dir_proper):
