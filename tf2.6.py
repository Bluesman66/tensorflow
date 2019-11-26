import tensorflow as tf

# x = tf.constant([[1., 2.]])
# negMatrix = tf.negative(x)

# with tf.compat.v1.Session() as sess:
#     result = sess.run(negMatrix)

# print(result)

c = tf.constant([[1., 2.]])
sess = tf.compat.v1.Session()

with sess.as_default():
  assert tf.compat.v1.get_default_session() is sess
  print(c.eval())
