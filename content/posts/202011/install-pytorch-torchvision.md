---
title: "安装Pytorch和Torchvision"
date: 2020-11-04T18:07:26+08:00
draft: false
---

本文简单描述在jetson nano上安装最新的pytorch 1.7.0和torchvision 0.8.1的步骤。

## 安装

### 安装前准备

```bash
sudo apt update
sudo apt upgrade
```

### 安装pytorch

首先下载最新的pytorch版本[PyTorch v1.7.0](https://nvidia.box.com/shared/static/wa34qwrwtk9njtyarwt5nvo6imenfy26.whl)，下载后得到文件`torch-1.7.0-cp36-cp36m-linux_aarch64.whl`.


```bash
sudo sudo apt-get install python3-pip libopenblas-base libopenmpi-dev
pip3 install Cython
pip3 install numpy torch-1.7.0-cp36-cp36m-linux_aarch64.whl
```

### 安装torchvision
```bash
sudo apt-get install libjpeg-dev zlib1g-dev
git clone --branch v0.8.1 https://github.com/pytorch/vision torchvision
cd torchvision
export BUILD_VERSION=0.8.1
sudo python3 setup.py install ## 这步需要编译，时间较长
```

## 校验

运行`python3`

```python
import torch
print(torch.__version__)
print('CUDA available: ' + str(torch.cuda.is_available()))
print('cuDNN version: ' + str(torch.backends.cudnn.version()))
a = torch.cuda.FloatTensor(2).zero_()
print('Tensor a = ' + str(a))
b = torch.randn(2).cuda()
print('Tensor b = ' + str(b))
c = a + b
print('Tensor c = ' + str(c))

import torchvision
print(torchvision.__version__)
```

python3交互式控制台会输出类似下面的语句：
```txt
1.7.0
CUDA available: True
cuDNN version: 8000
Tensor a = tensor([0., 0.], device='cuda:0')
Tensor b = tensor([ 0.3777, -0.5432], device='cuda:0')
Tensor c = tensor([ 0.3777, -0.5432], device='cuda:0')
0.8.0a0+45f960c
```


## 参考

[pytorch for jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-7-0-now-available)