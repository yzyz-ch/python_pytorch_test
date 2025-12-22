import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root="./datasets", train=False, transform=torchvision.transforms.ToTensor(), download=True)

dataloader = DataLoader(dataset, batch_size=64)

class convNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 3, 1, 0)


    def forward(self, x):
        x = self.conv1(x)
        return x

tudui = convNet()

writer = SummaryWriter('conv')

step = 0
for data in dataloader:
    img, target = data
    out = tudui(img)
    out= torch.reshape(out, (-1, 3, 30, 30))
    # print(img.shape)
    # print(out.shape)
    writer.add_images('input', img, step)
    writer.add_images('output', out, step)
    step += 1
