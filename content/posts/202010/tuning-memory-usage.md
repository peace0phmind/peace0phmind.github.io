---
title: "调整内存使用"
date: 2020-10-29T11:00:47+08:00
draft: false
---
nano分4G版和2G版。其SD镜像分别为：[4G版](https://developer.nvidia.com/jetson-nano-sd-card-image)，[2G版](https://developer.nvidia.com/jetson-nano-2gb-sd-card-image)。

---

4G和2G内存版本的主要区别在于启动后的桌面，2G内存版考虑到内存少的情况，启用的是LXDE的桌面。（切换到level 3后, 4G版镜像比2G版镜像多0.1G，jtop观察前者0.4G,后者0.3G）

## 禁用桌面GUI

考虑到nano的内存紧缺，如果不是直接在nano上进行GUI开发调试，那么会考虑使用level 3的方式启动nano。禁用桌面可以节省(Unity/GNOME 大概 800MB, LXDE可以节省大概250MB）内存。

禁用桌面
```
sudo init 3
```

启用桌面
```
sudo init 5
```

如果希望修改系统默认启动行为，则输入如下命令：

默认启动到控制台界面(level 3)：
```
sudo systemctl set-default multi-user.target
```

默认启动到图形界面(level 5):
```
sudo systemctl set-default graphical.target
```

## 创建swap文件(可选)
2G版本nano在启动配置时可以选择添加swap，也可以使用jtop工具通过界面配置swap文件的启用和大小。

此处给出手动创建和启用swap文件的方法：
假设需要创建4GB swap文件：

```
sudo fallocate -l 4G /mnt/4GB.swap
sudo mkswap /mnt/4GB.swap
sudo swapon /mnt/4GB.swap
```

将下面行添加到`/etc/fstab`文件中
```
/mnt/4GB.swap  none  swap  sw 0  0
```

## 创建swap分区(可选)
通过disks工具在磁盘上创建一个单独的分区，假设新建分区`/dev/sda1`

```
sudo mkswap /dev/sda1

# get the new partition id: xxx-xxx-xxx
sudo blkid /dev/sda1

# write config to file
echo "xxx-xxx-xxx none swap sw 0 0" | sudo tee -a /etc/fstab
```

重新启动操作系统。

## 参考

[How to Add a Swap Partition on Jetson TX1](https://jkjung-avt.github.io/swap-on-tx1/)

[How do I add swap after system installation?](https://askubuntu.com/questions/33697/how-do-i-add-swap-after-system-installation)