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
- 计算$w=w^0$时，对$L$的微分是多少：$\frac{{\partial}L}{{\partial}W}|_{w=w^0}$
  - 如果计算出来的结果为负数，则增加$w$
  - 如果计算出来的结果为正数，则减少$w$
  - 增加或减少的数值为：${\color{red}\eta}\frac{{\partial}L}{{\partial}W}|_{w=w^0}$, $\color{red}\eta$:叫learning rate,是一个hyperparameter
  - 这个过程用的数学表达式是：$ w^1 \leftarrow w^0 - {\color{red}\eta}\frac{{\partial}L}{{\partial}W}|_{w=w^0} $
  - 重复上述步骤不断更新$w$。两种状况会停下来:
    - 更新的次数达到预设值
    - 微分为0

当两个参数$w$, $b$时:
- 随机初始化$w^0$, $b^0$
- 计算两个微分值
  - $ \frac{\partial L}{\partial w}|_{w=w^0, b=b^0} $ 用$w$的微分更新$w$的值
  - $ w^1 \leftarrow w^0 - {\color{red}\eta}\frac{\partial L}{\partial w}|_{w=w^0, b=b^0} $
  - $ \frac{\partial L}{\partial b}|_{w=w^0, b=b^0} $ 用$b$的微分更新$b$的值
  - $ b^1 \leftarrow b^0 - {\color{red}\eta}\frac{\partial L}{\partial b}|_{w=w^0, b=b^0} $
  - Update $w$ and $b$ interatively

通过观察资料发现数据有7天为一个周期，所以使用新的公式进行调整, 并得到下面数据：
| days | function | training loss | test loss |
|--|--|--|--|
| 1  | $ y = b + wx_{\color{red}1} $                       | $ L = 0.48k $ | $ L' = 0.58k $ |
| 7  | $ y = b + \sum\limits_{j=1}^{\color{red}7}w_jx_j $  | $ L = 0.38k $ | $ L' = 0.49k $ |
| 28 | $ y = b + \sum\limits_{j=1}^{\color{red}28}w_jx_j $ | $ L = 0.33k $ | $ L' = 0.46k $ |
| 56 | $ y = b + \sum\limits_{j=1}^{\color{red}56}w_jx_j $ | $ L = 0.32k $ | $ L' = 0.46k $ |

上述模型有个共同的名字`Linear Models`

`hyperparameter`: 需要人来设置的参数

`local minima`: 局部最小值

`global minima`: 全局最小值

### 总结Machine Learning训练的简单步骤
- function with unknown
- define loss from training data
- optimization

## 打破Linear Models的局限性，对模型的进一步调整
不同的w和不同的b对Linear Models的影响如蓝色线。红色表示可能的真实趋势。这种来自于Model的限制叫做`Model Bias`。
![Linear Models的局限性](/images/202211/02-ai-introduce/02.0002.jpg)

### All Piecewise Linear Curves
All Piecewise Linear Curves = constant + sum of a set of `hard sigmoid`
![Piecewise Linear Curves](/images/202211/02-ai-introduce/02.0003.jpg)

### sigmoid function
$$ 
\begin{align}
y &= {\color{red}c}\frac{1}{1+e^{-({\color{green}b}+{\color{blue}w}x_1)}}  \cr
&= {\color{red}c}\\,sigmoid({\color{green}b}+{\color{blue}w}x_1)
\end{align}
$$



## 参考
{{< youtube Ye018rCVvOo >}}
{{< youtube bHcJCp2Fyxs >}}

{{< youtube Dr-WRlEFefw >}}
{{< youtube ibJpTrp5mcE >}}
{{< youtube fegAeph9UaA >}}
{{< youtube fZAZUYEeIMg >}}
{{< youtube hSXFuypLukA >}}
