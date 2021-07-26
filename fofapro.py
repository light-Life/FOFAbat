# !/usr/bin/python
# -*- coding:utf-8 -*-
# author: huayang
# time: 2021.7.2-2021.7.3
import requests
import base64
import json
import time
import xlwt
import re

print("""\033[1;36m
 ______           __                       _______
|  ____|         / _|                      |   __ \\
| |__     ___   | |_    __ _               |  |__| |
|  __|   / _ \  |  _|  / _  |   ________   | _ ___/
| |     | (_) | | |   | (_| |  |________|  | |
|_|      \___/  |_|    \__,_|              |_|      ro

                        V:1.0          by:huayang                             
\033[0m""")

email = '1273292809@qq.com' #邮箱

key = '171746577425c1d2a11b654f8a8cfa1f' #key

query = base64.b64encode(input('查询语句:').encode('utf-8'))

query_sub = re.sub("[']",'',str(query))

size = '10000'

fields = 'host,title,ip,domain,port,country,province,city,country_name,header,server,protocol,banner,cert,isp,as_number,as_organization,latitude,longitude,icp'

api = 'https://fofa.so/api/v1/search/all?email=%s&key=%s&qbase64=%s&size=%s&fields=%s' % (email,key,query_sub[1:],size,fields)

#time
localtime = time.localtime(time.time())

time = time.strftime("%Y%m%d%H%M%S", time.localtime())

response = requests.get(api)

#print(response.text)

if 'make sure email and apikey is correct' in response.text:
    print('\n\033[1;31m[-] 请检查邮箱或key是否有误\033[0m')

elif 'query statement error' in response.text:
    print('\n\033[1;31m[-] 查询语句错误\033[0m')

elif 'request params not valid' in response.text:
    print("\n\033[1;31m[-] 请求参数无效\033[0m")

elif 'FOFA coin is not enough' in response.text:
    print("\n\033[1;31m[-] F币不足\033[0m")

elif 'Internal Server Error' in response.text:
    print("\n\033[1;31m[-] 服务器异常\033[0m")

elif 'limits must less than' in response.text:
    print("\n\033[1;31m[-] 请求数必须小于1个达不溜\033[0m")

else:
    res = json.loads((response.content).decode('utf-8'))

    print("""选择要扫描的类型：
    1 【导出纯地址.txt】
    2 【导出完整文件.xls】
    """)

    choice = input('请输入数字:')

    if choice == '1':
        for i in range(len(res["results"])):
            url = res["results"][i][0]
            if 'http' not in url:
                url = 'http://' + url
                try:
                    response = requests.get(url, verify=False, timeout=2)
                    print('\n\033[1;32m[+]正在写入:\033[0m', url)
                    with open(time + '.txt', 'a')as f:
                        f.write(str(url) + '\n')
                except:
                    pass
            else:
                try:
                    response = requests.get(url, verify=False, timeout=2)
                    print('\n\033[1;32m[+]正在写入:\033[0m', url)
                    with open(time + '.txt', 'a')as f:
                        f.write(str(url) + '\n')
                except:
                    pass

    elif choice == '2':
        global number  # 定义一个全局变量
        number = 1
        workbook = xlwt.Workbook(encoding='utf-8')  # 工作簿
        worksheet = workbook.add_sheet('FOFA数据')  # 工作表
        for i in range(len(res["results"])):
            host = res["results"][i][0] #主机
            title = res["results"][i][1] #标题
            ip = res["results"][i][2] #ip
            domain = res["results"][i][3] #域名
            port = res["results"][i][4] #端口
            country = res["results"][i][5] #国家
            province = res["results"][i][6] #省份
            city = res["results"][i][7] #城市
            country_name = res["results"][i][8] #国家名
            #header = res["results"][i][9] #头部
            server = res["results"][i][10] #服务器
            protocol = res["results"][i][11] #协议
            #banner = res["results"][i][12] #Banner
            #cert = res["results"][i][13] #证书
            isp = res["results"][i][14] #运营商
            as_number = res["results"][i][15] #AS号
            as_organization = res["results"][i][16] #AS组织
            latitude = res["results"][i][17] #纬度
            longitude = res["results"][i][18] #经度
            icp = res["results"][i][19] #ICP备案

            #print(host,title,ip,domain,port,country,province,city,country_name,header,server,protocol,banner,cert,isp,as_number,as_organization,latitude,longitude,icp)
            print('\n\033[1;32m[+]正在写入:\033[0m', host)

            # 设置单元格的宽度
            worksheet.col(0).width = 240 * 20
            worksheet.col(2).width = 320 * 20
            worksheet.col(3).width = 250 * 20
            worksheet.col(4).width = 800 * 20
            worksheet.col(6).width = 240 * 20
            worksheet.col(7).width = 280 * 20

             #创建颜色
            pattern = xlwt.Pattern()  # 创建模式对象
            pattern.pattern = xlwt.Pattern.SOLID_PATTERN
            pattern.pattern_fore_colour = 5  # 设置模式颜色
            style = xlwt.XFStyle()  # 创建样式对象
            style.pattern = pattern  # 将模式加入到样式对象

            # 写入内容
            worksheet.write(number, 0, ip)
            worksheet.write(number, 1, port)
            worksheet.write(number, 2, host)
            worksheet.write(number, 3, domain)
            worksheet.write(number, 4, title)
            worksheet.write(number, 5, protocol)
            worksheet.write(number, 6, server)
            worksheet.write(number, 7, icp)
            worksheet.write(number, 8, country_name)
            worksheet.write(number, 9, province)
            worksheet.write(number, 10, city)
            worksheet.write(number, 11, isp)
            worksheet.write(number, 12, country)
            worksheet.write(number, 13, as_number)
            worksheet.write(number, 14, as_organization)
            worksheet.write(number, 15, longitude)
            worksheet.write(number, 16, latitude)
            # worksheet.write(number, 17, header)
            # worksheet.write(number, 18, banner)
            # worksheet.write(number, 19, cert)
            number = number + 1

            # 写入头部数据
        worksheet.write(0, 0, 'IP', style)
        worksheet.write(0, 1, '端口', style)
        worksheet.write(0, 2, '主机', style)
        worksheet.write(0, 3, '域名', style)
        worksheet.write(0, 4, '标题', style)
        worksheet.write(0, 5, '协议', style)
        worksheet.write(0, 6, '服务器', style)
        worksheet.write(0, 7, 'ICP备案', style)
        worksheet.write(0, 8, '国家名', style)
        worksheet.write(0, 9, '省份', style)
        worksheet.write(0, 10, '城市', style)
        worksheet.write(0, 11, '运营商', style)
        worksheet.write(0, 12, '国家', style)
        worksheet.write(0, 13, 'AS号', style)
        worksheet.write(0, 14, 'AS组织', style)
        worksheet.write(0, 15, '经度', style)
        worksheet.write(0, 16, '纬度', style)
        # worksheet.write(0, 17, '纬度')
        # worksheet.write(0, 18, '经度')
        # worksheet.write(0, 19, 'ICP备案')
        # 保存文件
        workbook.save(time + '.xls')
    else:
        print('\033[1;31[-] 输入的参数有误\033[0m')

