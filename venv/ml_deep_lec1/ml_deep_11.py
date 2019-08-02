"""
훈련데이타
테스트데이타
train_test_split
대문자 X : Data
소문자 y : label
유사난수 생성기 , random_state = 0
"""

"""
scikitLearn의 붓꽃 데이터 셋을 가져오기
"""

from sklearn.datasets import load_iris

irisData = load_iris()
"""
#load_iris()함수가 리턴하는 객체는 Bunch클래스 객체
#Bunch클래스 객체는 파이썬의 Dictionary와 유사한 객체로
#키와 값으로 구성되어 있다.

훈련데이터와 테스트데이로를 나누기 위한 함수
train_test_split모듈에 있는 train_test_split()
train_test_split모듈은 sklean.model_selection 패키지에 존재
"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =  train_test_split(irisData['data'], irisData['target'],random_state=0)

# train_test_split()의 리턴 타입은 모두 numpy배열이다.

print(X_train.shape)
print(X_test.shape)
print(y_test)

"""
#KNN(머신러닝 분류머신 모델중의 하나) : K-Nearest 1   ₩                                   ㅂ) : K-최근접 알고리즘 : 분류기
사용하기 쉬운 분류 알고리즘 중의 하나임
K의 의미는 가장 가까운 이웃 하나를 의미하느것이 아니라,
훈련데이터에서 새로운 데이터에 가장 가까운 K개의 이웃을 찾는다는 의미이다.(세개 혹은 다섯개의 이웃)

KNN을 사용하기 위해서는 Neighbors 모듈에 KNeighborsClassfier라는 함수를 사용한다.
KNeighborsClassfier()함수중에 중요한 매개변수는 n_neighbors
이 매개변수는 이웃으 개수를 지정하는 매개변수이다.


"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# 훈련 데이터셋을 가지고 모델을 만들려면 fit메소드를 사용한다.
# fit메소드의 리턴값은 knn객체를 리턴한다.
kObj = knn.fit(X_train, y_train)
print("knn object :" , kObj)


