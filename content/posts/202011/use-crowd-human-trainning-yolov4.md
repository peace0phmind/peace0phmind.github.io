---
title: "使用CrowdHuman训练Yolov4"
date: 2020-11-13T12:22:37+08:00
draft: false
---

本文介绍在agx上使用旷视CrowdHuman库训练yoloV4模型。

## 数据准备

```
git clone https://github.com/jkjung-avt/yolov4_crowdhuman

cd yolov4_crowdhuman/data

./prepare_data.sh 960x960
```

## 在agx上训练

```
git clone https://github.com/AlexeyAB/darknet.git


```