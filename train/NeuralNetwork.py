import tensorflow as tf
from configs import LearningConfigs

def newLayer(inputs, inSize, outSize, func = None):
    W = tf.Variable(tf.random_normal([inSize, outSize]))
    b = tf.Variable(tf.zeros([1, outSize]) + 0.1)
    if func is None:
        return tf.matmul(inputs, W) + b
    else:
        return func(tf.matmul(inputs, W) + b)

def DeepLearning(trainingData,
                 learingRate = LearningConfigs.LEARNING_RATE,
                 batch = LearningConfigs.BATCH):

    # x is the placeholder representing the observed snake state
    x = tf.placeholder(tf.int64, [None, 8])

    # d is the placeholder representing the direction our snake took
    d = tf.placeholder(tf.float32, [None, 3])

    # define two hidden layers
    h1 = newLayer(x, 8, 16, tf.nn.relu)
    h2 = newLayer(h1, 16, 16, tf.nn.relu)

    # define the prediction layer
    p = newLayer(h2, 16, 3)

    # define error function
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=d, logits=p))

    # define optimizer
    trainStep = tf.train.GradientDescentOptimizer(learingRate).minimize(loss)

    # initialization
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    steps = len(trainingData) / batch

    for i in range(steps):
        X = fetchObserve(x[i * batch: (i + 1) * batch])
        Y = fetchDirection(d[i * batch: (i + 1) * batch])
        sess.run(trainStep, feed_dict={x: X, d: Y})

    saver = tf.train.Saver()
    saver.save(sess, LearningConfigs.MODEL_PATH)


def fetchObserve(lst):
    res = []
    for flatList in lst:
        for move in flatList:
            res.append(move[0])

    return res


def fetchDirection(lst):
    dir = []
    for flatList in lst:
        for move in flatList:
            dir.append(move[1])

    return dir
