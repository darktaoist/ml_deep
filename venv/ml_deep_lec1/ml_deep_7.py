"""
    sparse : scipy에 있는 모듈 , 희소행렬(sparse matrix) 제공
    numpy : ones(10) , zeros
"""

import numpy as np

b1 = np.ones((5,5))
print(b1)

b2 = np.zeros(10)
print(b2)

b3 = np.zeros((6,4))
print(b3)

"""
numpy에서 특수행렬을 만드는 함수
eye(N= M=, K= dtype) : N=행 , M:열수 , K:대각의위치    
 --> 항등행렬을 만드는 함수
 --> 대각선의 값이 1인 함수
 --> 여기서 N은 행수의수룰 , M은 열의수 , K는 대각의 위치 , dtype은 자료형
"""

print(np.eye(3, dtype=int))  #k 대각의 위치를 바꾸는 파람
print(np.eye(4,dtype=int))
print(np.eye(4,k=1, dtype=int))

print(np.eye(4, M=3, dtype=int))

print(np.eye(4, M=5, k=1 , dtype=int))
print(np.eye(5,dtype=int))

"""
    diag함수는 정방행렬에서 대각 요소만 추출하여 벡터를 만드는 함수
    diag(v , k= ,
    diag()함수는 반대로 벡터 요소를 대각 요소로 하는 정방행렬을 만들기도 한다.     
"""

x = np.eye(5,dtype=int)
print(x)
print(np.diag(x))

x = np.arange(9).reshape(3,3)
print(x)
print(np.diag(x))
print(np.diag(x, k=1))

print(np.eye(5,k=-1,dtype=int))
print(np.eye(5,k=-2, dtype=int))