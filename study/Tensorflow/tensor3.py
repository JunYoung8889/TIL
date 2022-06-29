import tensorflow as tf
import pandas as pd
import numpy as np


# csv 형식 파일 읽기
data = pd.read_csv('gpascore.csv')

# null 값 각 열 별로 개수 확인
# print(data.isnull().sum())
'''
admit    0
gre      1
gpa      0
rank     0
dtype: int64
'''

# null, NaN 값 제거
data = data.dropna()

# 빈칸 해당 값으로 채우기
# data = data.fillna(100)

# 열에 접근해서 해당열 최소값, 최대값, 개수 확인
# print(data['gpa'].min())
# print(data['gpa'].max())
# print(data['gpa'].count())
# exit()

# 데이터 변수 만들기
y데이터 = data['admit'].values
x데이터 = []
for idx, rows in data.iterrows():
    x데이터.append([rows['gre'], rows['gpa'], rows['rank']])
x데이터 = np.array(x데이터)
y데이터 = np.array(y데이터)


model = tf.keras.models.Sequential([
    # activation / sigmoid, tanh, relu, softmax, leakyRelu 등등
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

# optimizer / adam, adagrad, adadelta, rmsprop, sgd 등등
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# epochs 학습 횟수
model.fit( x데이터, y데이터, epochs=1000)

# 에측
예측값 = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(예측값)