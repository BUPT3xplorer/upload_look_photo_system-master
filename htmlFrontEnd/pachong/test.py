'''
Author: your name
Date: 2021-07-07 01:40:06
LastEditTime: 2021-07-09 15:19:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \WWW\pachong\test.py
'''
import requests
from lxml import etree
import os
requests.packages.urllib3.disable_warnings()   #key code 
requests.adapters.DEFAULT_RETRIES = 5 #key code 
if __name__ == "__main__":
    
    headers = {
     'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'
     }
    #爬取到页面源码数据
    s = []
    s.append('')
    for i in range(2,22):
        s.append(f'_{i}')
    count = 1;
    n = len(s)
    k = requests.session() #key code  
    k.keep_alive = False #key code 
    for i in range(1,n):
        url = f"https://pic.netbian.com/4kdongwu/index{s[i]}.html"
        response = k.get(url = url, headers = headers)
        #手动设置响应数据的编码格式
        response.encoding=response.apparent_encoding
        page_text = response.text
        
        #数据解析：src的属性值，alt标签
        tree = etree.HTML(page_text)
        #存储的就是li标签
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        #创建一个文件夹
        if not os.path.exists('./piclibs_3'):
            os.mkdir('./piclibs_3')
        for li in li_list:
            #局部解析
            img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
            img_name = f"{count}"+'.jpg'
            count += 1
            #通用处理中文乱码的解决方案
        # imag_name = img_name.encoding('iso-8859-1').decode('gbk')
            
            img_data = k.get(url = img_src,headers=headers).content
            img_path = 'piclibs_3/' + img_name
            

            print(img_name,'下载成功！')

    