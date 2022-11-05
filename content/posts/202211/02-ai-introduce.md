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

使用不同的参数，计算出来的Loss画出来的等高线图叫做：`Error Surface`
![等高线图](/images/202211/02-ai-introduce/01.0001.jpg)

### Optimization
找一个$w$和$b$，使$L$最小： $ w^\*, b^\* = arg \min\limits_{w, b} L$
这种找到最小$w$和$b$的方法叫做：`Gradient Descent`

以一个参数$w$为例描述`Gradient Descent`的过程: 
- 随机初始化点$w^0$
- 计算$w=w^0$时，对$L$的微分是多少：$\frac{{\delta}L}{{\delta}W}|_{w=w^0}$
  - 如果计算出来的结果为负数，则增加$w$
  - 如果计算出来的结果为正数，则减少$w$
  - 增加或减少的数值为：${\color{red}\eta}\frac{{\delta}L}{{\delta}W}|_{w=w^0}$, $\color{red}\eta$:叫learning rate,是一个hyperparameter
  - 这个过程用数学是表达就是：$ w^1 \get  $

`hyperparameter`: 需要人来设置的参数

## 参考
{{< youtube Ye018rCVvOo >}}
{{< youtube bHcJCp2Fyxs >}}

{{< youtube Dr-WRlEFefw >}}
{{< youtube ibJpTrp5mcE >}}
{{< youtube fegAeph9UaA >}}
{{< youtube fZAZUYEeIMg >}}
{{< youtube hSXFuypLukA >}}
