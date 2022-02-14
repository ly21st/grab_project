# -*- coding: utf-8 -*-

data = [
                {"id":1,"name":"四川省","code":"0001","pid":0},
                {"id":2,"name":"成都市","code":"0002","pid":1},
                {"id":3,"name":"绵阳市","code":"0003","pid":1},
                {"id":4,"name":"高新区","code":"0004","pid":2},
                {"id":5,"name":"双流区","code":"0005","pid":2}
        ]

data2 = [
    {"id": 1, "name": "四川省", "code": "0001", "children": [
        {"id": 2, "name": "成都市", "code": "0002", "pid": 1, "children": [
            {"id": 4, "name": "高新区", "code": "0004", "pid": 2, "children": []},
            {"id": 5, "name": "双流区", "code": "0005", "pid": 2, "children": []}
        ]},
        {"id": 3, "name": "绵阳市", "code": "0003", "pid": 1, "children": []},
    ]}
]

id_map = {}
for value in data:
    id_map[value["id"]] = value
    value["children"] = []

print(id_map)

data3 = [
    id_map[1]
]
print("-"*30)

id_map[2]["children"].append(id_map[4])
id_map[2]["children"].append(id_map[5])

del(data3[0]["pid"])
data3[0]["children"].append(id_map[2])
data3[0]["children"].append(id_map[3])

import pprint
pprint.pprint(data3)


print('-' * 30)
print(id_map)
