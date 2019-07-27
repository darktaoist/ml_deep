"""
scipy에서 scikit-learn 알고리즘을 구현할때
많이 사용하는 모듈은 scipiy.sparse모듈이다.
이때 희소 행렬기능은 주요 기능중의 하나이다.
희소행렬(sparse matrix : 희박행렬) : 0을 많이 포함한 2차원 배열이다
"""
import numpy as np
from scipy import sparse

b1 = np.eye(4, dtype=int)

print("Numpy배열:\n{}".format(b1))

"""
sparse.csr_matrix()메소드는 0이 아닌 메소드만 저
"""

sparse_matrix = sparse.csr_matrix(b1)

print("Scripy의 CSR 행렬 : \n{}".format(sparse_matrix))

b2 = np.eye(5,k=-1, dtype=int)
print(b2)


"""
# CSR(Compressed Sparse Row) = CRS
"""
sparse_matrix_b2 = sparse.csr_matrix(b2)

print("Scipy CSR행렬 : \n{}".format(sparse_matrix_b2))

b3 = np.arange(16).reshape(4,4)

print(b3)
x = np.diag(b3)
print(x)

y = np.diag(np.diag(b3))
print("y:::\n{}".format(y))

sparse_matrix_b3 = sparse.csr_matrix(y)
print("Scipy CSR행렬 b3 : \n{}".format(sparse_matrix_b3))

"""
희소 행렬을 직접 만들때 사용하는 포맷
COO 포멧 (Coordinate 포맷) : 데이터가 놓이게될 위치
"""


data = np.ones(4)
print(data)

row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print(eye_coo)

