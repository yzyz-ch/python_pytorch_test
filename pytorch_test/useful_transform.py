from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter(log_dir='logs')

img = Image.open("E:\python-learn\\test_python_pytorch\pytorch_test\datasets\hymenoptera_data\\train\\ants\\0013035.jpg")

#to tensor
img_tensor = transforms.ToTensor()(img)
writer.add_image("image", img_tensor)

#normalize
img_normalize = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])(img_tensor)
writer.add_image("image_normalize", img_normalize)

#resize


img_resize = transforms.Resize((224, 224))(img_tensor)
writer.add_image("image_resize", img_resize)

#PIL resize
img_pil_resize = img.resize((224, 224)) #here
img_pil_resize_tensor = transforms.ToTensor()(img_pil_resize)
writer.add_image("image_pil_resize", img_pil_resize_tensor)

# compose transform
transform_compose = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])
img_compose = transform_compose(img)
writer.add_image("image_compose", img_compose)

# random crop
img_random_crop = transforms.RandomCrop((224, 224))(img_tensor)
writer.add_image("image_random_crop", img_random_crop)

writer.close()