---
title: "Docker Swarm"
description: "docker-swarm"
keywords: "docker,swarm"

date: 2022-11-29T14:36:41+08:00
lastmod: 2022-11-29T14:36:41+08:00

author: peace0phmind
url: "posts/202211/docker-swarm"

draft: false

categories:
  - blog
tags:
  - docker
  - swarm

---



## Swarm
- 与Docker Engine集成的集群管理: 创建一组Docker引擎，可以在其中部署应用程序服务。不需要额外的编排软件来创建或管理swarm。
- 分散式设计: Docker引擎不是在部署时处理节点角色之间的差异，而是在运行时处理特殊化。Docker引擎支持两种类型的节点：managers和workers。这意味着您可以从单个磁盘映像构建整个群。
- 声明式服务模型： Docker引擎使用声明式方法让您定义应用程序堆栈中各种服务的所需状态。例如：描述一个应用程序，该应用程序由具有消息队列服务的Web前端服务和数据库后端组成。
- 缩放：对于每个服务，可以声明要运行的任务数。当放大或缩小服务时，群管理器会通过添加或删除任务来自动适应以维持所需的状态。
- 期望的状态和重新调整：swarm管理器节点持续监控集群状态并协调实际状态与您表达的期望状态之间的任何差异。例如，如果设置一个服务运行10个容器副本，而其中两个副本的工作机器崩溃，则管理器创建两个新副本来替换崩溃的副本。集群管理器将新副本分配给正在运行且可用的workers上。
- 多主机网络：可以为您的服务指定覆盖网络(overlay network)。集群管理器在初始化或更新应用程序时自动为覆盖网络上的容器分配地址。
- 服务发现: Swarm管理器节点为swarm中的每个服务分配一个唯一的DNS名称并负载平衡运行的容器。您可以通过嵌入在swarm中的DNS服务器查询在swarm中运行的每个容器。
- 负载均衡: 您可以将服务端口公开给外部负载均衡器。在内部，swarm允许您指定如何在节点之间分发服务容器。
- 默认安全: 集群中的每个节点都强制执行TLS相互身份验证和加密，以确保自身与所有其他节点之间的通信安全。您可以选择使用自签名根证书或来自自定义根CA的证书。
- 滚动更新: 在滚动更新时，您可以逐步将服务更新应用于节点。集群管理器允许您控制服务部署到不同节点集之间的延迟。如果出现任何问题，您可以回滚到以前版本的服务。

### Init
初始化一个群。此命令的目标 docker 引擎成为新创建的单节点群中的管理器。

```bash
docker swarm init --advertise-addr 192.168.1.123
```

### Join
将节点加入群。该节点根据您使用--token标志传递的令牌作为管理节点或工作节点加入。如果您传递一个manager令牌，该节点将作为manager加入。如果您传递worker令牌，则该节点将作为worker加入。

```bash
docker swarm join --token xxx 192.168.1.123:2377
```

下面命令需在manager节点执行获取对应的token
```bash
# 获取加入workers的token
docker swarm join-token worker

# 获取加入managers的token
docker swarm join-token manager
```

## 节点管理

### ls
在manager节点执行下面命令，查看所有节点列表

```bash
docker node ls
```

### Promote
将一个或多个节点提升为集群中的管理器

```bash
docker node promote <node-id>
```

### Demote
从群中的管理器中降级一个或多个节点

```bash
docker node demote <node-id>
```

### Get All Labels as map
```bash
# run command under swarm manager
docker node ls -q | xargs docker node inspect -f '{{ .ID }} [{{ .Description.Hostname }}]: {{ .Spec.Labels }}'
```

### Get All Labels
```bash
# run command under swarm manager
docker node ls -q | xargs docker node inspect \
  -f '{{ .ID }} [{{ .Description.Hostname }}]: {{ range $k, $v := .Spec.Labels }}{{ $k }}={{ $v }} {{end}}'
```

### Add Labels
Run docker node update --label-add on a manager node to add label metadata to a node. The --label-add flag supports either a <key> or a <key>=<value> pair.
- 当只输入<key>时，得到的是一个空值标签
- 再次使用update可以更新该<key>值标签

```bash
docker node update --label-add <key> --label-add <key>=<value> <node_hostname>
```

### Remove Labels
```bash
docker node update --label-rm <key> <node_hostname>
```