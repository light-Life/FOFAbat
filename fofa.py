# !/usr/bin/python
# -*- coding:utf-8 -*-
# author: huayang
# time: 2021.7.2-2021.7.3
import requests
import time
import re
import base64

print("""\033[1;36m.
  `   ______    / . . __     `  . `。
   ` |  ____|    .   / _|     . `   `
    `| |__    .___   | |_    __ _ `
    `|  __|   / _ \  |  _|  / _  |`.
   ` | |   . | (_) | | |   | (_| |`
   ` |_|    ` \___/  |_|    \__,_|`
.`    . .         
              by:huayang                             
\033[0m""")

with open('url.txt', 'w')as f: 
    f.write('')

grammar = input('查询语法:')

grammars = grammar.encode("utf-8")

grammars_base64 = base64.b64encode(grammars)

grammars_sub = re.sub("[']",'',str(grammars_base64))

for number in range(int(input('起：')),int(input('始：'))):

    url = 'https://fofa.so/result?page=' + str(number) + '&qbase64=' + str(grammars_sub[1:])
    print('\n》》》》》》》》》第',number,'页《《《《《《《《《\n')
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cookie': '' #记得写cookie
    }

    time.sleep(2)

    response = requests.get(url,headers=headers)

    position_list = re.findall('.*?<a href="(.*?)" target="_blank">',response.text)

    for i in position_list:
        try:
            response = requests.get(i,verify=False,timeout=2)

            if response.status_code == 200:
                print('\n\033[1;32m[+]正在写入:\033[0m', i)
                with open('url.txt', 'a')as f:
                    f.write(str(i) + '\n')
        except OSError:
            pass
        continue
