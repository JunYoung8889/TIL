import tensorflow as tf


# loss(cost) function
def 손실함수():
    global 신발사이즈, 키, w1, b
    실제값 = 신발사이즈
    예측값 = 키 * w1 + b
    return tf.square(실제값 - 예측값)


키 = 170
신발사이즈 = 260

# weight 가중치
w1 = tf.Variable(0.1)

# bias 편향
b = tf.Variable(0.2)


# learning rate optimizer
opt = tf.keras.optimizers.Adam(learning_rate = 0.1)

# 총손실 E를 최소화하는 경사 하강법 Gradient Descent 300회 반복
for _ in range(300):
    opt.minimize(손실함수, var_list = [w1, b])
    print('weigth =', w1.numpy(), '/ bias =', b.numpy())

최종예측값 = 키 * w1 + b
실제값 = 신발사이즈
print('최종예측값 :', 최종예측값.numpy(), '/ 실제값 :', 신발사이즈)
