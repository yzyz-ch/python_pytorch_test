import torch

a = torch.zeros(2, 3, device=torch.device('cuda'))
print(a)

b  = torch.ones(4, 5)
print(b)

c = torch.rand(2, 3)
print(c)

import numpy
numpy_array = numpy.array([[1,2,3],[4,5,6]])
tensor_array = torch.from_numpy(numpy_array)
print(tensor_array)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
d = torch.rand(2, 4, device=device)
print("d:", d)

d_t = d.T
print("dt:", d_t)

e = torch.rand(2, 4, device=device)
f = torch.rand(2, 4, device=device)
g = e + f
print(g)
print(g.shape)

