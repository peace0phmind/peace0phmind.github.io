---
title: "AGX添加nvme ssd并设置从ssd启动"
date: 2020-10-22T16:51:33+08:00
draft: false
---

AGX出厂自带32G EMMC，并自带Ubuntu 18.04 + JetPack 4.4。本文对EMMC进行了磁盘读写的测试，并且对AGX进行改装，分别测试加装了海康的1T nvme ssd硬盘和SAMSUNG 1T nvme ssd，并进行了对比测试。最后简单介绍了了如何将AGX的默认启动方式修改为从nvme的ssd启动。

## 磁盘读写性能测试方式

使用linux下的dd进行磁盘读写性能测试。

### 测试磁盘写速度
```
sync; dd if=/dev/zero of=tempfile bs=1M count=1024; sync
```

### 测试磁盘读速度
```
dd if=tempfile of=/dev/null bs=1M count=1024
```

### 清理读缓存
```
sudo /sbin/sysctl -w vm.drop_caches=3
```

## emmc性能测试

### emmc写盘和覆盖写
1. emmc写盘1.4 GB/s(实际测试结果输出后，该民令并没有立即结束，所以这里的数据并不能用于参考)
1. emmc覆盖写的速度大概在119 MB/s
![emmc写盘和覆盖写](/images/202010/add-nvme-ssd/emmc-write-rewrite.png)

### emmc缓存读和直接读的速度
1. emmc缓存读的速度很高，在7.7GB/s左右
1. emmc直接读取的速度很低，在307 MB/s左右

![emmc缓存读和直接读的速度](/images/202010/add-nvme-ssd/emmc-cacheread-directread.png)

## SamSung 1T SSD性能测试

### SamSung写盘和覆盖写
1. SamSung写盘1.3 GB/s
1. SamSung覆盖写的速度大概在897 MB/s
![SamSung写盘和覆盖写](/images/202010/add-nvme-ssd/samsung-write-rewrite.png)

### SamSung缓存读和直接读的速度
1. SamSung缓存读的速度很高，在7.1GB/s左右
1. SamSung直接读取的速度很低，在1.7 GB/s左右

![SamSung缓存读和直接读的速度](/images/202010/add-nvme-ssd/samsung-cacheread-directread.png)

## HikVision 1T SSD性能测试

### HikVision写盘和覆盖写
1. HikVision写盘1.3 GB/s
1. HikVision覆盖写的速度大概在992 MB/s
![HikVision写盘和覆盖写](/images/202010/add-nvme-ssd/HikVision-write-rewrite.jpg)

### HikVision缓存读和直接读的速度
1. HikVision缓存读的速度很高，在7.9GB/s左右
1.HikVision直接读取的速度很低，在1.6 GB/s左右

![HikVision缓存读和直接读的速度](/images/202010/add-nvme-ssd/HikVision-cacheread-directread.jpg)

## 对比

HikVision 1T和SamSung 1T的性能相近，价格前者8百不到，后者1200左右，相差400左右，我先买了HikVision后购买并替换为了SamSung的ssd，下面介绍下原因：

先看下两个ssd的照片对比，上面为HikVison，下面为SamSung：

正面对比，差别不大
![正面对比](/images/202010/add-nvme-ssd/compare-front.jpg)

背面对比：从背面看SamSung的背面没有元器件，Hikision的有很多细小密集的元器件。
![背面对比](/images/202010/add-nvme-ssd/compare-back.jpg)

从HikVision装配图来看,背面有元器件会导致整个ssd中间突起。
![HikVision装配图](/images/202010/add-nvme-ssd/HikVision-added.jpg)

替换下来的HikVision，已经有轻微变形了。
![替换下来的HikVision](/images/202010/add-nvme-ssd/HikVision-single.jpg)

从SamSung装配图来看,背面没有元器件会非常贴合Agx的PCI-E接口。
![SamSung装配图](/images/202010/add-nvme-ssd/samsung-added.jpg)

## 修改启动盘，从ssd启动

1. 完成物理装配后开机
1. 在Disks工具中找到1T SSD，点击小齿轮，对整个磁盘进行format创建一个大分区（有别于参考中，还要预留16G空间，此处使用完整空间）。完成format后，保持磁盘在unmount状态。

![disks tools](/images/202010/add-nvme-ssd/disks-with-1t-ssd.png)

1. 打开命令行，执行下面命令：（`注： 在我的disks中，我的磁盘名称为/dev/nvme0n1，而不是参考中的/dev/nvme0n1p1，可能与我使用的jetpack 4.4.1有关，所以我修改了代码以保证程序可以运行`）

```
# clone the repository:
git clone https://github.com/peace0phmind/rootOnNVMe.git

# switch to that repository's directory
cd rootOnNVMe

# copy the rootfs of the eMMC card to the SSD
./copy-rootfs-ssd.sh

# Finally, we will add a service which will run a script when the system starts up. 
./setup-service.sh
```

## 参考
[Install NVMe SSD on NVIDIA Jetson AGX Developer Kit](https://www.jetsonhacks.com/2018/10/18/install-nvme-ssd-on-nvidia-jetson-agx-developer-kit/)

[Jetson Xavier NX – Run from SSD](https://www.jetsonhacks.com/2020/05/29/jetson-xavier-nx-run-from-ssd/)