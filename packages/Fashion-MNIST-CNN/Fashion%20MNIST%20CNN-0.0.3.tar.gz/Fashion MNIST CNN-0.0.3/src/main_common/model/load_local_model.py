from keras.models import load_model
import os

_dir = os.path.join(os.path.dirname(__file__), 'saved_model/')
restored_model = load_model(_dir + 'Fashion_Mnist_CNN.h5')
