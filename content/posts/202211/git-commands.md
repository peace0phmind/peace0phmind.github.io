---
title: "Git Commands"
description: "git-commands"
keywords: "git"

date: 2022-11-18T17:46:10+08:00
lastmod: 2022-11-18T17:46:10+08:00

author: peace0phmind
url: "posts/202211/git-commands"

draft: true

categories:
  -
tags:
  - git

---

获取已删除文件的列表
```bash
git log --diff-filter=D --summary | grep delete
```

获取一个指定文件或带通配符文件名的文件所在的hash
```bash
git log --all -- "**/*.tar"
git log --all -- "**/*.zip"
git log --all -- path/file
```

找到10个最大的文件
```bash
git verify-pack .git/objects/pack/pack-* -v | sort -n -k 3 | uniq | tail -10
```

查找hash-code对应的文件名
```bash
git rev-list --objects --all | grep <HASH_CODE>
```

永久删除目录或文件
```bash
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch filename" --prune-empty --tag-name-filter cat -- --all
```

删除快取，回收空间
```bash
rm -rf .git/refs/original
git reflog expire --expire=now --all
git gc --prune=now
```

获取修改的文件列表
```bash
git diff --name-only > ../xxx.log
```

删除文件中的\r字符
```bash
sed -i 's/\r//g' path/file
```

获取已经删除的文件
```bash
git checkout <SHA> -- /path/to/file
```
