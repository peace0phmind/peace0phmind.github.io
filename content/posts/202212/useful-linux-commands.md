---
title: "Useful linux commands"
description: "useful-linux-commands"
keywords: "linux"

date: 2022-12-06T16:22:41+08:00
lastmod: 2022-12-06T16:22:41+08:00

author: peace0phmind
url: "posts/202212/useful-linux-commands"

draft: false

categories:
  - blog
tags:
  - linux

---

## create sudo enabled user
```bash
# add a new user to the system
sudo adduser <username>
# adding the user to the sudo group
sudo usermod -aG sudo <username>
# testing sudo access
sudo su - <username>
```

## run sudo command without a password
```bash
sudo visudo
# change under line to next line
# %sudo   ALL=(ALL:ALL) ALL
%sudo   ALL=(ALL:ALL) NOPASSWD:ALL
```

## install miniconda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh
bash Miniconda3-py38_4.12.0-Linux-x86_64.sh
```

### init miniconda
```bash
conda create --name <env_name> --clone base
nano ~/.zshrc
# add under line in the bottom of ~/.zshrc
conda activate s232
```
