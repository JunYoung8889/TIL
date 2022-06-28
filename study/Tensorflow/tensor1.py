import tensorflow as tf

# tensor 생성
tensor1 = tf.constant([3, 4, 5])
tensor2 = tf.constant([6, 7, 8])
tensor3 = tf.constant([[1, 2], [3, 4]])

# 여러줄로 표현도 가능
tensor4 = tf.constant([[1, 2],
                        [3, 4]])

# 사칙연산
print(tensor1 + tensor2)
print(tf.add(tensor1, tensor2))
print(tensor1 - tensor2)
print(tf.subtract(tensor1, tensor2))
print(tensor1 * tensor2)
print(tf.multiply(tensor1, tensor2))
print(tensor1 / tensor2)
print(tf.divide(tensor1, tensor2))
print(tensor3 * tensor4)
print(tf.multiply(tensor3, tensor4))

# 행렬 곱셉 연산 / dot product
print(tf.matmul(tensor3, tensor4))

# 0으로 초기화
tensor5 = tf.zeros(10)
print(tensor5)
tensor6 = tf.zeros( [2, 2] )
print(tensor6)
tensor7 = tf.zeros( [2, 2, 3] )
print(tensor7)

# 모양 확인하기
print(tensor7.shape)

# tensor의 datatype 확인하기
tensor8 = tf.constant([1, 2, 3])
print(tensor8) # dtype=int32
tensor9 = tf.constant([1.0, 2.0, 3.0])
print(tensor9) # dtype=float32
tensor10 = tf.constant([1.0, 2, 3])
print(tensor10) # dtype=float32

# tensor의 datatype 변환하기
tensor11 = tf.constant([1, 2, 3], tf.float32)
print(tensor11)
print(tf.cast(tensor9, tf.int32))
tensor12 = tf.constant([1.1, 2.1, 3.1])
tensor13 = tf.dtypes.cast(tensor12, tf.int32)
print(tensor13)

# weight
w1 = tf.Variable(1.0) # dtype=float32
print(w1)
print(w1.numpy())
w1.assign(2) # dtype=float32
print(w1)
w2 = tf.Variable(1) # dtype=int32
print(w2)
w2.assign(2) # dtype=int32
print(w2)
# w2.assign(3.0)
# TypeError: Cannot convert 3.0 to EagerTensor of dtype int32