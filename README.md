# 项目介绍

此脚本分为两个版本  
分别是对应普通会员的爬虫版本fofa.py,以及对应高级会员的api版本fofapro.py  
当然普通会员也是可以使用fofapro.py

## fofapro.py

采用了fofa的api
实现了如下功能  
1 【导出纯地址.txt】  
2 【导出完整文件.xls】  

## fofa.py
采用了爬虫的形式进行爬取
批量的福音  

## 注意📢

需要使用的库

```
import requests
import base64
import json
import time
import xlwt
import re
```
记得添加邮箱、key或是cookie哈

## 其他
代码注释已经给得很清楚了，根据自己的口味随时调整

未来有时间会增加一键排除垃圾信息

如果师傅们还有什么需要添加的或是建议记得在Github或是博客给我里留言哦

师傅们看我这么用心给个Star✩不过分吧*ଘ(੭*ˊᵕˋ)੭* ੈ✩‧₊˚

[文章地址](https://hellohy.top/huayang/6815.html).

## 2021.7.5
优化xls排版问题

## 2021.7.26
优化判断

## 2022.1.29
更新api地址可以正常使用

## 2022.3.8
针对老哥提出的问题已给修复方案<br>
1.修改匹配方式<br>
2.删除功能二<br>
3.一些其他修改，见Commits
详情请见issues

## 2022.4.3
等我一个月兄弟们，我用golang再重写一次这个项目，实在用不起就看看别的，不用再给我发邮件了，最近实在很忙
