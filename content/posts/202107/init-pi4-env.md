---
title: "初始化pi4环境"
date: 2021-07-06T15:43:27+08:00
draft: false
---

## 更新环境
sudo apt update
sudo apt upgrade


## 安装docker

### Add Docker’s official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### set up the stable repository
```bash
echo "deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker Engine
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### 配置docker权限
1. 创建 `docker` 组(可选，nano中已包含docker组)
1. 将当前用户添加到 `docker` 组中
1. 激活组变化

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```


## install frpc

### create frpc.ini file
```bash
sudo mkdir /etc/frp
cd /etc/frp
sudo nano frpc.ini
```

add under line:
```txt
[common]
server_addr = xxx.xx.xx.xx
server_port = 7000


[pi-CM4-IO-POE-BOX-B-test]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6981
```

### start frpc
```
docker run --restart=always --network host -d -v /etc/frp/frpc.ini:/etc/frp/frpc.ini --name frpc snowdreamtech/frpc
```

## install golang
```
sudo tar -C /usr/local -xzf go1.16.5.linux-arm64.tar.gz
```

添加下面语句到.profile中
```
export PATH=$PATH:/usr/local/go/bin
```

