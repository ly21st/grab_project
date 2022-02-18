# -*- coding:utf-8 -*-

import csv
path = r"E:\liyuan-gitee\grab_project\chap07\eggs.csv"
with open(path, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    a = ['Spam'] * 5 + ['Baked Beans']
    print(a)
    spamwriter.writerow(a)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


print('-'*30)
import csv
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

print('-'*30)

name_path = r"E:\liyuan-gitee\grab_project\chap07\names.csv"

with open(name_path, 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open(name_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

print(row)

######csv参考资料
######https://docs.python.org/3/library/csv.html


