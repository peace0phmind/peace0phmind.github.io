---
title: "Pytorch"
description: "pytorch"
keywords: "pytorch"

date: 2022-11-23T11:31:54+08:00
lastmod: 2022-11-23T11:31:54+08:00

author: peace0phmind
url: "posts/202211/pytorch"

draft: true

categories:
  -
tags:
  - pytorch

---

## Dataset & DataLoader

- Dataset: stores data samples and expected values
- DataLoader: groups data in batches, enables multiprocessing

```python
dataset = MyDataset(file)
dataloader = DataLoader(dataset, batch_size, shuffle=True)
# When Training: shuffle=True, When Testing: shuffle=False
```

```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    # Read data & preprocess
    def __init__(self):
        self.data = ...

    # Returns one sample at a time
    def __getitem__(self, index):
        return self.data[index]

    # Returns the size of the dataset
    def __len__(self):
        return len(self.data)
```

## Tensors

- High-dimensional matrices (arrays)
  - 1-D tensor: e.g. audio
  - 2-D tensor: e.g. black&white images
  - 3-D tensor: e.g. RGB images

### Shape of Tensors

- Check with .shape()
- {{<color>}}dim{{</color>}} in PyTorch == {{<color>}}axis{{</color>}} in NumPy

![](/images/202211/pytorch/01.012.jpg)

### Creating Tensors

```python
import torch
import np

# Directly from data (list or numpy.ndarray)
x = torch.tensor([1, -1], [-1, 1])   
x = torch.from_numpy(np.array([1, -1], [-1, 1]))
# x is tensor([1., -1.], [-1., 1.])

# Tensor of constant zeros & ones (**the input is shape**)
x = torch.zeros([2, 2])   # x is tensor([[0., 0.], [0., 0.]])
x = torch.ones([1, 2, 5]) # x is tensor([[[1., 1., 1., 1., 1.], [1., 1., 1., 1., 1.]]])
```

### Common Operations

#### Common arithmetic functions

```python
# Common arithmetic functions are supported, such as:

z = x + y    # Addition
z = x - y    # Subtraction
y = x.sum()  # Summation
y = x.mean() # Mean
y = x.pow(2) # Power
```

#### Transpose
- Transpose: transpose two specified dimensions

```python
x = torch.zeros([2, 3])
x.shape
# output is: torch.Size([2, 3])

x = x.transpose(0, 1)  # input is dimension index
x.shape
# output is: torch.Size([3, 2])
```

#### Squeeze(压缩)
- Squeeze: remove the specified dimension with length = 1

```python
x = torch.zeros[1, 2, 3]
x.shape
# output is: torch.Size([1, 2, 3])

x = x.squeeze(0)  # squeeze x's dimension 0
x.shape
# output is: torch.Size([2, 3])
```

#### Unsqueeze
- Unsqueeze: expand a new dimension

```python
x = torch.zeros([2, 3])
x.shape
# output is: torch.Size([2, 3])

x = x.unsqueeze(1) # 在dimension index = 1的地方插入一个维度
x.shape
# output is: torch.Size([2, 1, 3])
```

#### Cat
- Cat: concatenate multiple tensors

```python
x = torch.zeros([2, 1, 3])
y = torch.zeros([2, 3, 3])
z = torch.zeros([2, 2, 3])
w = torch.cat([x, y, z], dim=1)
w.shape
# output is: torch.Size([2, 6, 3])
```

[more operators](https://pytorch.org/docs/stable/tensors.html)

### Data Type
- Using different data types for model and data will cause errors.

| Data type | dtype | tensor |
|--|--|--|
| 32-bit floating point | torch.float | torch.FloatTensor |
| 64-bit integer(signed) | torch.long | torch.LongTensor |

see [oﬃcial documentation](https://pytorch.org/docs/stable/tensors.html) for more information on data types.

### PyTorch v.s. NumPy
- Similar attributes

| PyTorch | NumPy |
|--|--|
| x.shape | x.shape |
| x.dtype | x.dtype |

- Many functions have the same names as well

| PyTorch | NumPy |
|--|--|
| x.reshape / x.view | x.reshape |
| x.squeeze() | x.squeeze() |
| x.unsqueeze(1) | np.expand_dims(x, 1) |

Ref [https://github.com/wkentaro/pytorch-for-numpy-users](https://github.com/wkentaro/pytorch-for-numpy-users)

### Device
- Tensors & modules will be computed with CPU by default
- Use .to() to move tensors to appropriate devices.
- Multiple GPUs: specify 'cuda:0', 'cuda:1', 'cuda:2', ...
- Why use GPUs?
  - Parallel computing with more cores for arithmatic calculations
  - See [What is a GPU and do you need one in Deep Learning?](https://towardsdatascience.com/what-is-a-gpu-and-do-you-need-one-in-deep-learning-718b9597aa0d)

```python
# CPU
x = x.to('cpu')

# GPU
x = x.to('cuda')

# Check if your computer has NVIDIA GPU
torch.cuda.is_available()
```

### Gradient Calculation

```python
x = torch.tensor([[1., 0.], [-1., 1.]], requires_grad=True) # 1
z = x.pow(2).sum()                                          # 2
z.backword()                                                # 3
x.grad                                                      # 4
# output is: tensor([[2., 0.], [-2., 2.]])
```

\begin{align}
x = \begin{bmatrix} 1 & 0 \cr -1 & 1 \end{bmatrix} \tag{1} \cr
z = \sum_i\sum_jx_{i,j}^2 \tag{2} \cr
\frac{\partial z}{\partial x_{i,j}} = 2x_{i,j} \tag{3} \cr
\frac{\partial z}{\partial x} = \begin{bmatrix} 2 & 0 \cr -2 & 2 \end{bmatrix} \tag{4}
\end{align}



## Reference Videos

{{< youtube 85uJ9hSaXig >}}

{{< youtube VbqNn20FoHM >}}
