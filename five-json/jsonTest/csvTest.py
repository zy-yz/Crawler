# encoding =utf-8

import csv

def write_csv_demo1():
    headers = ['username','age','height']
    values = [
        ('张三',18,189),
        ('李四',33,333),
        ('王五',44,444)
    ]

    with open('classroom.csv','w', encoding='utf-8',newline='')as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

def write_csv_demo2():
    headers = ['username','age','height']
    values = [
        ('张三',18,189),
        ('李四',33,333),
        ('王五',44,444)
    ]

    with open('classroom.csv','w', encoding='utf-8',newline='')as fp:
        writer = csv.DictWriter(fp,headers)
        # 写入投数据的时候，需要调用uriteheaders方法
        writer.writeheader()
        writer.writerows(values)


if __name__ == '__main__':
    write_csv_demo2()
