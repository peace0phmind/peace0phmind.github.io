---
title: "Jetson Nano环境初始化"
date: 2020-10-28T15:31:36+08:00
draft: false
---

    本文主要介绍Jetson Nano启动后环境的准备工作.


## TF卡flush以及系统启动初始化

下载并烧录最新的TF卡镜像[4G内存版](https://developer.nvidia.com/jetson-nano-sd-card-image) ; [2G内存版](https://developer.nvidia.com/jetson-nano-2gb-sd-card-image)。完成nvidia的一系列初始化操作（协议，时区配置，账号信息配置等）。

## Ubuntu 系统的更新

```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
sudo apt autoremove
```

## 安装ohmyzsh
个人比较喜欢ohmyzsh下的一些快捷输入和操作方式。
由于墙的存在，直接安装会失败，可以手动安装

首先需要安装zsh
```
sudo apt install zsh -y
```

手动安装ohmyzsh
```
# Clone the repository
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh

# Optionally, backup your existing ~/.zshrc file
cp ~/.zshrc ~/.zshrc.orig

# Create a new zsh configuration file
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# Change your default shell
chsh -s $(which zsh)
```

## 安装ohmyzsh的zsh-autosuggestions插件
zsh-autosuggestions插件支持超棒的历史命令联想功能。

```
# Clone this repository into $ZSH_CUSTOM/plugins (by default ~/.oh-my-zsh/custom/plugins)
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Add the plugin to the list of plugins for Oh My Zsh to load (inside ~/.zshrc):
plugins=(zsh-autosuggestions)

# Start a new terminal session.
```

## 安装jdk

```
sudo apt install openjdk-8-jdk -y
```

## 安装terminator
terminator是ubuntu下比较美观，且支持分屏的工具。其可以类比为mac下的iterm2。

```
sudo apt install terminator -y
```

## 安装pip3

```
sudo apt install python3-pip -y
```

## 安装jtop

jtop可以用来显示系统资源使用情况，比如：查看cpu，内存，gpu使用情况；查看安装的库的信息；控制风扇启用和转速等。

```
sudo -H pip3 install -U jetson-stats
sudo systemctl restart jetson_stats.service
```

使用前还需要logout或者reboot

## 使用jtop启用jetson_clocks
在不启用jetson_clocks时，jetson的cpu和gpu的主频是根据需要动态变化的，且如果支持PWM的风扇默认也是不工作的（Fan转速为0，如果是普通的3pin风扇则会持续稳定运行。只有4pin的调速风扇会受到jetson_clocks的影响控制转速）。建议启用jetson_clocks，将主频固定下来。在GUI界面，未启用jetson_clocks时会有卡顿的现象。

输入`jtop`启动jtop，按`5`进入控制界面：
1. 点击`system`按钮，启用Fan转速的Auto模式
1. 点击`jetson_clocks`左边的`s`按钮，启动jetson_clocks
1. 点击`boot`左边的`e`，设置jetson_clocks系统启动自动运行


## 安装golang环境

从[golang下载页面](https://golang.org/dl/)下载最新的[go1.15.3.linux-arm64安装包](https://golang.org/dl/go1.15.3.linux-arm64.tar.gz)

执行下面命令安装golang到/usr/local目录下:
```
sudo tar -C /usr/local -xzf go1.15.3.linux-arm64.tar.gz
```

将/usr/local/go/bin目录添加到PATH环境变量，参见
```
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
```

## 安装curl

curl 支持 http, https, socks4, socks5 代理
wget 支持 http, https 代理

而socks5支持dns代理，可以解决一些dns污染的问题

```
sudo apt install curl -y
```

## 配置nvcc环境变量

拷贝下面代码到.bashrc或.zshrc文件(如果你安装使用了zsh)，或者.profile或.zprofile文件。
关于[.*rc和.*profile文件的使用说明参见](https://superuser.com/questions/187639/zsh-not-hitting-profile)

```
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```


## 配置docker权限

1. 创建 `docker` 组(可选，nano中已包含docker组)
1. 将当前用户添加到 `docker` 组中
1. 激活组变化

```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

当激活了组变化后，执行`docker ps` 可以看到docker命令正确执行。

## 配置docker registry mirrors

配置docker registry mirrors可以进行docker pull加速，解决docker pull缓慢的问题。

使用编辑器打开`/etc/docker/daemon.json`文件，按json格式添加如下内容：

```
"registry-mirrors": ["https://registry.docker-cn.com"]
```

此处url也可使用阿里云的个人docker加速器，例如：https://xxxxx.mirror.aliyuncs.com，这里[xxxx参见](https://developer.aliyun.com/article/29941)

添加完后，`daemon.json`文件内容类似如下：
```
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    },
    "registry-mirrors": ["https://7s7m9b11.mirror.aliyuncs.com"]
}
```

## 安装 docker-compose
```
sudo apt install docker-compose -y
```

## 安装右键resize image工具

```
sudo apt install nautilus-image-converter
```

上面命令安装完成后，执行下面命令重启nautilus

```
nautilus -q
```
