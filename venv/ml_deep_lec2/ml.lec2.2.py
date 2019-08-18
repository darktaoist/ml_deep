import numpy as np

def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5,0.8
    tmp =  w1*x1 + w2*x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

"""
 ㄱㅏ중치와 편향을 도입한 퍼셉트론 식
 * 퍼셉트론 식에서 0(세타)를 -b로 치환하면
     0   w1*x1 + w2*x2 <= -b   ==>     0   b+w1*x1 + w2*x2 <= 0
y  =                                y = 
     1  w1*x1 + w2*x2 > -b      ==>    1  b+w1*x1 + w2*x2 > 0
     
이때 b(bias)를 편향이라고 한다.
퍼셉트론은 입력신호에 가중치를 곱한값과 편향을 합하여 그 값이 
0을 넘으면 1을 출력하고 그렇지 않으면 0을 출력한다.

XOR게이트 진리표
"""