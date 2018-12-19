import tensorflow as tf
import numpy as np
from configs import LearningConfigs


class NeuralNetwork:
    def __init__(self, learningRate = LearningConfigs.LEARNING_RATE):
        self.x = tf.placeholder(tf.int64, [None, 8])
        self.d = tf.placeholder(tf.float32, [None, 3])

        self.h1 = newLayer(self.x, 8, 16, tf.nn.relu)
        self.h2 = newLayer(self.h1, 16, 16, tf.nn.relu)

        self.p = newLayer(self.h2, 16, 3)

        self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = self.d, logits = self.p))

        self.trainStep = tf.train.GradientDescentOptimizer(learningRate).minimize(self.loss)

    def predict(self, observe):
        pred = self.sess.run(self.p, feed_dict = {self.x: observe})
        return np.argmax(pred) - 1

    def train(self, trainingData, batch = LearningConfigs.BATCH):
        init = tf.initialize_all_variables()
        self.sess = tf.Session()
        self.sess.run(init)

        steps = len(trainingData) / batch

        for i in range(steps):
            X = fetchObserve(trainingData[i * batch: (i + 1) * batch])
            Y = fetchDirection(trainingData[i * batch: (i + 1) * batch])
            self.sess.run(self.trainStep, feed_dict={self.x: X, self.d: Y})

    def saveModel(self):
        saver = tf.train.Saver()
        saver.save(self.sess, LearningConfigs.MODEL_PATH)

    def loadModel(self):
        saver = tf.train.Saver()

        with tf.Session() as session:
            saver.restore(session, LearningConfigs.MODEL_PATH)

def newLayer(inputs, inSize, outSize, func = None):
    W = tf.Variable(tf.random_normal([inSize, outSize]))
    b = tf.Variable(tf.zeros([1, outSize]) + 0.1)
    if func is None:
        return tf.matmul(inputs, W) + b
    else:
        return func(tf.matmul(inputs, W) + b)


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
