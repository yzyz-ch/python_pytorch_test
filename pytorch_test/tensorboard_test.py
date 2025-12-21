import torch
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image


writer = SummaryWriter('logs')
image_path = "E:\python-learn\\test_python_pytorch\pytorch_test\datasets\hymenoptera_data\\train\\ants\\0013035.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)
writer.add_image('test', img_array, 1, dataformats='HWC')

#y = x
for i in range(100):
    writer.add_scalar('y=2x', 2 * i, i) #description  yvalue xvalue

writer.close()
