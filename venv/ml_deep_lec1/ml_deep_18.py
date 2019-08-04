"""
# 1만명의 데이터 만들기(CSV 파일)
# BMI (Body Mass Index(체질량지수)) 데이터 만들기
"""

import random

def bmi_func(height, weight):
    bmi = weight / ((height/100)**2)
    if bmi < 18.5 : return "저체중"
    if bmi < 25 : return "정상"
    return "비만"

fp = open("d://works/bmi.csv" , "w" , encoding="utf-8")
fp.write("height , weight , label\r\n")

# 데이터 생성하기
cnt = {"저체중":0 , "정상":0 , "비만":0}


# 난수 테스트
print(random.randint(1,5))

for i in range(10000):
    h = random.randint(120,200)
    w = random.randint(35,90)
    label = bmi_func(h,w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h,w,label))

fp.close()
print("ok" , cnt)
