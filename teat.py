import pprint
import random
import time

import requests
import re
import parser

# r=requests.get("http://www.baidu.com")
# print(r.text)


# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36




def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False



headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'
    ,'Cookie':'PHPSESSID=sll5np1m5uoh5hqi2cn31qtgi3; _pk_id.10.8d30=78c1d06ffd38995c.1617857679.1.1617860095.1617857679.; _pk_ses.10.8d30=1; nav_switch=booklist'
}

r = requests.get('https://18cute.fun/topic/4', headers=headers)
rs = requests.get('https://18cute.fun/chapter/536', headers=headers)
# rs=requests.get('//t.cdn.ink/image/2020/01/2020020916481695-scaled.jpeg',headers=headers)


# print(r.request.haders)
# print(rs.text)
# print(r.text)

html = r.text



# <div class="mh-item"><a href="/comic/536" title="[ 惡犬小姊姊 ] Fishnet Socks - (39P)">
urls = re.findall('<a href="(.*?)" title=".*?" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">', html)

print(urls)



for url in urls:
    time.sleep(random.random() * 3)
    uurl = url.split('/')[-1]
    print(uurl)

    url_data = requests.get('https://18cute.fun/chapter/' + uurl, headers=headers).text

    print('https://18cute.fun/chapter/' + uurl)
    # print(url_data)

    # < imgclass ="lazy" data-original="https://img.viptoon.cc/static/upload/book/1091/32568/f19e40fb3c99fa23587b78455cbe5f52.jpg" src="/static/images/loading.jpg" >

    jpg_url=re.findall('<img class="lazy" data-original="(.*?)" ',url_data)
    jap_name=re.findall('<a class="comic-name" href=".*?" title=".*?">(.*?)</a>',url_data)
    print(jpg_url)
    print(jap_name)

    if jap_name:
        mkdir('img//'+jap_name[0])
        print(f'========{jap_name[0]}=========')
        for jpg in jpg_url:
            jpg_data=requests.get(jpg,headers=headers)



            # 数据保存

            file_name = jpg.split('/')[-1]

            with open(f'img//{jap_name[0]}//' + file_name, mode='wb') as f:
                f.write(jpg_data.content)
                print('保存成功'+file_name)
