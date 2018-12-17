from train.NeuralNetwork import NeuralNetwork
from train.Experience import ERM

nn = NeuralNetwork()
erm = ERM()

data = erm.loadData()

nn.train(data)
nn.saveModel()