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
  - ml
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
- Estimating the Probabilities From training data, 这整个想法就叫做{{<color>}}Generative Model{{</color>}}

![Generative Model](/images/202211/03-classification/4.010.jpg "Generative Model")

### Gaussian Distribution
- $ f_{\mu,\sum}(x) = \frac{1}{(2\pi)^{D/2}}\frac{1}{|\sum|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu)^T\sum^{-1}(x-\mu) \\} $
- input: vector x, output: probability of sampling x(实际是probability density，概率密度与概率成正比,此处简略为概率)
- The shape of the function determines by {{<color>}}mean $\mu${{</color>}} and {{<color>}}covariance matrix $\sum${{</color>}}(协方差矩阵)

![Gaussian Distribution](/images/202211/03-classification/4.014.jpg "Gaussian Distribution")

### Maximum Likelihood（找mean$\mu$和covariance matrix $\Sigma$的方法）
- mean $\mu$控制原点的位置。
- covariance matrix $\Sigma$决定图形的形状。
- 虽然图中左下角的点都可以求出相对于两个圈的概率，但是这两个概率的大小是不一样的。
- 给定一个Gaussian的$\mu$和$\Sigma$,就可以求出对应的Likelihood: 
  - $ L(\mu, \Sigma) = f_{\mu, \Sigma}(x^1)f_{\mu, \Sigma}(x^2)f_{\mu, \Sigma}(x^3)\dots\dots f_{\mu, \Sigma}(x^n) $
  - 这里的每一个$f_{\mu, \Sigma}(x^1)$展开，都是$ f_{\mu,\sum}(x) = \frac{1}{(2\pi)^{D/2}}\frac{1}{|\sum|^{1/2}} exp \\{  -\frac{1}{2}(x-\mu)^T\sum^{-1}(x-\mu)  \\} $
- Maximum Likelihood: $ \mu^\*, \Sigma^\* = arg \max\limits_{\mu, \Sigma} L(\mu, \Sigma) $
  - $\mu^\*$为取x的平均值: $ \mu^\* = \frac{1}{n}\sum\limits_{i=1}^n x^i $
  - $ \Sigma^\* = \frac{1}{n} \sum\limits_{i=1}^n(x^i-\mu^\*)(x^i-\mu^\*)^T $

![Maximum Likelihood](/images/202211/03-classification/4.017.jpg "Maximum Likelihood")

### 采用上诉方法得到的测试结果

| features | $\theta$ | test accuracy |
|--|--|--|
| `Defense`,`SP Defense` | $ \mu^1, \mu^2 $ : 2-dim vector <br/> $\Sigma^1, \Sigma^2$: 2*2 matrices | 47% |
| All the 7 features     | $ \mu^1\dots\mu^7 $ : 7-dim vector <br/> $\Sigma^1\dots\Sigma^7$: 7*7 matrices | 54% |

{{<color>}}结果不理想，需要重新调整模型。{{</color>}}

### Modifying Model (Ref: Bishop chapter 4.2.2)
- 给每一个Gaussian有一个自己的$\mu$和自己的covariance matrix $\Sigma$是很少见的
- 常见的做法是，不同的Class对应的Gaussian可以share相同的covariance matrix $\Sigma$

![Share Covariance matrix](/images/202211/03-classification/4.022.jpg "Share Covariance matrix")

#### 模型修改后如何计算$\mu$和$\Sigma$
- 假设有数量为n的class1,数量为m的class2
- likelihood: \begin{align} L(\mu^1, \mu^2, \Sigma) = & f_{\mu^1, \Sigma}(x^1)f_{\mu^1, \Sigma}(x^2)\dots\dots f_{\mu^1, \Sigma}(x^n) \cr \times &f_{\mu^2, \Sigma}(x^{n+1})f_{\mu^2, \Sigma}(x^{n+2})\dots\dots f_{\mu^2, \Sigma}(x^{n+m}) \end{align}
- 如下图， $\mu^1$, $\mu^2$和原来一样计算: \begin{align} \mu^1 & = \frac{1}{n}\sum\limits_{i=1}^n x^i \cr \mu^2 & = \frac{1}{m}\sum\limits_{i=1}^m x^i \end{align}
- $\Sigma^\*$的计算修改为：$ \Sigma = \frac{n}{n+m}\Sigma^1 + \frac{m}{n+m}\Sigma^2 $

![Compute](/images/202211/03-classification/4.023.jpg "Compute")

#### 模型修改后画出的图形
- 从原来的曲线，变成了一条直线
- 由于边界(boundary)是一条直线，所以这种模型也叫做Linear Model。
- {{<color green>}}在这个模型下，考虑所有的7个features进行计算，则accuracy从原来的54%上升到73%{{</color>}}

### 总结一下3个步骤
- Function Set(Model):
  \begin{align} P(C_1|x) &= \frac{P(C_1)P(x|C_1)}{P(C_1)P(x|C_1)+P(C_2)P(x|C_2)} \cr 
  & \begin{cases}  \text{if} P(C_1|x) > 0.5 & \text{, output: class 1} \cr Otherwise & \text{, output: class 2} \end{cases}
  \end{align}
- Goodness of a function:
  - The mean $\mu$ and covariance $\Sigma$ that maximizing the likelihood(the probability of generating data)
- Find the best function: easy

### Probability Distribution
- You can always use the distribution you like
- 假设$P(x|C^1)$构成Class1的x有K个，且K个x想对于Class1的几率是独立的，则：$ P(x|C1) = P(x_1|C_1)P(x_2|C_1)\cdots P(x_K|C_1) $，这个会得到1-D Gaussian,参数会进一步简化
- For binary features, you may assume they are from `Bernouli distributions`.
- If you assume all the dimensions are independent, then you are using `Naive Bayes Classifier`.

### Posterior Probability
- 设有表达式(1)上下同时除上表达式$ P(C_1)P(x|C_1) $得到表达式(2)
- 设$ z = ln\frac{P(C_1)P(x|C_1)}{P(C_2)P(x|C_2)} $,则表达式(2)变为表达式(3)
- 表达式(3)和(4)等价，为`Sigmoid Function`
\begin{align}
  P(C_1|x) &= \frac{P(C_1)P(x|C_1)}{P(C_1)P(x|C_1)+P(C_2)P(x|C_2)}  \tag{1} \cr
  &= \frac{1}{1+\frac{P(C_2)P(x|C_2)}{P(C_1)P(x|C_1)}} \tag{2} \cr
  &= \frac{1}{1 + exp^{-z}} \tag{3} \cr 
  &= \sigma(z) \tag{4}
\end{align}

#### 求z
- 设$N_1$是Class1出现的次数，$N_2$是Class2出现的次数
- 表达式(3)和(4)为Gaussian的Distribution
- 表达式(5)上下同时除以$\frac{1}{(2\pi)^{D/2}}$得到表达式(6)
\begin{align}
z &= ln\frac{P(C_1)P(x|C_1)}{P(C_2)P(x|C_2)} \cr
&= ln\frac{P(C_1)}{P(C_2)} + ln\frac{P(x|C_1)}{P(x|C_2)} \tag{1} \cr
ln\frac{P(C_1)}{P(C_2)} &=\frac{\frac{N_1}{N_1+N_2}}{\frac{N_2}{N_1+N_2}} = \frac{N_1}{N_2} \tag{2} \cr
P(x|C_1) &= \frac{1}{(2\pi)^{D/2}}\frac{1}{|\Sigma^1|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu^1)^T(\Sigma^1)^{-1}(x-\mu^1) \\} \tag{3} \cr
P(x|C_2) &= \frac{1}{(2\pi)^{D/2}}\frac{1}{|\Sigma^2|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu^2)^T(\Sigma^2)^{-1}(x-\mu^2) \\} \tag{4} \cr  
ln\frac{P(x|C_1)}{P(x|C_2)} &= ln\frac{\frac{1}{(2\pi)^{D/2}}\frac{1}{|\Sigma^1|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu^1)^T(\Sigma^1)^{-1}(x-\mu^1) \\}}
                                      {\frac{1}{(2\pi)^{D/2}}\frac{1}{|\Sigma^2|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu^2)^T(\Sigma^2)^{-1}(x-\mu^2) \\}} \tag{5} \cr
&= ln\frac{\frac{1}{|\Sigma^1|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu^1)^T(\Sigma^1)^{-1}(x-\mu^1) \\}}
          {\frac{1}{|\Sigma^2|^{1/2}} exp \\{ -\frac{1}{2}(x-\mu^2)^T(\Sigma^2)^{-1}(x-\mu^2) \\}} \tag{6} \cr
&= ln\frac{|\Sigma^2|^{1/2}}{|\Sigma^1|^{1/2}}exp \\{ -\frac{1}{2}\[(x-\mu^1)^T(\Sigma^1)^{-1}(x-\mu^1) - (x-\mu^2)^T(\Sigma^2)^{-1}(x-\mu^2)\] \\}  \tag{7} \cr
&= ln\frac{|\Sigma^2|^{1/2}}{|\Sigma^1|^{1/2}} - \frac{1}{2}\[(x-\mu^1)^T(\Sigma^1)^{-1}(x-\mu^1) - (x-\mu^2)^T(\Sigma^2)^{-1}(x-\mu^2)\] \tag{8} \cr
(x-\mu^1)^T(\Sigma^1)^{-1}(x-\mu^1) &= x^T(\Sigma^1)^{-1}x - x^T(\Sigma^1)^{-1}\mu^1 - (\mu^1)^T(\Sigma^1)^{-1}x + (\mu^1)^T(\Sigma^1)^{-1}\mu^1  \cr
&= x^T(\Sigma^1)^{-1}x - 2(\mu^1)^T(\Sigma^1)^{-1}x + (\mu^1)^T(\Sigma^1)^{-1}\mu^1 \cr
(x-\mu^2)^T(\Sigma^2)^{-1}(x-\mu^2) &= x^T(\Sigma^2)^{-1}x - 2(\mu^2)^T(\Sigma^2)^{-1}x + (\mu^2)^T(\Sigma^2)^{-1}\mu^2 \cr
z &= ln\frac{|\Sigma^2|^{1/2}}{|\Sigma^1|^{1/2}} - \frac{1}{2}x^T(\Sigma^1)^{-1}x + (\mu^1)^T(\Sigma^1)^{-1}x - \frac{1}{2}(\mu^1)^T(\Sigma^1)^{-1}\mu^1 \cr
  &+ \frac{1}{2}x^T(\Sigma^2)^{-1}x - (\mu^2)^T(\Sigma^2)^{-1}x + \frac{1}{2}(\mu^2)^T(\Sigma^2)^{-1}\mu^2 + ln\frac{N_1}{N_2}
\end{align}


#### 求 $\sigma(z)$
- 当$ \Sigma_1 = \Sigma_2 = \Sigma $时，表达式(1)变为表达式(2)
- 设: $ w^T = (\mu_1 - \mu_2)^T\Sigma^{-1} $以及$ b = -\frac{1}{2}(\mu^1)^T(\Sigma^1)-1\mu^1 + \frac{1}{2}(\mu^2)^T(\Sigma^2)-1\mu^2 + ln\frac{N_1}{N_2} $则(2)可以推导为(3)
- In generative model, we estimate $ N_1, N_2, \mu^1, \mu^2, \Sigma $, then we have w and b.
\begin{align}
z &= ln\frac{|\Sigma^2|^{1/2}}{|\Sigma^1|^{1/2}} - \frac{1}{2}x^T(\Sigma^1)^{-1}x + (\mu^1)^T(\Sigma^1)^{-1}x - \frac{1}{2}(\mu^1)^T(\Sigma^1)^{-1}\mu^1 \cr
  &+ \frac{1}{2}x^T(\Sigma^2)^{-1}x - (\mu^2)^T(\Sigma^2)^{-1}x + \frac{1}{2}(\mu^2)^T(\Sigma^2)^{-1}\mu^2 + ln\frac{N_1}{N_2}  \tag{1}\cr
  &= (\mu_1 - \mu_2)^T\Sigma^{-1}x -\frac{1}{2}(\mu^1)^T(\Sigma^1)-1\mu^1 + \frac{1}{2}(\mu^2)^T(\Sigma^2)-1\mu^2 + ln\frac{N_1}{N_2} \tag{2}\cr
  &= w \cdot x + b  \tag{3}  \cr
P(C_1|x) &= \sigma(z) \cr &= \sigma(w \cdot x + b)
\end{align}

{{<color>}}How about directly find w and b?{{</color>}}

## reference video

{{< youtube fZAZUYEeIMg >}}
