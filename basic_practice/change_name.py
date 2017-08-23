import os
import shutil

path=['/home/sj/google-images-download/running/','/home/sj/google-images-download/crawling/','/home/sj/google-images-download/soldier/','/home/sj/google-images-download/soldiers/','/home/sj/google-images-download/standing/']     
dest_path='/home/sj/google-images-download/train/'
ori_path='/home/sj/google-images-download/'

if not os.path.exists(dest_path):
    os.makedirs(dest_path, 0755)

num=0
for lists in path:
    filenames=os.listdir(lists) 
    
    for filename in filenames:
        if filename[-4:]==".jpg":
                    
            os.rename(lists+filename, "%05i.jpg" %num)

            shutil.move(ori_path + '%05i.jpg' %num, dest_path + '%05i.jpg' %num)
            num=num+1
