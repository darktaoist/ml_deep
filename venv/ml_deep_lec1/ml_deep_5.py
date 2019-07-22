from sklearn import svm

xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    res = row[2]

    data.append([p,q])
    label.append(res)

#SVM알고리즘을 사용하는 머신러닝 객체를 만든다.
clf = svm.SVC()

#fit() 메소드 학습기계에 데애터를 학습시킨다.

