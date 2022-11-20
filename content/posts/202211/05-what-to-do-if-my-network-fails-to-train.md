---
title: "What to Do if My Network Fails to Train"
description: "05-what-to-do-if-my-network-fails-to-train"
keywords: "fails,train"

date: 2022-11-20T11:22:00+08:00
lastmod: 2022-11-20T11:22:00+08:00

author: peace0phmind
url: "posts/202211/05-what-to-do-if-my-network-fails-to-train"

draft: true

categories:
  -
tags:
  - fails
  - train

---

## 机器学习的一般步骤

```markmap {height="200px"}
---
markmap:
  maxWidth: 300
  colorFreezeLevel: 6
  initialExpandLevel: 10
---

# loss on training data

## large
- [model bias](#model-bias)
  - make your model complex
- [optimization](#optimization-issue)

## small
- loss on testing data
  - large
    - [overfitting](#overfitting)
      - more training data
      - data augmentation
      - make your model simpler
    - [mismatch](#mismatch)
  - small :blush:
  
## [model complex trade-off(权衡)](#bias-complexity-trade-off)
- Split your training data into training set and validation set for model selection

```

### Model Bias
- The model is too simple.
  - find a needle in a haystack (大海捞针)
  - but there is no needle
- Solution: redesign your model to make it more flexible
  - more features
  - more neurons, layers

### Optimization Issue
- Large loss not always imply model bias. There is another possibility ...
  - A needle is in a haystack..., Just cannot find it.

### Model Bias v.s. Optimization Issue
- Gaining the insights from comparison
- 当在测试数据上和训练数据上有着类似的loss曲线时，这说明是`Optimization Issue`的问题

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02.009.jpg)

#### Optimization Issue
- Start from shallower networks(or other models), which are easier to optimize.
- 从更容易优化的较浅的网络（或其他模型）开始。
- If deeper networks do not obtain smaller loss on `training data`, then there is optimization issue.
- 如果更深的网络在“训练数据”上没有获得更小的损失，那么就存在优化问题。

### Overfitting
- Small loss on training data, large loss on testing data. Why?
- 数据分布的这条虚线通常是无法明确的获知的，我们通常只能拿到在这条曲线上的多个`Training Data`
- 由于model的Flexible, 训练出来的这个模型，在没有训练数据的地方会有“freestyle”, 从而导致测试数据的overfitting
  - 增加训练数据
  - Data augmentation(用一些对这个问题的理解，自己创造出新的训练数据。例如：对图片左右反转，或者是截取其中一块等)
  - 通过限制model来解决overfitting，给model制造限制的方法：
    - make your model simpler
    - Less parameters, sharing parameters
      - Fully-connected的架构是一个比较有弹性的架构；而CNN是一个比较有限制的架构（根据影像的特性来限制模型的弹性）
    - Less features
    - Early stopping
    - Regularization
    - Dropout
  - 这里需要注意，太多的限制和太简单的模型会导致`model bias`

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02.014.jpg)

### Bias-Complexity Trade-off
- 通过观察`Training loss`和`Testing loss`的loss曲线来选择model和对应的模型限制

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02.020.jpg)

### N-fold Cross Validation
- Cross Validation就是N-flod Cross Validation的一个特例
- 如果使用`Cross Validation`, 则使用`Validation Set`的loss最小进行模型的选择
- 当使用`N-fold Cross Validation`时，则使用mse的avg最小来挑选模型

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02.024.jpg)

### Mismatch
- Your training and testing data have different distributions.
- 需要对训练资料和测试资料有一定的了解才能分清到底是不是mismatch
- mismatch和overfitting不是一个东西，overfitting可以通过增加训练资料来解决，而mismatch无法通过增加训练资料来解决

## Optimization

### Optimization Fails because
- loss is `Not small enough`, because the gradient is close to zero.
- Gradient为零的情况有：`local minima`, `local maxima`, `saddle point`等
- `saddle point`: Gradient为零, 同时既不是`local minima`也不是`local maxima`的地方
- Gradient为零的点统称为`critical point`

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02-1.002.jpg)

### Tayler Series Approximation(泰勒级数逼近)
- 如何知道一个`critical point`是`local minima`还是`saddle point`
- 其中包括 Gradient $\color{green}g$ is a <u>vector</u>, Hessian $\color{red}H$ is a <u>matrix</u>.

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02-1.004.jpg)

#### Hessian
- Gradient $\color{green}g$ 为0时，则可知目前所在位置为临界点`Critical Point`
- Hessian $\color{red}H$ can telling the properties of critical points.

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02-1.005.jpg)

- 当$\color{red}H$这个矩阵中的值全部为正值，则当前所在为`Local Minima`
- 当$\color{red}H$这个矩阵中的值全部为负值，则当前所在为`Local Maxima`
- 当$\color{red}H$这个矩阵中的值有正有负，则当前所在为`Saddle Point`

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02-1.006.jpg)

### Saddle Point v.s. Local Minima
- 在一维的空间中看到的local minima，在二维的空间中看到的可能就只是saddle point.
- 当我们有更多的参数，也许local minima是很少见的

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02-1.014.jpg)

#### Minimum Ratio
- 是所有`Local Minima`的数量与所有`Critical Point`的比值
- 从图上可知，最大的ratio也只是0.6
- 图上Eigen Values就是前文所说的Hessian Matrix.

![](/images/202211/05-what-to-do-if-my-network-fails-to-train/02-1.015.jpg)


## Reference Video


{{< youtube WeHM2xpYQpw >}}
{{< youtube QW6uINn7uGk >}}
{{< youtube zzbr1h9sF54 >}}
{{< youtube HYUXEeh3kwY >}}
{{< youtube O2VkP8dJ5FE >}}

{{< youtube _j9MVVcvyZI >}}

{{< youtube 1_HBTJyWgNA >}}
{{< youtube 4pUmZ8hXlHM >}}
{{< youtube e03YKGHXnL8 >}}