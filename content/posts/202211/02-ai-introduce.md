---
title: "Ai介绍"
description: "ai introduce"
keywords: "ai"

date: 2022-11-04T22:20:52+08:00
lastmod: 2022-11-04T22:20:52+08:00

author: peace0phmind
url: "posts/202211/02-ai-introduce"

draft: true

categories:
  - machine-learning
tags:
  -

---

## 介绍
- `Regression`: Input a vector, the function outputs a scalar.
- `Classification`: Given options(classes), the function outputs the correct one.
- `Structured Learning`: Create something with structure (image, document).

## 回归
预测问题：根据前面的浏览数据，预测后面的浏览量

### Function with Unknown Parameters
`Model`: $y = b + wx_1$ <br/>
$y$(`Label`): no. of views on 2/26， $x_1$(`feature`): no. of views on 2/25  <br/>
$w$(`weight`) and $b$(`bias`) are unknown parameters (learned from data)  <br/>

### Define Loss from Training Data
Loss is a function of parameters: $L(b, w)$ <br/>
Loss: how good a set of values is.          <br/>
Loss: $ L = \frac{1}{N}\sum\limits_{n}e_n$  <br/>
$e = |y - \hat{y}|$ $L$ is mean absolute error (MAE) <br/>
$e = (y-\hat{y})^2$ $L$ is mean square error (MSE) <br/>
if $y$ and $\hat{y}$ are both probability distributions, then use `Cross-entropy`


## 参考
{{< youtube Ye018rCVvOo >}}
{{< youtube bHcJCp2Fyxs >}}

{{< youtube Dr-WRlEFefw >}}
{{< youtube ibJpTrp5mcE >}}
{{< youtube fegAeph9UaA >}}
{{< youtube fZAZUYEeIMg >}}
{{< youtube hSXFuypLukA >}}
