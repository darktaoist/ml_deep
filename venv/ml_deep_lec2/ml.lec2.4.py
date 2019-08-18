"""
XOR 게이트 진리표

x1        x2      y
---------------------
0          0        0
0           1       1
1           0       1
1           1       1

XOR 게이트는 배타적 논리합이라고 한다.
x1과 x2 중 어느 한쪽이 1일때만 1을 출력하는 논리회로

퍼셉트론으로는 XOR 게이트를 구현 할수 없다.

직선 하나로는 XOR 게이트의 출력을 구분할수 없다.(구분 불가능)
퍼셉트론(단층 퍼셉트론)은 직선 하나로 나눈 영역만 표현 할수 있다는
한계가 있다.

선형 : 직선의 영역을 선형 영역
비선형 : 곡선의 영역을 비선형 영역

"""


"""
 다층 퍼셉트론 (Multi Layer Perceptron)
 * 단층 페셉트론으로는 XOR게이트를 표현할수 없다. 
 즉, 단층 페셉트론으로는 비선형 영역을 분리할수 없다.
 
 기존 게이트(AND  OR  NAND)의 조합하여 층을 쌓으면 XOR 게이트를 구현할수 있게 된다.
 
 게이트를 조합한 XOR 게이트의 진리표
 
 x1     x2      s1(nand)    s2(or)      y(and)
 ----------------------------------------------
 0      0       1           0           0       
 0      1       1           1           1
 1      0       1           1           1   
 1      1       0           1           0
 
"""

import numpy as np

def AND(x1 , x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])  # 가중치
    b = 0.7                    # 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y



print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))


print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))


print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))


