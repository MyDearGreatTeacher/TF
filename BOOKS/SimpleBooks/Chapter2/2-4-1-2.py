import tensorflow as tf
#"2��2�������2�Ķ�ά����"
x=tf.constant(
        [
        [[2,5],[4,3]],
        [[6,1],[1,2]]
        ],tf.float32
        )
#"2��2�������2�Ķ�ά����"
y=tf.constant(
        [
        [[1,2],[2,3]],
        [[3,2],[5,3]]
        ],tf.float32
        )
session=tf.Session()
#"x��y�ĺ�"
result=x+y
print(session.run(result))