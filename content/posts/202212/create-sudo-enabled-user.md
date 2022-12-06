---
title: "Create Sudo Enabled User"
description: "create-sudo-enabled-user"
keywords: "create,sudo,enabled,user"

date: 2022-12-06T16:22:41+08:00
lastmod: 2022-12-06T16:22:41+08:00

author: peace0phmind
url: "posts/202212/create-sudo-enabled-user"

draft: true

categories:
  -
tags:
  - sudo
  - user

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