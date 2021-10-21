import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np

from admin.common.models import ValueObject


class TensorFunction(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/tensor/data/'

    def hook(self):
        menu = 'train_tf_model_by_random_data'
        if menu == 'tf_function':
            result = self.tf_function()
            '''
            [0.]]]]), array([4, 8, 1, 8, 6, 3, 4, 9, 8, 1, 3, 0, 8, 6, 6, 5, 1, 5, 7, 8, 0, 1,
               5, 1, 2, 7, 3, 7, 9, 8, 4, 7], dtype=uint8)), (array([[[[0.],
            '''
        elif menu == 'tf_sum':
            result = self.tf_sum()  # 결과: 6.0
        elif menu == 'tf_add':
            result = self.tf_add()
        elif menu == 'create_model':
            result = self.create_model().summary()
        elif menu == 'create_tf_empty_model':
            result = self.create_tf_empty_model()
        elif menu == 'train_tf_model_by_random_data':
            result = self.train_tf_model_by_random_data()
        else:
            result = '해당사항 없음'
        print(f'결과: {result}')

    def train_tf_model_by_random_data(self):
        (x, y) = self.make_random_data()
        x_train, y_train = x[:150], y[:150]
        x_test, y_test = x[:150], y[:150]
        model = keras.models.load_model(f'{self.vo.context}simple_model.h5')
        history = model.fit(x_train, y_train, epochs=30, validation_split=0.3)
        epochs = np.arange(1, 30 + 1)
        plt.plot(epochs, history.history['loss'], label='Training Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(f'{self.vo.context}simple_model.png')
        return model

    def create_tf_empty_model(self):
        '''
        Dense(units=1, input_dim=1)
        옵티마이저 sgd, 손실함수 mse, 활성화함수 Relu
        드롭아웃 20%
        simple_model.h5 로 작성하시오
        '''
        # model = keras.Sequential([
        #     keras.layers.Flatten(input_shape=[150, 150]),
        #     keras.layers.Dropout(rate=0.2),
        #     keras.layers.Dense(1, activation="relu", kernel_initializer="he_normal"),
        #     keras.layers.Dropout(rate=0.2),
        #     keras.layers.Dense(1, activation="softmax")
        # ])
        model = keras.Sequential()
        model.add(keras.layers.Dense(1, activation="relu", input_dim=1))
        model.add(keras.layers.Dropout(rate=0.2))
        model.add(keras.layers.Dense(1, activation="softmax"))
        '''
        model = Sequential()    # sequntial 모델 생성 할당 첫번째 층을  
        model.add(Dense(32, input_shape=(16, ))) # 첫번째 층을 dense 32 크기 out 
        model.add(Dense(32))
        Arguments:
        units: 현재 dense 를 통해서 만들 hidden layer 의 Node 의 수
        첫번째 인자 : 출력 뉴런의 수를 설정합니다.
        input_dim : 입력 뉴런의 수를 설정합니다.
        init : 가중치 초기화 방법 설정합니다.
        uniform : 균일 분포
        normal : 가우시안 분포
        activation : 활성화 함수 설정합니다.
        linear : 디폴트 값, 입력뉴런과 가중치로 계산된 결과값이 그대로 출력으로 나옵니다.
        relu : rectifier 함수, 은익층에 주로 쓰입니다.
        sigmoid : 시그모이드 함수, 이진 분류 문제에서 출력층에 주로 쓰입니다.
        softmax : 소프트맥스 함수, 다중 클래스 분류 문제에서 출력층에 주로 쓰입니다.
        다중클래스 분류문제에서는 클래스 수만큼 출력 뉴런이 필요합니다. 
        만약 세가지 종류로 분류한다면, 아래 코드처럼 출력 뉴런이 3개이고, 
        입력 뉴런과 가중치를 계산한 값을 각 클래스의 확률 개념으로 표현할 수 있는 
        활성화 함수인 softmax를 사용합니다.

        https://talkingaboutme.tistory.com/entry/DL-%ED%95%B4%EB%B3%B4%EB%A9%B4%EC%84%9C-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EB%94%A5%EB%9F%AC%EB%8B%9D-ANN-%EA%B5%AC%ED%98%84-2
        '''
        model.compile(optimizer="sgd", loss="mse", metrics=['accuracy'])
        model.save(f'{self.vo.context}simple_model.h5')
        return model

    def make_random_data(self):
        x = np.random.uniform(low=-2, high=2, size=200)
        y = []
        for t in x:
            r = np.random.normal(loc=0.0, scale=(0.5 + t * t /3), size=None)
            y.append(r)
        return x, 1726 * x - 0.84 + np.array(y)

    def create_model(self) -> object:
        input = tf.keras.Input(shape=(1, ))     # 텐서플로 입력층, 반드시 행렬(matrix)구조!
        output = tf.keras.layers.Dense(1)(input)    # 텐서플로 출력층
        model = tf.keras.Model(input, output)
        return model

    @tf.function
    def tf_sum(self):
        a = tf.constant(1, tf.float32)
        b = tf.constant(2, tf.float32)
        c = tf.constant(3, tf.float32)
        z = a + b + c
        print('#'*100)
        return z

    def tf_add(self):
        x = [1, 2, 3, 4, 5]
        # 값이 하나 혹은 1:1 매칭!
        # y = [1, 2, 3, 4, 5]
        y = 2
        
        z = tf.add(x, y)
        # z = tf.math.add(x, y)     # math 생략 가능
        # z = tf.subtract(x, y)
        # z = tf.multiply(x, y)
        # z = tf.divide(x, y)
        return z

    def tf_function(self):
        mnist = keras.datasets.mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X_train, X_test = X_train / 255.0, X_test / 255.0
        X_train = X_train[..., tf.newaxis]  # 차원 추가
        X_test = X_test[...], tf.newaxis
        train_ds = tf.data.Dataset.from_tensor_slices(
            (X_train, y_train)
        ).shuffle(10000).batch(32)  # 배치를 32조각으로 미니배치화!
        test_ds = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)
        '''
        print(f'train_ds: {type(train_ds)}')
        train_ds: <class 'tensorflow.python.data.ops.dataset_ops.BatchDataset'>
        # print(list(train_ds.as_numpy_iterator()))
        '''
        return list(train_ds.as_numpy_iterator())


class FashionClassification(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/tensor/data/'
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def fashion(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        # self.peek_datas(train_images, test_images, test_labels)
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=[28, 28]),
            keras.layers.Dense(128, activation="relu"),  # neron count 128
            keras.layers.Dense(10, activation="softmax")  # 출력층 활성화함수는 softmax
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=5)
        # self.test_and_save_images(model, test_images, test_labels)
        model.save(f'{self.vo.context}fashion_classification.h5')

    def peek_datas(self, train_images, test_images, train_labels):
        print(train_images.shape)
        print(train_images.dtype)
        print(f'훈련 행: {train_images.shape[0]} 열: {train_images.shape[1]}')
        print(f'테스트 행: {test_images.shape[0]} 열: {test_images.shape[1]}')
        plt.figure()
        plt.imshow(train_images[3])
        plt.colorbar()
        plt.grid(False) # 격자 제거
        plt.savefig(f'{self.vo.context}fashion_random.png')
        plt.figure(figsize=(10, 10))
        for i in range(25):
            plt.subplot(5,5,i+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_name[train_labels[i]])
        plt.savefig(f'{self.vo.context}fashion_subplot.png')

    def test_and_save_images(self, model, test_images, test_labels):
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)  # verbose 는 학습하는 내부상황 보기 중 2번선택
        predictions = model.predict(test_images)
        i = 5
        print(f'모델이 예측한 값 {np.argmax(predictions[i])}')
        print(f'정답: {test_labels[i]}')
        print(f'테스트 정확도: {test_acc}')
        plt.figure(figsize=(6, 3))
        plt.subplot(1, 2, 1)
        test_image, test_predictions, test_label = test_images[i], predictions[i], test_labels[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(test_image, cmap=plt.cm.binary)
        test_pred = np.argmax(test_predictions)

        if test_pred == test_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} : {} %'.format(self.class_names[test_pred],
                                      100 * np.max(test_predictions),
                                      self.class_names[test_label], color))
        plt.subplot(1, 2, 2)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        this_plot = plt.bar(range(10), test_pred, color='#777777')
        plt.ylim([0, 1])
        test_pred = np.argmax(test_predictions)
        this_plot[test_pred].set_color('red')
        this_plot[test_label].set_color('blue')
        plt.savefig(f'{self.vo.context}fashion_answer2.png')


class Perceptron(object):  # 퍼셉트론 분류기

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta  # float 학습률 (0.0과 1.0 사이)
        self.n_iter = n_iter  # int 훈련 데이터셋 반복 횟수
        self.random_state = random_state  # int 가중치 무작위 초기화를 위한 난수 생성기

    # 훈련 데이터 학습
    def fit(self, X, y, epoch) -> object:  # 여기서 오브젝트는 데이터 프레임이 아니다.
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])  # 1d-array : 학습된 가중치
        self.errors_ = []  # list 에포크마다 누적된 분류 오류

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    # 단위 계단 함수를 사용하여 클래스 변환
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    # 최종 입력 계산
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]


class AdalineGD(object): # 적응형 선형 뉴런 분류기

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        # X : {array-like}, shape = [n_samples, n_features]
        #           n_samples 개의 샘플과 n_features 개의 특성으로 이루어진 훈련 데이터

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = [] # 에포크마다 누적된 비용 함수의 제곱합

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            # Please note that the "activation" method has no effect
            # in the code since it is simply an identity function. We
            # could write `output = self.net_input(X)` directly instead.
            # The purpose of the activation is more conceptual, i.e.,
            # in the case of logistic regression (as we will see later),
            # we could change it to
            # a sigmoid function to implement a logistic regression classifier.
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return X

    def predict(self, X): # 단위 계단 함수를 사용하여 클래스 레이블을 반환
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


class Calculator(object):

    def __init__(self):
        print(f'Tensorflow Version {tf.__version__}')

    def process(self):
        self.plus(5, 10)
        print('*' * 100)
        self.mean()

    def plus(self, a, b):
        print(tf.constant(a) + tf.constant(b))

    def mean(self):
        x_array = np.arange(18).reshape(3, 2, 3)
        x2 = tf.reshape(x_array, shape=(-1, 6))
        # 각 열의 합을 계산
        xsum = tf.reduce_sum(x2, axis=0)
        # 각 열의 평균을 계산
        xmean = tf.reduce_mean(x2, axis=0)

        print(f'입력 크기: {x_array.shape}\n')
        print(f'크기가 변경된 입력 크기: {x2.numpy()}\n')
        print(f'열의 합: {xsum.numpy()}\n')
        print(f'열의 평균: {xmean.numpy()}\n')