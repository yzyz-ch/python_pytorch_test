import torch

# 检查 PyTorch 是否可以使用 GPU
print("CUDA Available:", torch.cuda.is_available())
print("CUDA Device Count:", torch.cuda.device_count())
print("Current CUDA Device:", torch.cuda.current_device())
print("Current Device Name:", torch.cuda.get_device_name(torch.cuda.current_device()))
