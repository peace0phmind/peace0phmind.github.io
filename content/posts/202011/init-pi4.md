---
title: "Raspberry PI4环境初始化"
date: 2020-11-18T18:45:20+08:00
draft: false
---

## pi 4准备

安装最新的pi镜像: [2020-08-20-raspios-buster-armhf](https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2020-08-24/2020-08-20-raspios-buster-armhf.zip)

## 配置apt代理

```
sudo nano /etc/apt/apt.conf
```

添加下面语句到文件中：其中如果代理不需要登陆。username:password@可省略；ip和port请按照实际情况填写。

```
Acquire::http::Proxy "http://username:password@ip:port";
```

## 更新操作系统到最新

```
sudo apt update
sudo apt upgrade
```

## 安装bcmstat

[bcmstat](https://github.com/MilhouseVH/bcmstat)可以检测到如下指标：

CPU fequencies (ARM, Core, H264, V3D, ISP)
Temperature (current and peak) for Core and/or PMIC
IRQ/s
Network Rx/Tx
System utilisation (percentage user, nice, idle etc.)
CPU load (including individual cores when available)
GPU mem usage
RAM usage (with/without swap)
Memory leak detection (D/A options - instantaneous and accumulated memory deltas)
Undervoltage, ARM frequency cap and temperature throttle event monitoring
Customisable columns

安装方式：
```
curl -Ls https://raw.githubusercontent.com/MilhouseVH/bcmstat/master/bcmstat.sh -o ~/bin/bcmstat.sh
chmod +x ~/bin/bcmstat.sh
```

添加环境变量到.profile，logout再login

```
export PATH=$PATH:~/bin
```

添加一个默认配置文件
```
echo "xgd10" >> ~/.bcmstat.conf
```

## 安装golang

下载[go1.15.5.linux-armv6l](https://dl.google.com/go/go1.15.5.linux-armv6l.tar.gz)

执行下面命令：
```
sudo tar -C /usr/local -xzf go1.15.5.linux-armv6l.tar.gz
```

添加下面语句到.profile中
```
export PATH=$PATH:/usr/local/go/bin
```
