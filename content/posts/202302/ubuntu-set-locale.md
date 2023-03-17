---
title: "Ubuntu Set Locale"
description: "ubuntu-set-locale"
keywords: "ubuntu,set,locale"

date: 2023-03-17T16:09:51+08:00
lastmod: 2023-03-17T16:09:51+08:00

author: peace0phmind
url: "posts/202302/ubuntu-set-locale"

draft: false

categories:
  -
tags:
  - ubuntu
  - locale
---

### set locale
```bash
sudo apt-get install language-pack-en
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
source /etc/default/locale
```
Then, restart terminator.
