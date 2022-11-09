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

## Probabilistic Generative Model

### features and predict target
- 一共有7个features，其中
- `Total` = `HP` + `Attack` + `Deffense` + `SP Atk` + `Sp Def` + `Speed`
- predict target: type of pokemon

![features and predict target](/images/202211/03-classification/4.004.jpg "features and predict target")

### How to do Classification
- 收集Training data for Classification
- 考虑如果做分类？

### Classification as Regression?（分类问题是否可以用回归算法处理？）
以二分类举个例子
- Training: Class 1 means the target is 1; Class 2 means the target is -1
- Testing: $ \text{closer to 1} \rightarrow \text{class 1}; \text{closer to -1} \rightarrow \text{class 2} $

这样直接用Regression来解决Classification的问题，会发生如下图的情况：
- 当样本feature如左图所示，则$y=b+w_1x_1+w_2x_2$的函数可以很好的工作。
- 当样本feature如右图所示，由于右下角的数据，导致Regression的Loss函数在求最小值时，会倾向于给出紫色的线段的方程。即Loss函数会由于“太正确”而导致最终预测结果出错。
- Penalize to the examples that are "too correct" ... (Bishop, P186)
![Classification as Regression](/images/202211/03-classification/4.007.jpg "Classification as Regression")


### Ideal Alternatives(理想的做法)
- Function (Model):
  $$ \delta(x) \Rightarrow \begin{cases}  g(x) > 0 & \text{Output = class 1} \cr else & \text{Output = class 2} \end{cases} $$
- Loss Function
  - The number of times f get incorrect results on training data.
    $$ L(f) = \sum_n\delta(f(x^n) \ne \hat{y}^n ) $$
- Find the best function:
  - Example: Perceptron, SVM


### Generative Model
- $P(C_1)$是从两个分类中，随机选中Class1的几率，$P(C_2)$是从两个分类中，随机选中Class2的几率。
- 假设x为其中一种颜色的圆圈，则：$P(x|C_1)$表示从Class1中选中x的几率，$P(x|C_2)$表示从Class2中选中x的几率，
- 选中x属于class1的几率就是：$ P(C_1|x) = \frac{P(C_1)P(x|C_1)}{P(C_1)P(x|C_1)+P(C_2)P(x|C_2)} $
- 选中x的总几率就是： $ P(x) = P(x|C_1)P(C_1) + P(x|C_2)P(C_2) $
- Estimating the Probabilities From training data, 这整个想法就叫做{{<clr>}}Generative Model{{</clr>}}
![Generative Model](/images/202211/03-classification/4.010.jpg "Generative Model")

### Gaussian Distribution
- $ f_{\mu,\sum}(x) = \frac{1}{(2\pi)^{D/2}}\frac{1}{|\sum|^{1/2}} exp \\{  -\frac{1}{2}(x-\mu)^T\sum^{-1}(x-\mu)  \\} $
- input: vector x, output: probability of sampling x(实际是probability density，概率密度与概率成正比,此处简略为概率)
- The shape of the function determines by {{<clr>}}mean $\mu${{</clr>}} and {{<clr>}}covariance matrix $\sum${{</clr>}}(协方差矩阵)

![Gaussian Distribution](/images/202211/03-classification/4.014.jpg "Gaussian Distribution")

### Maximum Likelihood（找mean$\mu$和covariance matrix $\Sigma$的方法）
- mean $\mu$控制原点在图中的位置。
- covariance matrix $\Sigma$决定图形的形状。
- 虽然图中左下角的点都可以求出相对于两个圈的概率，但是这两个概率的大小是不一样的。
- 给定一个Gaussian的$\mu$和$\Sigma$,就可以求出对应的likelihood
- $ L(\mu, \Sigma) = f_{\mu, \Sigma}(x^1)f_{\mu, \Sigma}(x^2)f_{\mu, \Sigma}(x^3)\dots\dots f_{\mu, \Sigma}(x^n) $
- 这里的没一个$f_{\mu, \Sigma}(x^1)$展开，都是$ f_{\mu,\sum}(x) = \frac{1}{(2\pi)^{D/2}}\frac{1}{|\sum|^{1/2}} exp \\{  -\frac{1}{2}(x-\mu)^T\sum^{-1}(x-\mu)  \\} $
- 得到Maximum Likelihood: $ \mu^\*, \Sigma^\* = arg \max\limits_{\mu, \Sigma} L(\mu, \Sigma) $
- $\mu^\*$为取x的平均值: $ \mu^\* = \frac{1}{n}\sum\limits_{i=1}^n x^i $
- $ \Sigma^\* = \frac{1}{n} \sum\limits_{i=1}^n(x^i-\mu^\*)(x^i-\mu^\*)^T $
![Maximum Likelihood](/images/202211/03-classification/4.017.jpg "Maximum Likelihood")

### 采用上诉方法得到的测试结果

| features | $\theta$ | test accuracy |
|--|--|--|
| `Defense`,`SP Defense` | $ \mu^1, \mu^2 $ : 2-dim vector <br/> $\Sigma^1, \Sigma^2$: 2*2 matrices | 47% |
| All the 7 features     | $ \mu^1\dots\mu^7 $ : 7-dim vector <br/> $\Sigma^1\dots\Sigma^7$: 7*7 matrices | 54% |


## reference video

{{< youtube fZAZUYEeIMg >}}
{{< youtube hSXFuypLukA >}}
