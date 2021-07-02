import requests
import time
import re
import base64

with open('url.txt', 'w')as f: #用于清空文件
    f.write('')

grammar = input('查询语法:')

grammars = grammar.encode("utf-8")

grammars_base64 = base64.b64encode(grammars)

grammars_sub = re.sub("[']",'',str(grammars_base64))#过滤编码后的 b ' =

for number in range(int(input('起：')),int(input('始：'))):

    url = 'https://fofa.so/result?page=' + str(number) + '&qbase64=' + str(grammars_sub[1:])
    print('\n》》》》》》》》》第',number,'页《《《《《《《《《\n')
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cookie': 'Hm_lvt_9490413c5eebdadf757c2be2c816aedf=1615897374,1615997473,1616165617,1616482234; Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1621734679,1622122706,1622299647,1622305482; refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6Njg2MTYsIm1pZCI6MTAwMDQzNTg4LCJ1c2VybmFtZSI6IuWNjuaJrCIsImV4cCI6MTYyMjY4NDAwOCwiaXNzIjoicmVmcmVzaCJ9.EeHHTLi1iRhyAFsGpAC6KphSdUkaCXoX6ql7jg1d9QbkZ7o02b2jWtDYGhuTRrPjzwxYNIeR-U9owMran6g4zg; befor_router=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6Njg2MTYsIm1pZCI6MTAwMDQzNTg4LCJ1c2VybmFtZSI6IuWNjuaJrCIsImV4cCI6MTYyMjU1Mzk2MS4xNjQ2NTMsImlzcyI6InJlZnJlc2gifQ.sgiLW8ZEqKUB2rfwLx5dKeePWIu8YXvoMjfphWuwVkhyiRZKcEU2nsPtJE_OO92TqzQ6l5Gr6hy9wJe6FG-bzA; user=%7B%22id%22%3A68616%2C%22mid%22%3A100043588%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22%E5%8D%8E%E6%89%AC%22%2C%22nickname%22%3A%22%22%2C%22email%22%3A%221273292809%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fi.nosec.org%2Favatar%2Fsystem%2Fusers%2Favatars%2F100%2F043%2F588%2Fmedium%2F1615704959825.jpg%3F1615705338%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fi.nosec.org%2Favatar%2Fsystem%2Fusers%2Favatars%2F100%2F043%2F588%2Fthumb%2F1615704959825.jpg%3F1615705338%22%2C%22key%22%3A%223ee0e6c9ded5a46d78b1314cdb0e5010%22%2C%22rank_name%22%3A%22%E6%99%AE%E9%80%9A%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A1%2C%22company_name%22%3A%22%22%2C%22coins%22%3A0%2C%22credits%22%3A5266%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1622511650'
    }

    time.sleep(2)

    response = requests.get(url,headers=headers)

    position_list = re.findall('.*?<a href="(.*?)" target="_blank">',response.text)

    for i in position_list:
        try:
            response = requests.get(i,verify=False,timeout=2)

            if response.status_code == 200:
                print('[+] 正在写入：', i)
                with open('url.txt', 'a')as f:
                    f.write(str(i) + '\n')
        except OSError:
            pass
        continue








