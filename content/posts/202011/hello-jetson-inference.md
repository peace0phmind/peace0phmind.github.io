---
title: "Hello Jetson Inference"
date: 2020-11-05T13:11:47+08:00
draft: false
---

本文尝试运行`Hello AI World`,`Hello AI World` 主要包括：图像分类、物体识别、图像分割。

## Jetson nano安装JetPack
略，参见[Jetson Nano环境初始化](../../202010/nano-env-init)

## 编译项目

更新系统，并安装必要的工具
```
sudo apt update
sudo apt upgrade
sudo apt install git cmake libpython3-dev python3-numpy
```

clone项目并进行编译，中间会提示下载模型，可以直接点击ok，下载默认的几个模型
```
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build
cd build
cmake ../
make -j$(nproc)
sudo make install
sudo ldconfig
```



pytorch的安装，参见[安装Pytorch和Torchvision](../install-pytorch-torchvision)

## 验证

切换到jetson-inference工程编译目录的bin目录下：
```
cd jetson-inference/build/aarch64/bin
```

### 图像分类

首次运行命令，TensorRT会花费较长时间进行网络优化，优化后的网络文件会缓存在磁盘上，下次运行直接加载优化后的模型。

```
# C++
./imagenet images/orange_0.jpg images/test/output_0.jpg

# Python
./imagenet.py images/orange_0.jpg images/test/output_0.jpg

# C++
./imagenet images/strawberry_0.jpg images/test/output_1.jpg

# Python
./imagenet.py images/strawberry_0.jpg images/test/output_1.jpg
```

可以使用`--network`关键字指定使用什么网络，默认未指定系统默认使用`googlenet`：
```
# C++
./imagenet --network=resnet-18 images/jellyfish.jpg images/test/output_jellyfish.jpg

# Python
./imagenet.py --network=resnet-18 images/jellyfish.jpg images/test/output_jellyfish.jpg

# C++
./imagenet --network=resnet-18 images/stingray.jpg images/test/output_stingray.jpg

# Python
./imagenet.py --network=resnet-18 images/stingray.jpg images/test/output_stingray.jpg
```

项目支持的完整的模型列表参见：[Classifying Images with ImageNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md)

检测rtsp流:(这里的admin:123456为摄像头的用户名和密码，请根据实际情况填写用户名、密码和IP地址)
```
./imagenet rtsp://admin:123456@192.168.1.26
```

### 物体识别

首次运行命令，TensorRT会花费较长时间进行网络优化，优化后的网络文件会缓存在磁盘上，下次运行直接加载优化后的模型。

```
# C++
./detectnet --network=ssd-mobilenet-v2 images/peds_0.jpg images/test/output_peds_0.jpg

# Python
./detectnet.py --network=ssd-mobilenet-v2 images/peds_0.jpg images/test/output_peds_0.jpg

# C++
./detectnet images/peds_1.jpg images/test/output_peds_1.jpg

# Python
./detectnet.py images/peds_1.jpg images/test/output_peds_1.jpg
```

项目支持的完整的模型列表参见：[Locating Objects with DetectNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-console-2.md)


检测rtsp流:(这里的admin:123456为摄像头的用户名和密码，请根据实际情况填写用户名、密码和IP地址)
```
./detectnet rtsp://admin:123456@192.168.1.26
```

### 图像分割

```
# C++
./segnet --network=fcn-resnet18-cityscapes images/city_0.jpg images/test/output_city_0.jpg

# Python
./segnet.py --network=fcn-resnet18-cityscapes images/city_0.jpg images/test/output_city_0.jpg

# C++
./segnet --network=fcn-resnet18-deepscene images/trail_0.jpg images/test/output_trail_0.jpg

# C++
./segnet --network=fcn-resnet18-deepscene --visualize=mask images/trail_0.jpg images/test/output_mask_trail_0.jpg


# C++
./segnet --network=fcn-resnet18-mhp images/humans_0.jpg images/test/output_humans_0.jpg

# Python
./segnet.py --network=fcn-resnet18-mhp images/humans_0.jpg images/test/output_humans_0.jpg
```

项目支持的完整的模型列表参见：[Semantic Segmentation with SegNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/segnet-console-2.md)


检测rtsp流:(这里的admin:123456为摄像头的用户名和密码，请根据实际情况填写用户名、密码和IP地址)
```
./segnet --network=fcn-resnet18-deepscene rtsp://admin:Zyx123456@192.168.1.26
```

## 参见

[Hello AI World](https://github.com/dusty-nv/jetson-inference)

[Building the Project from Source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

[Classifying Images with ImageNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md)

[Locating Objects with DetectNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-console-2.md)

[Semantic Segmentation with SegNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/segnet-console-2.md)