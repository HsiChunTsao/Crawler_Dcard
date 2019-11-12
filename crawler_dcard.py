import requests 
from bs4 import BeautifulSoup
import re
import urllib.request
from urllib.request import urlretrieve
import os
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

print('1：美妝版 2：穿搭版 3：網購版 4：感情版 5：心情版 6：閒聊版 7：女孩版\n8：有趣版 9：彩虹版 10：追星版 11：攝影版 12：美食版 13：旅遊版 14：動漫板')
a = input('請輸入要抓取的看板(不輸入即為全部文章,校版請輸入校名縮寫)：')
board = 'f'
if a=='1':
    board = 'f/makeup'
elif a=='2':
    board = 'f/dressup'
elif a=='3':
    board = 'f/buyonline'
elif a=='4':
    board = 'f/relationship'
elif a=='5':
    board = 'f/mood'
elif a=='6':
    board = 'f/talk'
elif a=='7':
    board = 'f/girl'
elif a=='8':
    board = 'f/funny'
elif a=='9':
    board = 'f/rainbow'
elif a=='10':
    board = 'f/entertainer'
elif a=='11':
    board = 'f/photography'
elif a=='12':
    board = 'f/food'
elif a=='13':
    board = 'f/travel'
elif a=='14':
    board = 'f/acg'
else:
    board = 'f/'+a

times = input("請輸入要抓取前幾篇熱門文章的圖片(至多30篇):")
int(times)


if not os.path.isdir('download'):
    os.mkdir('download')
url = 'https://www.dcard.tw/'+board
reg_imgur_file  = re.compile('http[s]://imgur.dcard.tw/\w+\.(?:jpg|png|gif)')
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
articles = soup.select('div.PostEntry_content_g2afg h3')
articles2 =  soup.select('div.PostList_wrapper_2BLUM a')
x = 0
for art in articles[:int(times)]:
    art2 = articles2[x]
    if not os.path.isdir(os.path.join('download',art.text)):
        os.mkdir(os.path.join('download',art.text))
    print(art.text)
    print('https://www.dcard.tw'+art2['href'])
    res = requests.get('https://www.dcard.tw'+art2['href'])
    images = reg_imgur_file.findall(res.text)
    print(images)
    for image in set(images):
            ID = re.search('http[s]://imgur.dcard.tw/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,os.path.join('download',art.text,ID))
    x = x+1
input('\n完成！')


