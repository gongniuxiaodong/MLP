import  os
import json
import time
f = open(r'd:/ai_challenge_picture_sample_1000/json_data.json')
data=json.load(f)

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
start = time.time()
pic=[]
print(len(data))
for i in range(0,len(data)-1):
    pic.append(np.load('d:/ai_challenge_picture_sample_1000/picture/'+data[i]['image_id']+'.npy'))
# plt.imshow(pic)
# plt.show()
end = time.time()
print(end-start)
