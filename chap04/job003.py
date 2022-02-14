#  -*- coding:utf-8 -*-

# 有这样的一个字典：{'百度':‘www.baidu.com’, '搜狐':‘www.sohu.com’, '猿人学':‘www.yuanrenxue.com’, '这里是随机的':‘www. 这里是随机的.com’,}
# 将以上的字典内的网址全部提取，并放入列表中且在前面增加：http://，最后将这个列表打印出来。

web_info = {'百度': 'www.baidu.com', '搜狐':'www.sohu.com', '猿人学':'www.yuanrenxue.com', '这里是随机的':'www.这里是随机的.com',}

web_list = []
for value in web_info.values():
    web_list.append("http://" + value)

print(web_list)


# 12、有一个列表，列表内有几百个网址，请实现如下功能：
# 16.    去重，且不改变原来列表的顺序
# 17.  制作一个字典，字典的key自己定义，将列表中的网址放入逐一放入字典中 例：
# {‘第1个网址’:‘www.*****.com’, ‘第2个网址’:‘www.*****.com’, 后面省略}

a = ['http://www.baidu.com', 'http://www.sohu.com', 'http://www.yuanrenxue.com', 'http://www.这里是随机的.com', 'http://www.sohu.com', 'http://www.sohu.com', 'http://www.sohu.com']

web_set = set()
web_list = []
for web in a:
    if not web in web_set:
        web_list.append(web)
        web_set.add(web)

print(web_list)

web_map = {}
i = 1
for value in web_list:
    web_map["第{}个网址".format(i)] = value
    i = i + 1

print(web_map)

# 15、有一批爬虫请求日志数据，如下：
# 时间              请求成功   请求失败
# 2021-1-1 14:00     113         4
# 2021-1-1 16:00     156        3
# 2021-1-1 19:00     234        9
# 2021-1-2 10:00     156        16
# 2021-1-2 21:00     100        27
# 2021-1-5 09:00     112        38
# 2021-1-5 12:00     178        40
# 2021-1-6 18:00     269        36
# …………………………
#
# 要求：清洗这批，做好结构化，并输出：
#
# 1.     请求成功最多的那一天和成功次数
# 比如：2021-1-1 成功503次
#
# 2.     失败次数大于30次的时间段
# 比如：2021-1-5 09:00 失败38次
# 2021-1-5 12:00 失败40次
# 2021-1-6 18:00 失败36次

records = [
    { "date": "2021-1-1 14:00",  "success":   113, "fail":         4},
    {"date":"2021-1-1 16:00",   "success":  156  , "fail":      3},
    {"date":"2021-1-1 19:00", "success":    234 , "fail":       9},
    {"date":"2021-1-2 10:00",   "success": 156   , "fail":     16},
    {"date":"2021-1-2 21:00",  "success":   1000  , "fail":      27},
    {"date":"2021-1-5 09:00", "success":    112  , "fail":      38},
    {"date":"2021-1-5 12:00",  "success":   178  , "fail":      40},
    {"date":"2021-1-6 18:00",   "success":  269  , "fail":      36}
]

max_success = 0
max_success_record = {}
for record in records:
    if record["success"] > max_success:
        max_success = record["success"]
        max_success_record = record

print(max_success_record)

fail_list = []
for record in records:
    if record["fail"] > 30:
        fail_list.append("{}失败{}次".format(record["date"], record["fail"]))

print(fail_list)