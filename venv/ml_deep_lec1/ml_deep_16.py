from sklearn import svm, metrics
import random , re   # re는 정규표현식용 패키지
#붓꽃의 데이터를 읽어 들이기

csv = []

with open('/Users/taoist/woks/irisData/iris.csv', 'r', encoding='utf-8') as fp:
    # 한 줄씩 읽어오기
    for line in fp:
        line = line.strip() # 줄바꿈 제거
        cols = line.split(',')  # 쉼표로 칼럼을 구분
        print(line)
        #문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$',n) else n
        cols = list(map(fn,cols))
        csv.append(cols)

# 헤더 제거 (컬럼명 제거)
del csv[0]

print(csv)

# 데이터를 섞어주기
random.shuffle(csv)

# 훈련(학습) 데이터와 테스트 데이터로 분리하기
total_len = len(csv)
train_len = int(total_len * 2/3)
print(train_len)

train_data = []
train_lable = []




