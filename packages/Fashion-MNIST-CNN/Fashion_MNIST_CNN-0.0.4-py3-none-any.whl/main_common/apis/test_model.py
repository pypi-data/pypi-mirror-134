import numpy as np
from keras.datasets import fashion_mnist

from ..model import load_local_model

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()


def get_inference():
    index = np.random.randint(0, len(x_test) - 1)  # randomly choose a sample from the test set
    sample = np.array([x_test[index]])
    prediction = load_local_model.restored_model.predict(sample)
    print('Sample Number:', index, '\n',
          '\nPredicted Class:', np.argmax([prediction[0]]),
          'Actual Class:', np.argmax(y_test[index]))


# get_inference()
