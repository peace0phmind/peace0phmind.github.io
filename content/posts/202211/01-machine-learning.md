---
title: "Machine Learning"
description: "machine-learning"
keywords: "machine-learning"

date: 2022-11-04T08:50:08+08:00
lastmod: 2022-11-04T08:50:08+08:00

author: peace0phmind
url: "posts/202211/01-machine-learning"

draft: false

categories:
  - machine-learning
tags:
  - 

#expand: true
weight: 1

---

```markmap
# ML

## Suppervised Learning
- [Regression](/posts/202211/02-regression)
  - [Backpropagation](/posts/202211/02-regression#backpropagation)
  - [Regularization](/posts/202211/02-regression#regularization)
- [Classification](/posts/202211/03-classification)
- Structured Learning
  - Create something with structure (image, document)

## Self-Supervised Learning
- Pre-Trained Model(Foundation Model)
- unlabeled Data
- Downstream Tasks
- Models
  - BERT
  - ELMo
  - GPT-2
  - GPT-3
  - T5

## Generative Adversarial Network
- 收集大量x和y
- x和y是unpaired
- 研究成果
  - [Unsupervised Abstractive Summarization](https://arxiv.org/abs/1810.02851)
  - [Unsupervised Translation](https://arxiv.org/abs/1710.11041)
    - [04087](https://arxiv.org/abs/1710.04087)
  - [Unsupervised ASR](https://arxiv.org/abs/2105.11084)
    - [1804.00316](https://arxiv.org/abs/1804.00316)
    - [1812.09323](https://arxiv.org/abs/1812.09323)
    - [1904.04100](https://arxiv.org/abs/1904.04100)

## Reinforcement Learning (RL)

## Anomaly Detaction(异常检测, 让机器知道它不知道)

## Explainable AI

## Model Attack (模型攻击)

## Domain Adaptation

## Network Compression

## Life-Long Learning

## Meta Learning = Learn to Learn
- Few-shot Learning

```

## Machine Learning是什么

简单的理解就是在输入和输出中找一个函数

![Different types of Functions](/images/202211/01-machine-learning/01.0001.jpg "Different types of Functions")

## Deep Learning Introduce

### history (Ups and downs of Deep Learning)
- 1958: Perceptron (linear model)
- {{<color>}}1969: Perceptron has limitation{{</color>}}
- 1980: Multi-layer perceptron
  - Do not have significant difference from DNN today
- 1986: Backpropagation
  - Usually more than 3 hidden layers is not helpful
- {{<color>}}1989: 1 hidden layer is "good enough", why deep?{{</color>}}
- 2006: RBM initialization (breakthrough)
- 2009: GPU
- 2011: Start to be popular in speech recognition
- 2012: win ILSVRC image competition

### Fully Connect Feedforward Network
- 输入叫`Input Layer`
- 输出叫`Output Layer`
- 中间层叫`hidden Layers`
![Fully Connect Feedforward Network](/images/202211/01-machine-learning/6.0002.jpg "Fully Connect Feedforward Network")

### Deep = Many hidden layers
- AlexNet(2012), 8 layers, error rate: 16.4%
- VGG(2014), 19 layers, error rate: 7.3%
- GoogleNet(2014), 22 layers, error rate: 6.7%
- Residual Net(2015), 152 layers, error rate: 3.57%

### FAQ
- Q: How many layers? How many neurons for each layer?
  - `Trial and Error` + `Intuition`
- Q: Can the structure be automatically determined?
  - Evolutionary Artificial Neural Networks
- Q: Can we design the network structure?
  - Convolutional Neural Network (CNN)
- Q: Deeper is Better?
  - Universality Theorem
    - Any continuous function f
    - $ f : R^N \rightarrow R^M $
    - Can be realized by a network with one hidden layer (given `enough` hidden neurons)
    - {{<color>}}Why `Deep` neural network not `Fat` neural network?{{</color>}}


## Reference
系列文档是国立台湾大学[李宏毅](https://speech.ee.ntu.edu.tw/~hylee/index.php)老师Machine Learning系列教材的学习整理。

- [Machine Learning 2022](https://speech.ee.ntu.edu.tw/~hylee/ml/2022-spring.php)
- [Machine Learning 2021](https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.php)
- [Machine Learning 2020](https://speech.ee.ntu.edu.tw/~hylee/ml/2020-spring.php)
- [Machine Learning 2019](https://speech.ee.ntu.edu.tw/~hylee/ml/2019-spring.php)
- [Machine Learning 2016 FALL](https://speech.ee.ntu.edu.tw/~hylee/ml/2016-fall.php)
- [MLDS 2015 FALL](https://speech.ee.ntu.edu.tw/~hylee/mlds/2015-fall.php)

### Nvidia Resources
- [nvidia training resource](https://www.nvidia.com/en-us/training/resources/)


### Reference Book
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
  - written by Michael Nielsen
- [Deep Learning](https://www.deeplearningbook.org/)
  - written by Yoshua Bengio, Ian J. Goodfellow and Aaron Courville
