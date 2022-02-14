#  -*- coding:utf-8 -*-


# 9、 实现功能：输入任意一段字符串，提取这个字符串内的所有英文字母和数字，例：
# 9.     输入：我是ht传说中的tp一个://www快乐.baid的u.co程10序员m
# 10.  输出：httpwww.baidu.co10m
# 11.  输入：猿htt人q学s:/啦啦啦/德玛\t西\n亚
# 12.  输出：httqstn

text = input("输入:")
char_num_list = []
for value in text:
    if (value >= 'a' and value <= 'z') or (value >= 'A' and value <= 'Z') or value == ".":
        char_num_list.append(value)

char_num_str = "".join(char_num_list)
print(char_num_str)


