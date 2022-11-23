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

## torch.nn

### Network Layers
- Linear Layer (Fully-connected Layer)

```python
layer = torch.nn.Linear(32, 64)
layer.weight.shape
# output is: torch.Size([64, 32])
layer.bias.shape
# output is: torch.Size([64])
```

### Non-Linear Activation Functions
- Sigmoid Activation: nn.Sigmoid()
- ReLU Activation: nn.ReLU()

### Build your own neural network

```python
import torch.nn as nn

class MyModel(nn.Module):
  def __init__(self):
    super(MyModel, self).__init__()
    self.net = nn.Sequential(
      nn.Linear(10, 32),
      nn.Sigmoid(),
      nn.Linear(32, 1)
    )

  def forward(self, x):
    return self.net(x)
```

上下这两段代码是等价的

```python
import torch.nn as nn

class MyModel(nn.Module):
  def __init__(self):
    super(MyModel, self).__init__()
    self.layer1 = nn.Linear(10, 32)
    self.layer2 = nn.Sigmoid()
    self.layer3 = nn.Linear(32, 1)

  def forward(self, x):
    out = self.layer1(x)
    out = self.layer2(out)
    out = self.layer3(out)
    return out
```

### Loss Functions
- Mean Squared Error (for regression tasks)
  - criterion = nn.MSELoss()
- Cross Entropy (for classification tasks)
  - criterion = nn.CrossEntropyLoss()
- loss = criterion(model_output, expected_value)

### Optimization Algorithms
- Gradient-based optimization algorithms that adjust network
  parameters to reduce error. 
- E.g. Stochastic Gradient Descent (SGD)
  - torch.optim.SGD(model.parameters(), lr, momentum = 0)

### torch.optim
optimizer = torch.optim.SGD(model.parameters(), lr, momentum = 0)

- For every batch of data:
  - Call optimizer.zero_grad() to reset gradients of model parameters.
  - Call loss.backward() to backpropagate gradients of prediction loss.
  - Call optimizer.step() to adjust model parameters.

###  Training Loop

```python
dataset = MyDataset(file)                           # read data via MyDataset
tr_set = DataLoader(dataset, 16, shuffle=True)      # put dataset into Dataloader
model = MyModel().to(device)                        # construct model and move to device (cpu/cuda)
criterion = nn.MSELoss()                            # set loss function
optimizer = torch.optim.SGD(model.parameters(), 0.1)# set optimizer

for epoch in range(n_epochs):                       # iterate n_epochs
  model.train()                                     # set model to train mode
  for x, y in tr_set:                               # iterate through the dataloader
    optimizer.zero_grad()                           # set gradient to zero
    x, y = x.to(device), y.to(device)               # move data to device (cpu/cuda)
    pred = model(x)                                 # forward pass (compute output)
    loss = criterion(pred, y)                       # compute loss
    loss.backward()                                 # compute gradient (backpropagation)
    optimizer.step()                                # update model with optimizer
```

### Validation Loop

```python
model.eval()                                        # set model to evaluation mode
total_loss = 0
for x, y in dv_set:                                 # iterate through the dataloader
  x, y = x.to(device), y.to(device)                 # move data to device (cpu/cuda)
  with torch.no_grad():                             # disable gradient calculation
    pred = model(x)                                 # forward pass (compute output)
    loss = criterion(pred, y)                       # compute loss
  total_loss += loss.cpu().item() * len(x)          # accumulate loss
  avg_loss = total_loss / len(dv_set.dataset)       # compute averaged loss
```

### Testing Loop

```python
model.eval()                                        # set model to evaluation mode
preds = []
for x in tt_set:                                    # iterate through the dataloader
  x = x.to(device)                                  # move data to device (cpu/cuda)
  with torch.no_grad():                             # disable gradient calculation
    pred = model(x)                                 # forward pass (compute output)
    preds.append(pred.cpu())                        # collect prediction
```

### Notice - model.eval(), torch.no_grad()
- model.eval()
  - Changes behaviour of some model layers, such as dropout and batch normalization.
  - 类似dropout或者batch normalization在训练和测试的时候做的事情是不一样的，所以需要告知模型当前在做训练还是测试
- with torch.no_grad()
  - Prevents calculations from being added into gradient computation graph. Usually used to prevent accidental training on validation/testing data.
  - 梯度是拿来调整模型的，在做测试的时候我们不需要做这件事情，把梯度计算关掉会跑的快一点点。另外，也可以避免用测试数据的梯度更新我们的模型。

### Save/Load Trained Models
```python
# Save
torch.save(model.state_dict(), path)

# Load
ckpt = torch.load(path)
model.load_state_dict(ckpt)
```

### More About PyTorch
- torchaudio: speech/audio processing
- torchtext: natural language processing
- torchvision: computer vision
- skorch: scikit-learn + pyTorch

## Reference

### Reference projects
- [huggingface-transformers](https://github.com/huggingface/transformers) (transformer models: BERT, GPT, ...)
- [Facebook-fairseq](https://github.com/facebookresearch/fairseq) (sequence modeling for NLP & speech)
- [espnet](https://github.com/espnet/espnet) (speech recognition, translation, synthesis, ...)
- [pytorch tutorials](https://pytorch.org/tutorials/index.html)

### Reference Videos

{{< youtube 85uJ9hSaXig >}}

{{< youtube VbqNn20FoHM >}}
