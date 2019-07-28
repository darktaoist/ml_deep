"""
matplotlib : 과학 계산용 그래프 라이브러리
(선그래프, 히스토그램 , 산점도 등을 지원)

그래프를 그리기 위해서는 matplotlib의 pyplot모듈을 이용한다.
"""

import numpy as np
import matplotlib.pyplot as plt

print(np.arange(0,6,0.1))

"""
데이터를 준비
"""

#그래프 그리기
x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
#plt.show()

"""
-------------------------------------------------------------
"""

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--", label="cos")
plt.title("sin and cos function")
plt.xlabel("x축")
plt.ylabel("y축")
plt.legend()   # 범
plt.show()

