import requests
import re
finded_url = []#已经查找过的域名
waitfind_url = ["https://www.baidu.com"]#待查找的域名
differ_url = list(set(waitfind_url).difference(set(finded_url)))#对比已查找过的域名中待查找中新增加的域名

while differ_url!=[]:
    for url in differ_url:
        try:
            finded_url.append(url)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
            url_html = requests.get(url,headers=headers)
            get_new_url = (re.findall('https?://\w+.baidu.com',url_html.text))
            new_url = list(set(get_new_url))
            waitfind_url=list(set(waitfind_url+new_url))
            urlfinded_dic = {url:new_url}
            #print (f"{urlfinded_dic}\n")#每个域名下包含的域名的字典
        except:
            pass
    differ_url = list(set(waitfind_url).difference(set(finded_url)))
    print(differ_url)#每一级所有域名查找后新增加的待查找域名
#print(waitfind_url)
#print(finded_url)#最后输出所有查找过的域名