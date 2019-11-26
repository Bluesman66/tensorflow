import tensorflow as tf

sess = tf.compat.v1.InteractiveSession()

x = tf.constant([[1., 2.]])
negMatrix = tf.negative(x)

result = negMatrix.eval()

sess.close()