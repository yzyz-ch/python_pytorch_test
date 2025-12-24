import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision.transforms import transforms

dataset = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True, transform=transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=64)

class activateNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.relu1 = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        # output = self.relu1(input)
        output = self.sigmoid(input)
        return output

net = activateNet()
writer = SummaryWriter('./logs/activate')

step = 0
for data in dataloader:
    img, target = data
    out = net(img)
    writer.add_images('input', img, step)
    writer.add_images('output', out, step)
    step += 1

writer.close()