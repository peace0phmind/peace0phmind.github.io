---
title: "LVM"
description: "lvm"
keywords: "lvm"

date: 2022-12-13T10:37:56+08:00
lastmod: 2022-12-13T10:37:56+08:00

author: peace0phmind
url: "posts/202212/lvm"

draft: true

categories:
  -
tags:
  - lvm

---

## 介绍
- Physical Volumes (PV): 物理卷, 对应实际的物理磁盘 (如： /dev/sda, /dev,sdb 等)
- Volume Groups (VG)： 卷组, 由物理卷组成（如： vg=/dev/sda + /dev/sdb）
- Logical Volumes (LV): 逻辑卷, 由卷组划分而来

## 显示信息

### 显示物理卷信息

键入以下命令以查看有关物理卷的信息
```bash
sudo pvs
```

要查看详细的物理卷属性信息
```bash
sudo pvdisplay
```

### 显示卷组信息

键入以下命令以查看有关卷组的信息

```bash
sudo vgs
```

要查看详细的卷组属性信息
```bash
sudo vgdisplay
```

### 显示逻辑卷信息

键入以下命令以查看有关逻辑卷的信息

```bash
sudo lvs
```

要查看详细的逻辑卷属性信息
```bash
sudo lvdisplay
```

### 查找磁盘信息
```bash
# list all disk
sudo fdisk -l
# list all disk with grep
sudo fdisk -l | grep '^Disk /dev/'
```

## 扩展LVM

### 创建新的PV

```bash
sudo pvcreate /dev/sdb
# or [-f] 强制创建PV。[-ff] 强制创建PV，并覆盖现有磁盘(忽略磁盘检查)
sudo pvcreate -ff /dev/sdc
```

如果执行上述命令出现`device is partitioned`，那么进行下面检查:
```bash
sudo fdisk -l /dev/sdb
```
如果出现类似`Disklabel type: gpt`的字样那么需要进行额外的操作。(当您拥有GPT（GUID 分区表）时可能会发生这种情况。不幸的是，这甚至不能用 -f 强制执行)

```bash
sudo wipefs --all --backup /dev/sdb
```
执行上述命令后，直接执行`sudo pvcreate /dev/sdb`，提示成功

### 将新的pv添加到vg中
```bash
sudo vgextend vgubuntu /dev/sdb
```

### 扩展对应的lv
```bash
sudo lvm lvextend -l +100%FREE /dev/vgubuntu/root
```

### 扩展对应的分区
```bash
df -h
sudo resize2fs -p /dev/mapper/vgubuntu-root
df -h
```