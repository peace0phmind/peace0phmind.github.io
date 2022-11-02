---
title: "在Pi4上编译ffmpeg支持硬件编解码以及测试和使用方法"
date: 2020-11-19T15:27:31+08:00
draft: false
---

由于某些原因，需要在raspberry pi 4上编译最新版本ffmpeg，下面是方法以及测试方案。

## 编译准备

```
sudo apt update
sudo apt upgrade
```

## 安装必要的工具和库

```
sudo apt install build-essential yasm pkg-config libx264-dev
```

## 下载源代码并编译

```
# 下载并解压
wget http://ffmpeg.org/releases/ffmpeg-snapshot-git.tar.bz2
tar jxvf ffmpeg-snapshot-git.tar.bz2
cd ffmpeg

# 切换到明确的tag并创建分支
git checkout tags/n4.3.1 -b b4.3.1

./configure --enable-gpl --enable-libx264 --enable-mmal --enable-omx --enable-omx-rpi

## pi4 2G上大约需要14分钟左右，请注意cpu散热
make -j4

sudo make install
```

## 测试rtsp h.264，1080p的cpu解码，并每5s保存一张图片

```
ffmpeg -rtsp_transport tcp -nostdin -loglevel error -i rtsp://username:password@ip -filter:v fps=fps=1/5 test_%03d.jpg
```

通过[bcmstat](https://github.com/MilhouseVH/bcmstat)软件观察，cpu消耗每路17%,内存消耗较少，约60MB。

## 测试rtsp h.264，1080p硬解，并每5s保存一张图片

首先需要配置GPU内存到300MB左右，默认76MB，配置路径为：Start->Preferences->Raspberry Pi Configuration->Performance->GPU Memory

```
ffmpeg -c:v h264_mmal -rtsp_transport tcp -nostdin -loglevel error -i rtsp://username:password@ip -filter:v fps=fps=1/5 test_%03d.jpg
```

通过[bcmstat](https://github.com/MilhouseVH/bcmstat)软件观察，cpu消耗一路9%左右，内存消耗也需要60MB，另外需要GPU mem约94MB。

`注`:使用GPU硬解码两路时，cpu上升到28%左右，内存和gpu内存也等比上升。

## 结论

使用pi的h264硬件解码时，除GPU额外内存消耗较大外，节省的cpu使用率也很少。当然，目前仅进行了ffmpeg的测试，并未通过其他软件来证实是芯片自生问题还是ffmpeg硬件解码算法问题。建议大家使用ffmpeg解码时，仅进行一路硬解。

## 参考

[Compile FFmpeg for Ubuntu, Debian, or Mint](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)

[Hardware Encoding with the Raspberry Pi](https://www.redhenlab.org/home/the-cognitive-core-research-topics-in-red-hen/the-barnyard/hardware-encoding-with-the-raspberry-pi)

