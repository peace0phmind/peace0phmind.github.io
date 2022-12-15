---
title: "Ddns"
description: "ddns"
keywords: "ddns"

date: 2022-12-15T09:06:42+08:00
lastmod: 2022-12-15T09:06:42+08:00

author: peace0phmind
url: "posts/202212/ddns"

draft: true

categories:
  -
tags:
  - ddns

---


## 介绍

每台连接到Internet的计算机都有一个IP地址。域名解析是将名称（如“www.google.com”）与IP地址（如“74.125.19.103”）相关联的过程，以便可以使用易于记忆的名称访问计算机上的网站（或其他服务）名称，而不是计算机的IP地址编号。域名解析是通过称为域名系统的分布式数据库实现的。

该数据库由DNS域名服务器在Internet上实现，这些服务器跟踪DNS记录并在彼此之间交换此信息以保持一致性。然后，每次域名解析都会定向到这些名称服务器之一。

Internet上的大多数服务器都有一个固定的（静态的）IP地址，永远不会改变。此节点的DNS记录不会经常更改。

然而许多家庭用户分配的IP地址更改得更频繁。这些动态IP地址由ISP分配。这使得将名称转换为这些IP地址成为一项挑战。

许多DNS域名服务器提供了一种使用动态IP名称转换更新DNS数据库的方法。这是通过在他们的计算机或本地路由器上使用一个小型软件实用程序来完成的。

这些动态DNS服务允许用户选择一个主机名并设置一个初始IP地址以对应于该主机名。然后，该软件实用程序会定期检查计算机IP地址的更改，当发现新IP地址时，它会更新动态DNS数据库以反映该更改。

## 设置动态DNS服务更新

选择动态DNS服务提供商后，您需要设置一种方式，以便在您的IP地址记录发生更改时进行更新。有两种方法可以做到这一点：
1. 使用安装在您计算机上的动态DNS软件实用程序
2. 使用电缆/DSL调制解调器/路由器的内置功能

许多路由器/调制解调器直接支持动态DNS报告/通知/更新。如果您的路由器的配置可以从Web浏览器访问，请尝试通过登录路由器的本地IP地址（例如http://10.1.1.1/或http://192.168.0.1/）来访问它并查找动态DNS(DDNS)设置。

但是，即使您的调制解调器/路由器确实支持动态DNS报告，在某些情况下您可能仍希望使用计算机上的软件实用程序来执行更新：
1. 您同时使用多个动态DNS服务（大多数路由器一次只能提供一项服务）
2. 路由器不支持您的特定动态DNS服务
3. 您的服务器位于并非始终连接到同一网络/路由器/调制解调器的移动计算机（例如笔记本电脑）上。

## 使用软件实用程序执行动态DNS更新

有几个可用的实用程序。每个动态DNS服务可能与特定的实用程序一起工作得更好。（您可能需要将Ubuntu Universe添加到您的软件存储库集中以安装其中一些实用程序。请参阅安装软件。）

### ddclient

ddclient是用于动态DNS更新的原始Linux实用程序。ddclient wiki列出了几个动态DNS服务的一些配置。更多信息可以在ddclient论坛上找到。以下部分改编自Ubuntuguide.org动态IP服务器。

#### 使用软件包管理器或使用命令行界面安装ddclient

```bash
sudo apt-get install ddclient
```

如果这是您第一次安装ddclient，安装脚本会提示您输入您在DynDNS（或其他动态DNS服务）注册的主机名。您还将被提示输入您在动态DNS服务中注册的用户名/密码。最后，系统会询问您主要使用哪个以太网端口连接到Internet（通常是eth0用于有线或wlan0用​​于无线）。大多数情况下，您只需执行此操作即可使实用程序正常运行。

但是，您也可以稍后编辑ddclient配置文件以满足您的特定需求（或者如果您对服务、主机名或其他变量进行更改）。

#### 编辑ddclient配置文件

```bash
sudo nano /etc/ddclient.conf
```

```text
# 设置更新间隔的秒数
daemon=300

pid=/var/run/ddclient.pid
#use=if, if=eth0
# 要使用DynDNS的checkip服务（它将自动检测您当前的IP地址）
use=web, web=checkip.dyndns.com/, web-skip='IP Address'

# Login and change the values at the DynDNS site, using SSL.
protocol=dyndns2
# 使用安全的SSL通信
ssl=yes

server=members.dyndns.org
login=myDynDNSusername
password='myDynDNSuserpassword'
mysite_1.dynds.org,mysite_2.dyndns.org,mysite_3.dyndns.org
```

注意：如果这不起作用，请尝试将web-skip更改为“当前地址”
注意：密码必须用引号引起来，例如DynDNS的'myDynDNSuserpassword'。

### cron + python
略


## Reference

[DynamicDNS](https://help.ubuntu.com/community/DynamicDNS)