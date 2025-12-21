from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

#数据下载

path = '../datasets/mnist'
# 下载并定义数据集
train_dataset = MNIST(path, train=True, transform=ToTensor(), download=True)
test_dataset = MNIST(path, train=False, transform=ToTensor(), download=True)


