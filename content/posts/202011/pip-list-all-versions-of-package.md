---
title: "列举pip可安装组件的版本信息"
date: 2020-11-13T15:13:02+08:00
draft: false
---

## 方法1

在需要安装组件名称后添加`==`符号，pip会自动列举可安装版本信息。

输入：
```
pip3 install pyqt5==
```

得到：
```
 Could not find a version that satisfies the requirement pyqt5== (from versions: 5.14.0, 5.14.1, 5.14.2, 5.15.0, 5.15.1)
```

## 其他方法参考

[Python and pip, list all versions of a package that's available](https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available)