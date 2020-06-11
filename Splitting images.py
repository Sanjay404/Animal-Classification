import os.path
from os import path
import glob
import shutil
import random
update_dir = '/home/srikumar/Downloads/animals/data' #RAN ON UBUNTU
if not(path.exists(os.path.join(update_dir,'sorted'))): #makes sorted folder 
    os.mkdir(os.path.join(update_dir,'sorted'))
  #Splits up images into categorized directories
for image in os.listdir(os.path.join(update_dir)):
    if not('_img_' in image):
        continue
    animal = image.split("_img_")[0]
    target_dir = os.path.join(update_dir,'sorted',animal)
    if not os.path.isdir(target_dir):
      os.mkdir(target_dir)
    if not path.exists(os.path.join(target_dir, image)): #if image hasnt been copied over
      shutil.copy(os.path.join(update_dir,image), os.path.join(target_dir,image))  
print('A done!') 


test = 0.2
update_dir = '/home/srikumar/Downloads/animals' #RAN ON UBUNTU
if not(path.exists(os.path.join(update_dir,'training'))): 
    os.mkdir(os.path.join(update_dir,'training'))
if not(path.exists(os.path.join(update_dir,'testing'))): 
    os.mkdir(os.path.join(update_dir,'testing'))

for folder in os.listdir(os.path.join(update_dir,'data', 'sorted')):
    dir_list = os.listdir(os.path.join(update_dir, 'data', 'sorted', folder))
    random.shuffle(dir_list)
    for image in dir_list:
        r = random.random()
        if r <= test:
            shutil.copy(os.path.join(update_dir,'data','sorted', folder, image), os.path.join(update_dir,'training', image))
        else:
            shutil.copy(os.path.join(update_dir,'data','sorted', folder, image), os.path.join(update_dir,'testing', image))
print('done!!!')
