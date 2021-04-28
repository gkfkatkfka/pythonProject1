import csv

#파일 선택
f = open('./경기일정.csv', 'r', encoding='cp949')

# csv 파일 하나를 읽어옴
information = csv.reader(f)

# 한 줄씩 읽어와서 정보를 가지고 옴
for info in information:
    print(info)
    place=info[5]
    date=info[1]+"."+info[2]
    time=info[3][0:2]
    print(date[0:4]+date[5:7]+date[8:10],place,time)

# 닫아줌
f.close() 