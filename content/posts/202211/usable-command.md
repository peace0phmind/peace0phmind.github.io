---
title: "Usable Command"
description: "usable-command"
keywords: "usable,command"

date: 2022-11-22T14:12:32+08:00
lastmod: 2022-11-22T14:12:32+08:00

author: peace0phmind
url: "posts/202211/usable-command"

draft: true

categories:
  -
tags:
  - usable
  - command

---

导出markdown到docx
```bash
cat xxx.md | sed 's/(\/images\//(/g' | pandoc -f markdown -t docx --resource-path=../../../static/images --reference-doc=../../../static/templates/numbered-sections.docx -o xxx.docx
```

cat face-inspection-program.md | sed 's/(\/images\//(/g' | pandoc -f markdown -t docx --resource-path=../../../static/images --reference-doc=../../../static/templates/numbered-sections.docx -o xxx.docx
