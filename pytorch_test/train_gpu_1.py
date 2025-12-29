import torch
import torchvision
from torch import nn
# from model import TestNet
from torch.utils.tensorboard import SummaryWriter

#准备数据集
train_data = torchvision.datasets.CIFAR10(root='./datasets', train=True, download=True, transform=torchvision.transforms.ToTensor())
test_data = torchvision.datasets.CIFAR10(root='./datasets', train=False, download=True, transform=torchvision.transforms.ToTensor())

#
train_data_size = len(train_data)
test_data_size = len(test_data)
print("train_data_size:", train_data_size)
print("test_data_size:", test_data_size)

train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=64)
test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=64)

#创建网络模型

class TestNet(nn.Module):
    def __init__(self):
        super(TestNet, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64*4*4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x

test_net = TestNet()
if torch.cuda.is_available():
    test_net.cuda()
#损失函数
loss_fun = nn.CrossEntropyLoss()
if torch.cuda.is_available():
    loss_fun.cuda()
#优化器
Learning_rate = 0.001
optimizer = torch.optim.SGD(test_net.parameters(), lr=Learning_rate) #随机梯度下降


#设置训练网络一些参数
#记录训练次数
total_train_step = 0
#记录测试次数
total_test_step = 0
#训练轮数
epoch = 5

#添加tensorboard
writer = SummaryWriter("logs/train")

for i in range(epoch):
    print("第{}轮训练开始".format(i+1))
    #训练步骤开始

    test_net.train()  #模型中包含dropout或batch norm层，可以在训练时调用
    for data in train_dataloader:
        img, label = data
        if torch.cuda.is_available():
            img = img.cuda()
            label = label.cuda()
        output = test_net(img)
        loss = loss_fun(output, label)
        #优化器优化模型参数
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step += 1
        # print("训练次数：{}， Loss: {}".format(total_train_step, loss.item())) 不让每次都print
        if total_train_step % 100 == 0:
            print("训练次数：{}， Loss: {}".format(total_train_step, loss.item()))
            writer.add_scalar("loss", loss.item(), total_train_step)


    test_net.eval()  #模型中包含dropout或batch norm层，可以在测试时调用
    total_test_loss = 0
    total_test_accuracy = 0 #整体正确的次数
    with torch.no_grad(): #没有梯度
        #测试步骤开始
        for data in test_dataloader:
            img, label = data
            if torch.cuda.is_available():
                img = img.cuda()
                label = label.cuda()
            output = test_net(img)
            loss = loss_fun(output, label)
            total_test_loss = total_test_loss + loss.item()
            # 计算准确率
            accuracy = (output.argmax(1) == label).sum()
            total_test_accuracy += accuracy.item()

            # total_test_step += 1
            # print("测试次数：{}， Loss: {}".format(total_test_step, loss.item()))

    print("整体测试集上的Loss: {}".format(total_test_loss))
    print("整体测试集上的准确率: {}".format(total_test_accuracy/test_data_size))
    writer.add_scalar("test_loss", total_test_loss, total_train_step)
    writer.add_scalar("test_accuracy", total_test_accuracy/test_data_size, total_train_step)
    total_test_step += 1

    # torch.save(test_net.state_dict(), "logs/test_net.pth")
    torch.save(test_net, "test_net_gpu{}.pth".format(total_test_step))
    print("模型已保存")

writer.close()

