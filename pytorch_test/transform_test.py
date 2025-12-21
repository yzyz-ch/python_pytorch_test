from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image

img_path = "E:\python-learn\\test_python_pytorch\pytorch_test\datasets\hymenoptera_data\\train\\ants\\0013035.jpg"

img = Image.open(img_path)
tensor_img = transforms.ToTensor()(img)
print(img)
print(tensor_img.shape)

writer = SummaryWriter(log_dir='logs')
writer.add_image('test_transform', tensor_img)
writer.close()

