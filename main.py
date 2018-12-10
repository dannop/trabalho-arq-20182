import sys
import network
sys.path.insert(0, "/home/danno/Documentos/Dev/Python/Arq_trabalho/neural-networks/src")
import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)