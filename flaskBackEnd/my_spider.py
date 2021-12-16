import requests
import re
requests.packages.urllib3.disable_warnings()   #key code 
requests.adapters.DEFAULT_RETRIES = 5 #key code 
import os
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
import imghdr
from tensorflow import keras
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
import shutil
import csv
from requests.sessions import session
import time

t="百度:萨摩耶"
img_size = (180, 180)


# def spider_save(s):
#     # model = MobileNetV2(weights='imagenet')
#     Sample = Image.open(BytesIO(s)).resize((180, 180))
#     # Sample = Image.frombytes(mode='RGB', size=(180, 180), data=s)
#     # print(help())
#     plt.imshow(Sample)

# def pic_save(img,result):
#     with open("global_total.txt",'r') as f:
#         s_temp=f.read()
#     #pic_dir="./uploads/"+result
#     pic_dir="album/"+result
#     if(not os.path.exists(pic_dir)):
#         os.mkdir(pic_dir)
    
#     pic_path=pic_dir+"/"+s_temp.replace('/n','')+'.jpg'
#     img.save(pic_path)

#     with open("global_total.txt",'w') as f:
#         f.write(str(int(s_temp)+1))

def spider_calssify():
    img_path = "/home/ubuntu/code/load_img_test/raw"
    model = MobileNetV2(weights='imagenet')
    i = 0

    for fname in os.listdir(img_path):
        img = tf.keras.preprocessing.image.load_img(os.path.join(img_path, fname), color_mode='rgb').resize((224, 224))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array, mode='tf')
        

        preds = model.predict(img_array)
        pred_proba = "{:.3f}".format(np.amax(preds))    
        pred_class = decode_predictions(preds, top=1)
        result = str(pred_class[0][0][1]).replace('_', ' ')

        fpath = "/var/www/html/photo/pic_find/" + result
        with open("global_total.txt",'r') as f:
            s_temp=f.read()

        if not os.path.exists(fpath):
            os.mkdir(fpath)
        img.save(fpath + '/' + result + s_temp + ".jpeg")
        with open("global_total.txt",'w') as f:
            f.write(str(int(s_temp)+1))


        print((pred_proba, result), fname)


def spider_fun(s):
    s=s.split(":")
    web_select=s[0]
    key_word=s[1]
    if web_select=='百度':
        spider_baidu(key_word)
    elif web_select=='微博':
        spider_weibo(key_word)





def spider_baidu(s):
    key_word=s
    if not os.path.exists(f'./{key_word}'):
        os.mkdir(f'./{key_word}')

    url = f'https://m.baidu.com/sf/vsearch?pd=image_content&word={key_word}&tn=vsearch&atn=page'
    # url = 'https://img1.baidu.com/it/u=3738836484,3055850216&fm=26&fmt=auto&gp=0.jpg'
    s = requests.session()
    s.keep_alive = False #key code
    resp = s.get(url)

    obj0 = re.compile(r'https://img0.baidu.com/it/(?P<key>.*?)&fmt=auto&gp=0.jpg',re.S)
    obj1 = re.compile(r'https://img1.baidu.com/it/(?P<key>.*?)&fmt=auto&gp=0.jpg',re.S)
    obj2 = re.compile(r'https://img2.baidu.com/it/(?P<key>.*?)&fmt=auto&gp=0.jpg',re.S)
    result_0 = obj0.finditer(resp.text)
    result_1 = obj1.finditer(resp.text)
    result_2 = obj2.finditer(resp.text)

    urls = []
    for it in result_0:
        key = it.group('key')
        key = f'https://img0.baidu.com/it/{key}&fmt=auto&gp=0.jpg'
        urls.append(key)
    for it in result_1:
        key = it.group('key')
        key = f'https://img0.baidu.com/it/{key}&fmt=auto&gp=0.jpg'
        urls.append(key)
    for it in result_2:
        key = it.group('key')
        key = f'https://img0.baidu.com/it/{key}&fmt=auto&gp=0.jpg'
        urls.append(key)
    count = 1 

    shutil.rmtree('/home/ubuntu/code/load_img_test/raw')
    os.mkdir('/home/ubuntu/code/load_img_test/raw')
    #update pic buffer
    for key_url in urls:
        resp = s.get(key_url)
        data=resp.content
        # spider_save(data)
        img_type=imghdr.what(None,data)
        if(img_type!=None):
            img_name = f"{count}" +'.'+img_type
            count += 1
            img_path = "/home/ubuntu/code/load_img_test/raw/" + img_name
            print(img_path)
            with open(img_path,'wb') as fp:
                fp.write(resp.content)
                print(f"{img_name}已完成")

    spider_calssify()
    print("关键词为"+key_word+"的百度图片爬取完毕！")



def spider_weibo(s):

    weibo_id=4636276756316984


    headers = {
        'Cookie' : '_T_WM=14627810303; WEIBOCN_FROM=1110006030; SCF=Aq3As3Vqs1tScI51tNV_vTaUKDUcWxN_zvxPdN_JS7t3h1GMEsyhpUuHMEQ_RGxm5EzTUDqxloMRQ8PmOpgMM20.; SUB=_2A25Nsy5HDeRhGeFI6lsW8i7Pwz6IHXVvX7IPrDV6PUJbktB-LRTEkW1NfVw6WYgoL0lJvTAPIb7WbsujvgzDkJJ8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhsgRGZDgHFL4IV7F_LkdqO5JpX5KzhUgL.FoMceK.Neo501hz2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSo24S0z7e0nE; SSOLoginState=1622629911; ALF=1625221911; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4635403158556543%26luicode%3D20000061%26lfid%3D4635403158556543%26uicode%3D20000061%26fid%3D4635403158556543; XSRF-TOKEN=8c25cf',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Referer': 'https://m.weibo.cn/detail/4635403158556543',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN' : '5c0faa',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'MWeibo-Pwa': '1'
    }
    f = open("微博评论.csv",mode ='w',encoding='utf-8')
    csvwriter = csv.writer(f)
    #打开csv文件
    csvwriter.writerow(['id','comment','data_time'])


    url = "https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0".format(weibo_id,weibo_id)
    session = requests.Session()
    resp = session.get(url, headers=headers)
    dict = resp.json()


    max_id_type =  dict['data']['max_id_type']
    max_id = dict['data']['max_id']
    print("now max_id="+str(max_id))
    flag_ok=dict['ok']
    print(flag_ok)
    flag_time=0
    while(flag_ok==1 and max_id!=0):
        url = "https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type={}".format(weibo_id,weibo_id,max_id,max_id_type)
        resp = session.get(url,headers=headers)
        dict = resp.json()
        flag_time= flag_time+1
        if(flag_time==10):
            flag_time=0
            #time.sleep(2)
            #print("Now relax for 2s to avoid 反扒机制")
        flag_ok=dict['ok']
        print("now max_id="+str(max_id))
        '''
        if(flag_ok==1):
            max_id = dict['data']['max_id']
            max_id_type =  dict['data']['max_id_type']

            for j in range(len(dict['data']['data'])):
                comment = dict['data']['data'][j]['text']
                reg = re.compile('<[^>]*>')
                comment = reg.sub('',comment).replace('\n','').replace(' ','')#过滤掉html标签内容
                name = dict['data']['data'][j]['user']['screen_name']  
                wb_time=dict['data']['data'][j]['created_at']
                csvwriter.writerow([name,comment,wb_time])
        '''
    print("关键词为"+s+"的微博图片爬取完毕！")

if __name__ == '__main__':
    spider_fun(t)

