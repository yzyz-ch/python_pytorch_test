import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


test_data = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True, transform=torchvision.transforms.ToTensor())
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=False)


writer = SummaryWriter(log_dir='dataloader')
# 测试数据集中的第一张图片及标签
img, target = test_data[0]
print(img.shape)
print(target)

step = 0
for data in test_loader:
    img, target = data
    # print(img.shape)
    # print(target)
    writer.add_images('loaderlog', img, step)
    step = step + 1

writer.close()



