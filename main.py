# import tensorflow as tf
from matplotlib import pyplot as pl
x = [3, 6, 10, 13, 14, 17]
y = [1, 2, 3, 4, 5, 6]
pl.plot(x, y, 'ro')
pl.axis([0, 20, 0, 10])
pl.plot()
pl.show()
'''
var = tf.constant(1.0)
# tf types: int16, int32, float64, string
tensor = tf.ones([5, 5, 5, 5])
tensor = tf.reshape(tensor, [-1])
tf.print(tensor.shape)
'''
