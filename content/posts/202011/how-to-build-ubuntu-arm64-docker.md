---
title: "分析Ubuntu Arm64 Docker Build"
date: 2020-11-21T17:25:57+08:00
draft: false
---

Ubuntu的Arm64 Docker Image项目在：
[docker-brew-ubuntu-core](https://github.com/tianon/docker-brew-ubuntu-core)

该项目需要配合[Jenkins pipe line](https://github.com/docker-library/oi-janky-groovy/blob/master/tianon/update-ubuntu-pipeline.groovy)文件执行。

文件首先删除[docker-brew-ubuntu-core](https://github.com/tianon/docker-brew-ubuntu-core)工程的对应arm64分支`dist-amd64`，并重新创建该分支，在该分支各ubuntu版本下创建`Dockerfile`，下载构造文件并归档到git仓库。

具体参考：[docker-brew-ubuntu-core](https://github.com/tianon/docker-brew-ubuntu-core)


最后，docker下官方提供的arm64的资源在[arm64v8](https://hub.docker.com/u/arm64v8)用户下。

另一个优质的docker arm资源在[balena.io](https://www.balena.io/docs/reference/base-images/base-images-ref/),项目地址在[balena-io-library jetson-xavier](https://github.com/balena-io-library/base-images/tree/master/balena-base-images/device-base/jetson-xavier)
