---
title: "Iperf3"
description: "iperf3"
keywords: "iperf3,network,speed"

date: 2022-12-16T08:48:31+08:00
lastmod: 2022-12-16T08:48:31+08:00

author: peace0phmind
url: "posts/202212/iperf3"

draft: false

categories:
  -
tags:
  - iperf3
  - performance

---

## installation
```bash
sudo apt install iperf3 -y
```

## test tcp speed/throughput

### start server on serverA(server mode)
```bash
iperf3 -s -p [default port 5201]
```

### start server on serverB(client mode)
```bash
iperf3 -c <ip of serverA> -p [serverA port]
```

## test udp speed/throughput

### start server on serverA(server mode)
same with tcp
```bash
iperf3 -s -p [default port 5201]
```

use `-u` option on client side
### start server on serverB(client mode)
```bash
iperf3 -c <ip of serverA> -u -p [serverA port]
```

## more client options

### number of parallel client threads
Pass the `-P` option

### set time in seconds to transmit for (default 10 secs)
Pass the `-t` option

## examples

run on serverA
```base
iperf3 -s
```

run on serverB
```bash
iperf3 -c x -P 3 -t 30
```