import os
import json
f = open('D:\caption_train_annotations_20170902.json')
data =json.load(f)
data_image_id = []
data_json_id = []
for json_data in data:
    data_json_id.append(json_data['image_id'])
n=0
# print(dddd)
fileName=[]
index = []
data_image_id_1000=[]
for filename in os.listdir(r"D:\搜狗高速下载\ai_challenger_caption_train_20170902\ai_challenger_caption_train_20170902\caption_train_images_20170902"):              #listdir的参数是文件夹的路径
   # print ( filename)
   index.append(data_json_id.index(filename))
   fileName.append(filename)
   n=n+1;
   if n==1000:
       break
# print(len(index))
# print(fileName)
# for i in range(0,1000):
#     data_image_id_1000.append(data[index[i]])
# # print(data_image_id_1000)
# write_json = json.dumps(data_image_id_1000)
# with open('d:/ai_challenge_picture_sample_1000/json_data.json','w') as json_file:
#     json_file.write(write_json)
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
# for filename in fileName:
#     lena = mpimg.imread("D:/搜狗高速下载/ai_challenger_caption_train_20170902/ai_challenger_caption_train_20170902/caption_train_images_20170902"+'/'+filename)
#     # plt.savefig('d:/ai_challenge_picture_sample_1000/picture/'+filename)//打印好的图像才能保存
#     np.save('d:/ai_challenge_picture_sample_1000/picture/'+filename,lena)
# plt.imshow(lena)  # 显示图片
# plt.axis('off')  # 不显示坐标轴
# plt.show()
import shutil
for filename in fileName:
    old_path = "D:/搜狗高速下载/ai_challenger_caption_train_20170902/ai_challenger_caption_train_20170902/caption_train_images_20170902/"+filename
    new_path = 'd:/ai_challenge_picture_sample_1000/picture1/'+filename
    shutil.copyfile(old_path,new_path)
