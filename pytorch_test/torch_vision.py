import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

dataset_transform = transforms.Compose([
    transforms.ToTensor()
])

# 修复：将 transform 参数传递给数据集
train_set = torchvision.datasets.CIFAR10(root='./dataset', train=True, download=True, transform=dataset_transform)
test_set = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True, transform=dataset_transform)

print(train_set[0])
print(test_set[0])

img, target = test_set[0]
print(test_set.classes)

img, target = test_set[0]
print(img)
print(target)
print(test_set.classes[target])
# img.show()


writer = SummaryWriter("p10")
for i in range(10):
    img, target = test_set[i]
    writer.add_images("test_set", img, i)

writer.close()
