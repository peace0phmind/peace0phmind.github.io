---
title: "常用命令与工具"
date: 2020-10-30T17:23:54+08:00
draft: false
---

## 类似mac airdrop的工具

这里强烈推荐一个类似mac下airdrop的网站,[https://snapdrop.net](https://snapdrop.net)

![snapdrop](/images/202010/usage-commands/snapdrop.png)

这个网站可以让使用同一局域网的所有设备（jetson agx/nano, raspberry pi, windows, linux_x86, phone etc.）相互快速共享文件或发送消息。(使用时请关闭代理，否则无法正确找到对方)

用浏览器打开即可看到自己的名字，每次刷新名字随机产生。点击对方头像可以选择文件，拖动文件到头像也可以进行文件分享。在头像上点击右键，弹出框中输入需要发送的消息。


还有个[https://www.sharedrop.io](https://www.sharedrop.io)，不过这个网站用的缓存服务器需要代理才可以访问，不是很方便。

## 清除DNS缓存

ubuntu操作系统使用如下命令：
```
sudo systemd-resolve --flush-caches
```

### 22.04
```bash
resolvectl flush-caches
```

参考：[How to clear DNS cache](https://www.ispsystem.com/news/clear-dns-cache)

## 获取不同网络环境下的ping值，DNS解析结果等

[https://www.boce.com](https://www.boce.com)

