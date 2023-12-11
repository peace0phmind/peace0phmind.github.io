---
title: "01 ffmpeg"
description: "01-ffmpeg"
keywords: "ffmpeg"

date: 2023-12-11T15:19:57+08:00
lastmod: 2023-12-11T15:19:57+08:00

author: peace0phmi1nd
url: "posts/202312/107-ffmpeg"

draft: true

categories:

- ml
  tags:
- Convolutional
- Neural
- Network

---

## 将rtsp流保存为文件，并指定录制时长,

- i 参数指定输入文件或输入源。在这种情况下，它指定了一个通过RTSP协议访问的视频文件的地址。
- t 参数用于指定输出文件的持续时间（秒）。在本例中，输出文件将被剪辑为只包含前 10 秒的内容。
- c:v 参数指定视频编码器。在这里使用的是 libx264 编码器
- c:a 参数指定音频编码器。这里使用的是 AAC（Advanced Audio Coding）编码器，它是一种广泛支持的音频编码格式。
- force_key_frames "expr:gte(t,n_forced*3)" 表示将关键帧设置为每隔 3 秒生成一次。expr:gte(t,n_forced*3) 是一个表达式，其中
  t 是当前时间，n_forced 是已经生成的关键帧数量，gte 表示大于等于的条件
- abc.mp4 输出文件的名称和格式

```bash
ffmpeg -i rtsp://admin:Zyx123456@192.168.1.26 -t 10 -c:v libx264 -c:a aac -force_key_frames "expr:gte(t,n_forced*3)" abc.mp4
```

## 将视频中的某一秒保存为图片

- i 是输入视频文件的名称
- ss 00:00:03 指定了要从第3秒开始进行截取。可以根据需要修改时间值，格式为 HH:MM:SS
- vframes 1 表示只截取一帧图像
- output.jpg 是输出图像文件的名称和格式。

```bash
ffmpeg -i abc.mp4 -ss 00:00:03 -vframes 1 output.jpg
```

## 将视屏裁剪为多个小块视频

```bash
ffmpeg -i abc.mp4 -filter_complex "[0:v]crop=200:100:0:0[out1];[0:v]crop=800:600:200:200[out2]" -map "[out1]" sub-1.mp4 -map "[out2]" sub-2.mp4
```

## 将图片裁剪为多个小块图片

```bash
ffmpeg -i output.jpg -filter_complex "[0:v]crop=200:100:0:0[out1];[0:v]crop=800:600:200:200[out2]" -map "[out1]" -frames:v 1 sub-image1.jpg -map "[out2]" -frames:v 1 sub-image2.jpg
```

## 调整分辨率大小

```bash
ffmpeg -i movie.mp4 -vf "scale=800:600" -c:a copy resized_movie.mp4
```

## 视屏拼接

```bash
ffmpeg -i resized_movie.mp4 -i sub-2.mp4 -filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" finish.mp4
ffmpeg -i resized_movie.mp4 -i sub-2.mp4 -filter_complex "[0:v:0][1:v:0]concat=n=2:v=1:a=0[outv]" -map "[outv]" finish.mp4
ffmpeg -i resized_movie.mp4 -i sub-2.mp4 -filter_complex "[0:v:0][1:v:0]concat=n=2:v=1:a=0[outv]" -map "[outv]" -r 30 -pix_fmt yuv420p -b:v 2000k finish.mp4
```