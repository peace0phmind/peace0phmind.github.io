---
title: "07 Convolutional Neural Network"
description: "07-Convolutional-Neural-Network"
keywords: "Convolutional,Neural,Network"

date: 2023-03-20T15:19:57+08:00
lastmod: 2023-03-20T15:19:57+08:00

author: peace0phmind
url: "posts/202303/06-convolutional-neural-network"

draft: true

categories:
  - ml
tags:
  - Convolutional
  - Neural
  - Network

---

## Image Classification
- `Image Classification`: 给机器一张图片，机器判断你面有什么样的东西
- 输入是每个模型固定的。如果遇到不同规格的输入，则需要通过scale的方式缩放到对应的尺寸
- 输出是分类：`one hot vector`
- 使用`Cross entropy`做梯度下降，得到`one hot vector`的分类结果

假设使用RGB三通道，分辨率在100*100的图像作为模型大小对图像进行分类：

### Fully Connected Network
- 入参为100*100*3，即$3*10^4$
- 假设第一层neuron的数目有1000个，那么第一层全连接层的weight就有$3*10^7$个
- 虽然随着模型参数的增加，我们可以增加模型的弹性，但是我们也增加了Overfitting的风险。
- 我们真的需要在图像处理上使用全连接机制么？

### 观察下鸟的分类任务
- 人来识别鸟的话，会考虑鸟嘴，研究，爪子等等这些鸟的关键特征
- 人们期望机器在cnn模型下做的是类似的事情
- neuron并不需要观察整个图片，一些重要特征相对于整张图片来说要小的多。

## Reference video

{{< youtube OP5HcXJg2Aw >}}

{{< youtube SoCywZ1hZak >}}
