---
title: "Wireguard"
description: "wireguard"
keywords: "wireguard"

date: 2022-12-13T16:28:33+08:00
lastmod: 2022-12-13T16:28:33+08:00

author: peace0phmind
url: "posts/202212/wireguard"

draft: true

categories:
  -
tags:
  - wireguard

---

## 介绍
WireGuard®是一种极其简单但快速的现代VPN，它使用最先进的加密技术。它旨在比IPsec更快、更简单、更精简和更有用，同时避免令人头疼的问题。它旨在比OpenVPN具有更高的性能。WireGuard被设计为在嵌入式接口和超级计算机上运行的通用VPN，适用于许多不同的环境。最初是为Linux内核发布的，现在是跨平台的（Windows、macOS、BSD、iOS、Android）并且可以广泛部署。它目前正在大力发展，但它可能已经被认为是业内最安全、最容易使用和最简单的VPN解决方案。

### 简单易用
WireGuard旨在像SSH一样易于配置和部署。只需交换非常简单的公钥就可以建立VPN连接——就像交换SSH密钥一样——所有其余的都由WireGuard透明地处理。它甚至能够在IP地址之间漫游，就像Mosh一样。无需管理连接、关注状态、管理守护进程或担心引擎盖下的内容。WireGuard提供了一个极其基本但功能强大的界面。

### 加密可靠
WireGuard使用最先进的密码学，如Noise协议框架、Curve25519、ChaCha20、Poly1305、BLAKE2、SipHash24、HKDF和安全可信结构。它做出了保守而合理的选择，并得到了密码学家的审查。

### 最小的攻击面
WireGuard的设计考虑了易于实施和简单性。它旨在以极少的代码行轻松实现，并且易于审计安全漏洞。与像*Swan/IPsec或OpenVPN/OpenSSL这样的庞然大物相比，即使对于大型安全专家团队来说，审计巨大的代码库也是一项艰巨的任务，WireGuard意味着可以由单个人进行全面审查。

### 高性能
极高速加密原语和WireGuard存在于Linux内核中这一事实的结合意味着安全网络可以非常高速。它既适用于智能手机等小型嵌入式设备，也适用于满载的主干路由器。

### 定义明确且经过深思熟虑
WireGuard是经过漫长而全面考虑的学术过程的结果，产生了[技术白皮书](https://www.wireguard.com/papers/wireguard.pdf)，这是一份学术研究论文，明确定义了协议以及每个决定中的深入考虑。


## 概念概述

### 简单的网络接口

WireGuard的工作原理是添加一个（或多个）网络接口，如eth0或wlan0，称为wg0（或wg1、wg2、wg3等）。然后可以使用ifconfig(8)或ip-address(8)正常配置此网络接口，使用route(8)或ip-route(8)添加和删除它的路由，等等所有普通网络实用程序.接口的特定WireGuard方面是使用wg(8)工具配置的。此接口充当隧道接口。

WireGuard将隧道IP地址与公钥和远程端点相关联。当接口向对等体发送数据包时，它会执行以下操作：
1. 此数据包适用于192.168.30.8。那是哪个端点？让我看看...好吧，这是给同级ABCDEFGH的。（或者，如果它不适用于任何已配置的对等点，则丢弃该数据包。）
2. 使用对等ABCDEFGH的公钥加密整个IP数据包。
3. 对等ABCDEFGH的远程端点是什么？让我看看...好的，端点是主机216.58.211.110上的UDP端口53133。
4. 使用UDP通过Internet将步骤2中的加密字节发送到216.58.211.110:53133。

当接口收到数据包时，会发生以下情况：
1. 我刚从主机98.139.183.24上的UDP端口7361收到一个数据包。让我们解密吧！
2. 它为对等LMNOPQRS正确解密和验证。好的，让我们记住对等LMNOPQRS的最近Internet端点是使用UDP的98.139.183.24:7361。
3. 解密后，明文数据包来自192.168.43.89。是否允许对等LMNOPQRS以192.168.43.89的形式向我们发送数据包？
4. 如果是，则在接口上接受数据包。如果没有，放弃它。

### 密钥路由

WireGuard的核心是一个称为Cryptokey Routing的概念，它通过将公钥与隧道内允许的隧道IP地址列表相关联来工作。每个网络接口都有一个私钥和一个对等点列表。每个对等点都有一个公钥。公钥简短而简单，由对等方用来相互验证。它们可以通过任何带外方法在配置文件中使用，类似于将SSH公钥发送给朋友以访问shell服务器的方式。

例如，服务器计算机可能具有以下配置：

```
[Interface]
PrivateKey = yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk=
ListenPort = 51820

[Peer]
PublicKey = xTIBA5rboUvnH4htodjb6e697QjLERt1NAB4mZqp8Dg=
AllowedIPs = 10.192.122.3/32, 10.192.124.1/24

[Peer]
PublicKey = TrMvSoP4jYQlY6RIzBgbssQqY3vxI2Pi+y71lOWWXX0=
AllowedIPs = 10.192.122.4/32, 192.168.0.0/16

[Peer]
PublicKey = gN65BkIKy1eCE9pP1wdc8ROUtkHLF2PfAqYdyYBz6EA=
AllowedIPs = 10.10.10.230/32
```

客户端计算机可能具有以下更简单的配置：

```
[Interface]
PrivateKey = gI6EdUSYvn8ugXOt8QQD6Yc+JyiZxIhp3GInSWRfWGE=
ListenPort = 21841

[Peer]
PublicKey = HIgo9xNzJMWLKASShiTqIybxZ0U3wGLiUeJ1PKf8ykw=
Endpoint = 192.95.5.69:51820
AllowedIPs = 0.0.0.0/0
```

在服务器配置中，每个对等点(客户端)都能够将数据包发送到源IP与其相应的允许IP列表相匹配的网络接口。例如，当服务器从对端gN65BkIK...接收到数据包时，经过解密和身份验证后，如果其源IP为10.10.10.230，则允许进入该接口；否则它会被丢弃。

在服务器配置中，当网络接口想要将数据包发送到对等点（客户端）时，它会查看该数据包的目标IP并将其与每个对等点的允许IP列表进行比较，以确定将其发送到哪个对等点。例如，如果要求网络接口发送目标IP为10.10.10.230的数据包，它将使用对等方gN65BkIK...的公钥对其进行加密，然后将其发送到该对等方最近的互联网端点。

在客户端配置中，它的单个对等点（服务器）将能够将数据包发送到具有任何源IP的网络接口（因为0.0.0.0/0是通配符）。例如，当从对等HIgo9xNz...接收到数据包时，如果它使用任何源IP正确解密和验证，则允许它进入接口；否则它会被丢弃。

在客户端配置中，当网络接口想要将数据包发送到它的单个对等点（服务器）时，它将为具有任何目标IP地址的单个对等点加密数据包（因为0.0.0.0/0是通配符）。例如，如果要求网络接口发送一个具有任何目标IP的数据包，它将使用单个对等点HIgo9xNz...的公钥对其进行加密，然后将其发送到单个对等点最近的Internet端点。

换句话说，当发送数据包时，允许的IP列表充当一种路由表，而当接收数据包时，允许的IP列表充当一种访问控制列表。

这就是我们所说的加密密钥路由表：公钥和允许的IP的简单关联。

对于任何字段，可以使用IPv4和IPv6的任意组合。如有必要，WireGuard完全能够将一个封装在另一个内部。

因为在WireGuard接口上发送的所有数据包都经过加密和验证，并且因为对等点的身份和对等点允许的IP地址之间存在如此紧密的耦合，所以系统管理员不需要复杂的防火墙扩展，例如在这种情况下IPsec，而是他们可以简单地匹配“它来自这个IP吗？在这个接口上？”，并确保它是一个安全和真实的数据包。这极大地简化了网络管理和访问控制，并提供了更多保证，即您的iptables规则实际上正在执行您希望它们执行的操作。

### 内置漫游

客户端配置包含其单个对等方（服务器）的初始端点，因此它知道在接收到加密数据之前将加密数据发送到哪里。服务器配置没有其对等方（客户端）的任何初始端点。这是因为服务器通过检查经过正确身份验证的数据的来源来发现其对等方的端点。如果服务器本身更改了自己的端点，并将数据发送给客户端，客户端将发现新的服务器端点并更新配置。客户端和服务器都将加密数据发送到他们真正解密数据的最新IP端点。因此，两端都有完整的IP漫游。

## 安装和配置

### Ubuntu安装

```bash
sudo apt install wireguard
```

### 增加新接口

使用ip-link(8)添加一个新接口，它应该自动处理模块加载：

```bash
sudo ip link add dev wg0 type wireguard
```

使用ip-address(8)在wg0上配置IP地址

```bash
sudo ip address add dev wg0 10.88.16.3/24
```

使用wg对wg0进行配置

```bash
wg set wg0 listen-port 53 private-key /path/to/private-key peer ABCDEF... allowed-ips 10.88.16.0/24 endpoint 209.202.254.14:53
# or
wg setconf wg0 myconfig.conf
```

server端demo配置
```
[Interface]
Address = 10.66.66.1/24,fd42:42:42::1/64
PostUp = iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE; ip6tables -t nat -A POSTROUTING -o ens3 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -o ens3 -j MASQUERADE; ip6tables -t nat -D POSTROUTING -o ens3 -j MASQUERADE
ListenPort = 53
PrivateKey = <server private key>

[Peer]
PublicKey = <client 1 public key>
AllowedIPs = 10.66.66.2/32, fd42:42:42::2/128
```

peer1端demo配置
```
[Interface]
PrivateKey = <client 1 private key>
Address = 10.66.66.2/24,fd42:42:42::2/64
DNS = 176.103.130.130,176.103.130.131

[Peer]
PublicKey = <server public key>
Endpoint = <server public IP>:53
AllowedIPs = 0.0.0.0/0,::/0
```

最后使用ip-link(8)激活该接口

```bash
sudo ip link set up dev wg0
```

使用`wg show`查看当前配置

```bash
sudo wg
# or
sudo wg show
```

### 密钥生成

WireGuard需要base64编码的公钥和私钥。如下获取私钥：

```bash
umask 077
wg genkey > wireguard-privatekey
```

然后，可以从私钥中导出公钥：
```bash
wg pubkey < wireguard-privatekey > wireguard-publickey
```

或者通过一个命令得到两个key
```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

### NAT和防火墙穿越持久性

默认情况下，WireGuard在不使用时会尽量保持安静；它不是一个繁琐的协议。大多数情况下，它仅在对等方希望发送数据包时才传输数据。当它没有被要求发送数据包时，它会停止发送数据包，直到再次被要求。在大多数配置中，这很有效。但是，当对等点位于NAT或防火墙之后时，它可能希望能够接收传入的数据包，即使它没有发送任何数据包。因为NAT和状态防火墙跟踪“连接”，如果NAT或防火墙后面的对等方希望接收传入数据包，他必须通过定期发送保持活动数据包来保持NAT/防火墙映射有效。这称为持久保活。启用此选项后，将每隔interval秒向服务器端点发送一次保活数据包。适用于各种防火墙的合理间隔是25秒。将其设置为0将关闭该功能，这是默认设置，因为大多数用户不需要它，并且它会使WireGuard更健壮。可以通过在配置文件中向对等节点添加PersistentKeepalive=字段或在命令行设置persistent-keepalive来指定此功能。如果您不需要此功能，请不要启用它。但是，如果您位于NAT或防火墙后面，并且您希望在网络流量停止后很长时间内接收传入连接，则此选项将使“连接”在NAT眼中保持打开状态。

### 调试信息

如果使用的是Linux内核模块并且您的内核支持动态调试，则可以通过为模块启用动态调试来获得有用的运行时输出：

```bash
sudo modprobe wireguard && echo module wireguard +p > /sys/kernel/debug/dynamic_debug/control
```
如果您使用的是用户空间实现，请设置环境变量`export LOG_LEVEL=verbose`

## 通过服务器转发客户端的流量

### 在服务器上启用路由

首先我们需要在服务器上启用IPv4和IPv6路由，以便它可以转发数据包。

```
echo "net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1" > /etc/sysctl.d/wg.conf

sysctl --system
```

### 在服务器上启用NAT

我们想在服务器的公共接口（对我来说是ens3）和wg0接口之间启用NAT。为此，我们需要两个iptables命令：

```
iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE
ip6tables -t nat -A POSTROUTING -o ens3 -j MASQUERADE
```

WireGuard可以在启动时为我们执行这些操作。为了保持干净，我们想在界面关闭时删除它们，所以这里是您需要添加到服务器上的[Interface]块的内容：
```
PostUp = iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE; ip6tables -t nat -A POSTROUTING -o ens3 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -o ens3 -j MASQUERADE; ip6tables -t nat -D POSTROUTING -o ens3 -j MASQUERADE
```

### 使服务器成为客户端的网关

我们可以利用AllowedIPs选项来覆盖客户端上的默认路由。只需将行更改为：

```
AllowedIPs = 0.0.0.0/0,::/0
```

重启界面。完成，所有客户端的数据包都通过服务器！

## 已知限制

WireGuard是一种协议，与所有协议一样，它会进行必要的权衡。下面总结了由于这些权衡而导致的已知限制。

### 深度包检测

WireGuard不专注于混淆。相反，混淆应该发生在WireGuard之上的一层，WireGuard专注于通过简单的实现提供可靠的加密。但是，很可能会插入各种形式的混淆。

### TCP模式

WireGuard明确不支持基于TCP的隧道，因为隧道TCP-over-TCP的经典网络性能非常糟糕。相反，将WireGuard的UDP数据包转换为TCP是上层混淆的工作（见上一点），并且可以通过udptunnel和udp2raw等项目完成。

### 硬件加密

WireGuard使用ChaCha20Poly1305，它在几乎所有通用CPU上的软件速度都非常快。在撰写本文时，并没有大量的专用硬件支持它，尽管这种情况正在发生变化。实际上，这不是问题，因为CPU上的矢量指令最终与AES-NI指令处于同一范围内（有时甚至更快）。

### 漫游恶作剧

WireGuard的漫游无需额外的往返或其他身份验证，这意味着中间的活跃人员可以替换源IP地址。由于处于活动状态，中间人已经可以重定向数据包，但是端点地址可能会更新，并且中间人在失去中间人后可能会中继数据包。然而，由于WireGuard通常的身份验证加密，这些数据包仍然无法被攻击者破译。但是，如果这是一个问题，普通的防火墙可以将WireGuard套接字锁定到特定的IP地址，并且WireGuard的未来修订版可能会天生允许这样做。相关地，可以玩TCP序列号猜测游戏，以便让WireGuard服务器将数据包定向到不受控制的IP地址。

### 身份隐藏前向保密

由于握手，WireGuard具有数据包的前向保密性，但握手本身使用响应者的静态公钥加密发送者的公钥，这意味着响应者的私钥和先前握手的流量日志的妥协将启用攻击者可以找出谁发送了握手，但不知道其中包含什么数据。类似地，mac1是通过响应者的公钥生成的，这意味着可以通过尝试哈希来猜测数据包是否针对特定响应者，尽管mac1可能是伪造的。缓解措施包括根据不可链接性的预期轮换或重新生成密钥。

### 后量子保密

默认情况下，WireGuard不是后量子安全的。但是，预共享密钥参数可用于添加后量子保密层。如果公钥被散列而不是直接发送，它可能是后量子安全的，但这不是WireGuard握手所基于的噪声协议框架的一部分，并且这种散列技术不会启用前向安全的后量子保密任何一个。后量子安全的最佳选择是在WireGuard之上运行真正的后量子握手，然后将该密钥插入WireGuard的预共享密钥槽。

### 拒绝服务

由于使用mac1和mac2，WireGuard应该是抗滥用的，尽管在mac2启动之前，ECDH计算可能会使用大量CPU。但实际上，mac2通常就足够了。

### 不可靠的单调计数器

WireGuard使用系统时间作为可靠的单调计数器。如果向前跳转，用户可能会DoS他们自己的密钥，使以后不可能有更大的值，或者控制系统时间的对手可以存储握手启动以供以后使用。如果它向后跳，握手同样是不可能的。因此，系统时间不应处于敌对对手的控制之下。

### 路由环路

目前在本地和网络上检测路由环路存在一些问题，并且有各种技巧，例如将外部src更改为内部src。


### 有用的命令行

```bash
nano wg0.conf
sudo wg-quick down wg0
sudo wg-quick up wg0
sudo systemctl start wg-quick@wg0
sudo systemctl enable wg-quick@wg0
sudo systemctl restart wg-quick@wg0
```

## Reference
- [wireguard](https://www.wireguard.com/)
- [How to setup a VPN server using WireGuard (with NAT and IPv6)](https://stanislas.blog/2019/01/how-to-setup-vpn-server-wireguard-nat-ipv6/)
