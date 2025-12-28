import torch
from torch.utils.tensorboard import SummaryWriter


class SampleNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # self.conv1 = torch.nn.Conv2d(3, 32, 5, padding = 2)
        # self.maxpool1 = torch.nn.MaxPool2d(2)
        # self.conv2 = torch.nn.Conv2d(32, 32, 5, padding = 2)
        # self.maxpool2 = torch.nn.MaxPool2d(2)
        # self.conv3 = torch.nn.Conv2d(32, 64, 5, padding = 2)
        # self.maxpool3 = torch.nn.MaxPool2d(2)
        # self.flatten = torch.nn.Flatten()
        # self.fc1 = torch.nn.Linear(1024, 64)
        # self.fc2 = torch.nn.Linear(64, 10)

        #等同上面的注释
        self.model1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 32, 5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 32, 5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 64, 5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Flatten(),
            torch.nn.Linear(1024, 64),
            torch.nn.Linear(64, 10)
        )

    def forward(self, x):
        # x = self.conv1(x)
        # x = self.maxpool1(x)
        # x = self.conv2(x)
        # x = self.maxpool2(x)
        # x = self.conv3(x)
        # x = self.maxpool3(x)
        # x = self.flatten(x)
        # x = self.fc1(x)
        # x = self.fc2(x)

        # 使用Sequential定义的模型
        x = self.model1(x)
        return x

sample_net = SampleNet()
print(sample_net)

input = torch.ones(64, 3, 32, 32)
output = sample_net(input)
print(output.size())
# print(output)

writer = SummaryWriter('logs/sequential')
writer.add_graph(sample_net, input)
writer.close()


