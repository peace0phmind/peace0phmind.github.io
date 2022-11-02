---
title: "人体姿势识别"
date: 2020-11-06T18:51:12+08:00
draft: false
---

本文尝试运行trt_pose项目。

## 安装依赖

1. 安装PyTorch和Torchvision, 参见[安装Pytorch和Torchvision](../install-pytorch-torchvision/)

1. 安装 [torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)
```
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
cd torch2trt
sudo python3 setup.py install --plugins
```

1. 安装其它依赖
```
sudo pip3 install tqdm cython pycocotools
sudo apt-get install python3-matplotlib
```

## 安装trt_pose

```
git clone https://github.com/NVIDIA-AI-IOT/trt_pose
cd trt_pose
sudo python3 setup.py install
```

## 安装jetcam

jetcam是一个jetson下操作usb和csi摄像头的库。

jetcam运行依赖模块traitlets，需先安装traitlets。
```
sudo pip3 install traitlets
```

然后安装jetcam
```
git clone https://github.com/NVIDIA-AI-IOT/jetcam
cd jetcam
sudo python3 setup.py install
```

## 运行示例

```python {linenos=true}
import time

t0 = time.time()
torch.cuda.current_stream().synchronize()
for i in range(50):
    y = model_trt(data)

torch.cuda.current_stream().synchronize()
t1 = time.time()

print(50.0 / (t1 - t0))
```

## 参考

[trt_pose](https://github.com/NVIDIA-AI-IOT/trt_pose)