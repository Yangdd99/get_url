import requests
import re
key_word = "六中全会"
url = "https://www.baidu.com"
key_word_url = []
finded_url = []
waitfind_url = [url]
differ_url = list(set(waitfind_url).difference(set(finded_url)))

while differ_url!=[]:
    for url in differ_url:
        try:
            finded_url.append(url)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
            url_html = requests.get(url,headers=headers)
            get_new_url = (re.findall('https?://\w+.baidu.com',url_html.text))
            new_url = list(set(get_new_url))
            waitfind_url=list(set(waitfind_url+new_url))
            if key_word in url_html.text:
            	key_word_url.append(url)
        except:
            pass
    differ_url = list(set(waitfind_url).difference(set(finded_url)))
    #print(differ_url)
print (key_word_url)#最后输出包含关键字的域名

