---
title: "Docker Command"
date: 2021-07-06T16:34:11+08:00
draft: false
---

## Docker Removing

### Removing Images by ID or Name

```bash
docker rmi <id>
```

### Docker Image Prune
Removes All Dangling Images

```bash
docker image prune -a
```

### Docker System Prune
查找和删除所有未使用的对象

```bash
docker system prune -a
```