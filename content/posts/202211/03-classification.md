---
title: "Classification"
description: "classification"
keywords: "classification"

date: 2022-11-08T14:59:57+08:00
lastmod: 2022-11-08T14:59:57+08:00

author: peace0phmind
url: "posts/202211/03-classification"

draft: false

categories:
  - machine-learning
tags:
  - classification

---

`Classification`: Given options(classes), the function outputs the correct one.

## Classification
- Function (Model):
  $$ \delta(x) \begin{cases}  g(x) > 0 & \text{Output = class 1} \cr else & \text{Output = class 2} \end{cases} $$
- Loss Function
  - The number of times f get incorrect results on training data.
    $$ L(f) = \sum_n\delta(f(x^n) \ne \hat{y}^n ) $$
- Find the best function:
  - Example: Perceptron, SVM

从训练数据中找出二分类问题的概率的模型叫做:{{<clr>}}`Generative Model`{{</clr>}} $ P(x) = P(x|C1)P(C1) + P(x|C2)P(C2) $
![Generative Model](/images/202211/03-classification/4.0002.jpg "Generative Model")

### Gaussian Distribution
$ f_{\mu,\sum}(x) = \frac{1}{(2\pi)^{D/2}}\frac{1}{|\sum|^{1/2}} exp \\{  -\frac{1}{2}(x-\mu)^T\sum^{-1}(x-\mu)  \\} $
- input: vector x, output: probability of sampling x
- The shape of the function determines by {{<clr>}}mean $\mu${{</clr>}} and {{<clr>}}covariance matrix $\sum${{</clr>}}

![Gaussian Distribution](/images/202211/03-classification/4.0004.jpg "Gaussian Distribution")

### Maximum Likelihood
![Maximum Likelihood](/images/202211/03-classification/4.0006.jpg "Maximum Likelihood")


## reference video

{{< youtube fZAZUYEeIMg >}}
{{< youtube hSXFuypLukA >}}
