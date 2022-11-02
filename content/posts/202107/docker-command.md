---
title: "Docker Command"
date: 2021-07-06T16:34:11+08:00
draft: false
---

## run v2ray under docker

docker run --restart=always --network host -d --name v2ray -v ~/etc/v2ray:/etc/v2ray v2fly/v2fly-core v2ray --config=/etc/v2ray/config.json
