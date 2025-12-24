import torch
import torch.nn.functional as F
import torchvision
from torch.nn.modules.module import T
from torch.utils.data import Dataset, DataLoader
from torch.utils.tensorboard import SummaryWriter

datasets = torchvision.datasets.CIFAR10(root='./datasets', train=True, download=True, transform=torchvision.transforms.ToTensor())
train_loader = DataLoader(dataset=datasets, batch_size=64)

class maxpool(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool1 = torch.nn.MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool1(input)
        return output

maxpoolLayer = maxpool()

writer = SummaryWriter("logs/maxpool")

step = 0
for data in train_loader:
    img, target = data
    writer.add_images('input', img, step)
    out = maxpoolLayer(img)
    writer.add_images('output', out, step)
    # print(img.shape)
    # print(out.shape)
    step += 1

