import tensorflow as tf
from tensorflow.random import uniform, normal


class VarSpec:
    def __init__(self, character='x', limit=(0, 1)):
        self._character = character
        self._limit = limit

    @property
    def character(self):
        return self._character

    def random_uniform(self, num):
        min_val, max_val = self._limit
        return uniform([num, 1], minval=min_val, maxval=max_val)

    def random_normal(self, num, **kwargs):
        min_val, max_val = self._limit
        data = normal([num, 1], **kwargs)
        data = tf.where(data > max_val, max_val, data)
        data = tf.where(data < min_val, min_val, data)
        return data

    def random(self, num, random_type='uniform', **kwargs):
        if random_type == "uniform":
            return self.random_uniform(num)
        elif random_type == "normal":
            return self.random_normal(num, **kwargs)
        else:
            raise ValueError(f"random_type must be uniform or normal.")
