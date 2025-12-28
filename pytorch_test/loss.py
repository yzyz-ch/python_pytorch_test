import torch
from torch import nn
from torch.nn import L1Loss

input = torch.tensor([1, 2, 3])
target = torch.tensor([1, 2, 5])

input = torch.reshape(input, (1, 1, 1, 3))
target = torch.reshape(target, (1, 1, 1, 3))

loss = L1Loss(reduction='sum')
output = loss(input, target)

loss_mse = nn.MSELoss()
loss_mse_output = loss_mse(input, target)
print(output)




