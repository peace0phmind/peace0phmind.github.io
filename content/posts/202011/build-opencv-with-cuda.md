---
title: "编译最新opencv 4.4.0 with cuda"
date: 2020-11-03T15:23:50+08:00
draft: false
---

本文介绍如何在nano/agx上编译opencv 4.4.0 with cuda.

## 步骤

该库在原有库基础上做了一些调整，原有库在nano上只能单线程运行。需要原有库的同学参见参考连接。

```
# clone the repository
git clone https://github.com/peace0phmind/nano_build_opencv.git

cd nano_build_opencv

./build_opencv.sh

```


## 参考

[nano_build_opencv](https://github.com/mdegans/nano_build_opencv)