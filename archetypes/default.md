---
title: "{{ replace .Name "-" " " | title }}"
description: "{{ .Name }}"
keywords: "{{replace .Name "-" ","}}"

date: {{ .Date }}
lastmod: {{ .Date }}

author: peace0phmind
url: "{{ lower .Dir }}{{ lower .Name }}"

draft: true

categories:
  -
tags:
  - {{replace .Name "-" "\n  - "}}

# 原文链接
#link:
# 图片链接，用在open graph和twitter卡片上
#images:
# 在首页展开内容
#expand: true
# 外部链接地址，访问时直接跳转
#extlink:
# 在当前页面关闭评论功能
#comment:
#  enable: false
# 关闭文章目录功能
#toc: false
# 开启文章置顶，数字越小越靠前
#weight: 1

---
