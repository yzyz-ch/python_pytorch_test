import torchvision
from torch import nn
from torchvision import models

vgg16_false = models.vgg16(pretrained=False) # 不使用预训练模型
vgg16_true = models.vgg16(pretrained=True) # 使用预训练模型
print(vgg16_true)

train_data = torchvision.datasets.CIFAR10('../datasets', train=True, download=True, transform=torchvision.transforms.ToTensor())

vgg16_true.add_module('linear', nn.Linear(1000, 10))
print(vgg16_true)

print(vgg16_false)
vgg16_false.classifier[6] = nn.Linear(1000, 10)
print(vgg16_false)