---
title: "Regression"
description: "regression"
keywords: "regression"

date: 2022-11-08T14:27:33+08:00
lastmod: 2022-11-08T14:27:33+08:00

author: peace0phmind
url: "posts/202211/02-regression"

draft: false

categories:
  - machine-learning
tags:
  - regression

---

`Regression`: Input a vector, the function outputs a scalar.

# 单参数到历史多参数的模型演进

## 使用简单模型
预测问题：根据前面的浏览数据，预测后面的浏览量

### Function with Unknown Parameters
`Model`: $y = b + wx_1$ <br/>
$y$(`Label`): no. of views on 2/26， $x_1$(`feature`): no. of views on 2/25  <br/>
$w$(`weight`) and $b$(`bias`) are unknown parameters (learned from data)  <br/>

### Define Loss from Training Data
- Loss is a function of parameters: $L(b, w)$ <br/>
- Loss: how good a set of values is.          <br/>
- Loss: $ L = \frac{1}{N}\sum\limits_{n=1}^N e_n$  <br/>
  - $e = |y - \hat{y}|$ $L$ is mean absolute error (MAE) <br/>
  - $e = (y-\hat{y})^2$ $L$ is mean square error (MSE) <br/>
  - if $y$ and $\hat{y}$ are both probability distributions, then use `Cross-Entropy`

使用不同的参数，计算出来的Loss画出来的等高线图叫做：`Error Surface`
![等高线图](/images/202211/02-regression/01.0001.jpg "等高线图: Error Surface")

### Optimization
找一个$w$和$b$，使$L$最小： $ w^\*, b^\* = arg \min\limits_{w, b} L$
这种找到最小$w$和$b$的方法叫做：`Gradient Descent`

#### 简述`Gradient Descent`过程
以一个参数$w$为例描述`Gradient Descent`的过程: 
- 随机初始化点$w^0$
- 计算$w=w^0$时，对$L$的微分是多少：$\frac{{\partial}L}{{\partial}W}|_{w=w^0}$
  - 如果计算出来的结果为负数，则增加$w$
  - 如果计算出来的结果为正数，则减少$w$
  - 增加或减少的数值为：${\color{red}\eta}\frac{{\partial}L}{{\partial}W}|_{w=w^0}$, $\color{red}\eta$:叫{{<clr>}}learning rate{{</clr>}},是一个hyperparameter
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

#### 使用单参数的多个连续的历史记录

通过观察资料发现数据有7天为一个周期，所以使用新的公式进行调整, 并得到下面数据：
| days | function | training loss | testing loss |
|--|--|--|--|
| 1  | $ y = b + wx_{\color{red}1} $                       | $ L = 0.48k $ | $ L' = 0.58k $ |
| 7  | $ y = b + \sum\limits_{j=1}^{\color{red}7}w_jx_j $  | $ L = 0.38k $ | $ L' = 0.49k $ |
| 28 | $ y = b + \sum\limits_{j=1}^{\color{red}28}w_jx_j $ | $ L = 0.33k $ | $ L' = 0.46k $ |
| 56 | $ y = b + \sum\limits_{j=1}^{\color{red}56}w_jx_j $ | $ L = 0.32k $ | $ L' = 0.46k $ |

上述模型有个共同的名字`Linear Models`

{{<clr>}}调整模型参数，观察Training Loss和Testing Loss的变化，挑选合适的模型{{</clr>}}
#### 名词解释

`hyperparameter`: 需要人来设置的参数

`local minima`: 局部最小值

`global minima`: 全局最小值

### 总结Machine Learning训练的简单步骤
- function with unknown
- define loss from training data
- optimization

## 打破模型局限
不同的w和不同的b对Linear Models的影响如蓝色线。红色表示可能的真实趋势。这种来自于Model的限制叫做`Model Bias`。
![Linear Models的局限性](/images/202211/02-regression/02.0002.jpg "Linear Models的局限性")

### All Piecewise Linear Curves
All Piecewise Linear Curves = constant + sum of a set of `Hard Sigmoid`
![Piecewise Linear Curves](/images/202211/02-regression/02.0003.jpg "Piecewise Linear Curves")

### sigmoid
\begin{align*}
y &= {\color{red}c}\frac{1}{1+e^{-({\color{green}b}+{\color{blue}w}x_1)}}  \cr
&= {\color{red}c}\\,sigmoid({\color{green}b}+{\color{blue}w}x_1)
\end{align*}

调整$ {\color{blue}w}, {\color{green}b}, {\color{red}c} $对应的函数图像
![Sigmoid Parameters](/images/202211/02-regression/02.0004.jpg "Sigmoid Parameters")

相对于红色线段，可以用多个`Sigmoid`函数组合出来，将0:`constant`和1,2,3`sigmoid`加起来就是红色线段

\begin{align*}
b\tag{0}\cr
{\color{red}c_1}\\,sigmoid({\color{green}b_1}+{\color{blue}w_1}x_1)\tag{1}\cr
{\color{red}c_2}\\,sigmoid({\color{green}b_2}+{\color{blue}w_2}x_1)\tag{2}\cr
{\color{red}c_3}\\,sigmoid({\color{green}b_3}+{\color{blue}w_3}x_1)\tag{3}\cr
\textcolor{red}{\text{red curve}}\text{ will be:} \cr
y = b + \sum_{i=1}^3{\color{red}c_i}\\,sigmoid({\color{green}b_i}+{\color{blue}w_i}x1)
\end{align*}


![Sigmoid Parameters](/images/202211/02-regression/02.0005.jpg "Sigmoid Parameters")

基于sigmoid的模型，对原来的模型进行调整如下：
\begin{align*}
y &= b+wx_1  \cr
& \Downarrow  \cr
y &= b + \sum_{i=1}^n {\color{red}c_i} \\, sigmoid({\color{green}b_i}+{\color{blue}w_i}x_i) \cr
y &= b + \sum_{j=1}^m w_jx_j  \cr
& \Downarrow  \cr
y &= b + \sum_{i=1}^n {\color{red}c_i} \\, sigmoid({\color{green}b_i}+\sum_{j=1}^m{\color{blue}w_{ij}}x_j)
\end{align*}

使$n=3, m=3$对表达式$y = b + \sum_{i=1}^n {\color{red}c_i} \\, sigmoid({\color{green}b_i}+\sum_{j=1}^m{\color{blue}w_{ij}}x_j)$进行展开
\begin{align*}
r_1 &= {\color{green}b_1} + {\color{blue}w_{11}}x_1 + {\color{blue}w_{12}}x_2 + {\color{blue}w_{13}}x_3  \cr
r_2 &= {\color{green}b_2} + {\color{blue}w_{21}}x_1 + {\color{blue}w_{22}}x_2 + {\color{blue}w_{23}}x_3  \cr
r_3 &= {\color{green}b_3} + {\color{blue}w_{31}}x_1 + {\color{blue}w_{32}}x_2 + {\color{blue}w_{33}}x_3  \cr
&\Downarrow \cr
\begin{bmatrix} r_1 \cr r_2 \cr r_3 \end{bmatrix} &=
\begin{bmatrix} {\color{green}b_1} \cr {\color{green}b_2} \cr {\color{green}b_3} \end{bmatrix} + 
\begin{bmatrix}
{\color{blue}w_{11}} & {\color{blue}w_{12}} & {\color{blue}w_{13}}  \cr
{\color{blue}w_{21}} & {\color{blue}w_{22}} & {\color{blue}w_{23}}  \cr
{\color{blue}w_{31}} & {\color{blue}w_{32}} & {\color{blue}w_{33}}  \cr
\end{bmatrix}
\begin{bmatrix} x_1 \cr x_2 \cr x_3 \end{bmatrix}
\end{align*}

其中$\color{red}\sigma$表示`sigmoid`表达式
![展开图示](/images/202211/02-regression/02.0008.jpg "Sigmoid 展开图示")

如下图所示，x为`feature`；而所有的$W, {\color{green}b}, c^T, b$作为unknown parameters展开为一个长的一维向量，定义为$\color{red}\theta$
![unknown parameters](/images/202211/02-regression/02.0009.jpg "unknown parameters")

### Loss function
- Loss is a function of parameters $L(\theta)$
- Loss means how good a set of values is.

### Optimization of New Model
$ \theta^* = arg\\,\min\limits_\theta L$
- (Randomly) Pick initial values $\theta^0$
- 对所有参数$\theta$对$L$做微分，这里的$g$叫做`gradient`
```math
\begin{align}
gradient \Leftarrow g &=
\begin{bmatrix}
{\frac{\partial L}{\partial\theta_1}|_{\theta=\theta^0}}  \cr
{\frac{\partial L}{\partial\theta_2}|_{\theta=\theta^0}}  \cr
\vdots
\end{bmatrix} \cr
g &= \nabla L(\theta^0)
\end{align}
```
- 然后进行参数更新
```math
$$
\begin{bmatrix}
\theta_1^1  \cr \theta_2^1 \cr \vdots
\end{bmatrix} 
\leftarrow
\begin{bmatrix}
\theta_1^0  \cr \theta_2^0 \cr \vdots
\end{bmatrix}
-
\begin{bmatrix}
{\color{red}\eta}\frac{\partial L}{\partial\theta_1}|_{\theta=\theta^0} \cr
{\color{red}\eta}\frac{\partial L}{\partial\theta_2}|_{\theta=\theta^0} \cr
\vdots
\end{bmatrix}
$$

$$
\theta^1 \leftarrow \theta^0 - {\color{red}\eta}g
$$
```
- Compute gradient $ g = \nabla L(\theta^0) $

全部资料是$L$,批次编号为$L^1, L^2, L^3$。{{<clr>}}batch{{</clr>}}是进行参数更新的单位，即一个批次进行一次参数更新；{{<clr>}}epoch{{</clr>}}表示所有批次全部执行了参数更新。
![batch and epoch](/images/202211/02-regression/02.0010.jpg "batch and epoch")

### 使用$ Sigmoid \rightarrow ReLU $
- `Rectified Linear Unit (ReLU)`: $ {\color{red}c}\\,max(0, {\color{green}b} + {\color{blue}w}x_1) $
- 类似`sigmoid`和`ReLU`的函数在机器学习中叫做{{<clr>}}`Activation function`{{</clr>}}

#### 作个数不同的ReLU
- only one layer
- input features are the no. of views in the past 56 days

| model | training loss | testing loss |
|--|--|--|
| linear   | 0.32k | 0.46k |
| 10ReLU   | 0.32k | 0.45k |
| 100ReLU  | 0.28k | 0.43k |
| 1000ReLU | 0.27k | 0.43k |

#### 作多层ReLU
- 100 ReLU for each layer
- input features are the no. of views in the past 56 days
- `Better on training data, worse on unseen data`: {{<clr>}}`Overfittin`{{</clr>}} , see layer count 4.

| layer count | training loss | testing loss |
|--|--|--|
| 1 | 0.28k | 0.43k |
| 2 | 0.18k | 0.39k |
| 3 | 0.14k | 0.38k |
| 4 | 0.10k | 0.44k |

## Backpropagation
`Backpropgation`: an efficient way to compute $\sfrac{\partial L}{\partial w}$

### Gradient Descent
- 对每一个参数针对L进行偏微分得到: $\nabla L(\theta)$
- 使用`batch`的数据对参数$\theta$进行更新.
![Gradient Descent](/images/202211/02-regression/7.0001.jpg "Gradient Descent")

### Chain Rule
- case 1: $\frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}$
- case 2: $\frac{dz}{ds}=\frac{dz}{dx}\frac{dx}{ds}+\frac{dz}{dy}\frac{dy}{ds}$
![Chain Rule](/images/202211/02-regression/7.0002.jpg "Chain Rule")

### Forward and Backward pass:
- `Forward pass`: Compute $\sfrac{\partial z}{\partial w}$for all parameters
- `Backward pass`: Compute $\sfrac{\partial C}{\partial z}$ for all activation function inputs z
![Forward and Backward pass](/images/202211/02-regression/7.0003.jpg "Forward and Backward pass")

## Regularization
`Regularization`出现的背景：当原始数据有过多的feature和模型有大量的w，可能存在某些feature确实与最终的结果无关，在这种情况下可以先将所有feature包含进来，然后通过`Regularization`的思路对w进行优化，从而降低无效feature对最终结果的影响。
- 假设Model Function为$ y = b + \sum w_i x_i $
- 原来定义的Loss Function为$ L = \sum\limits_n( \hat{y}^n - ( b + \sum w_i x_i ) )^2$
- Regularization既是在上面Loss Function的基础上加上红色部分: $ L = \sum\limits_n( \hat{y}^n - ( b + \sum w_i x_i ) )^2 + \color{red}\lambda\sum(w_i)^2$
- {{<clr>}}The functions with smaller $w_i$ are better{{</clr>}}
- Why smooth functions are preferred?
  - If some noises corrupt input $x_i$ when testing. A smoother function has less influence.
  - 因为在进行预测时，有噪音输入的情况下，越smooth的function对输出造成的影响越不敏感。
- {{<clr>}}其中的$\lambda$也是一个hyperparameter{{</clr>}}

当我们调整$\lambda$的值，观察Loss的变化是，我们可以观察到如下信息：
- $\lambda$越大时，Regularization项影响就越大，整个function就越平滑
- Training随着$\lambda$的增加而增加
- Testing随着$\lambda$的增加先减少再增加
- We prefer smooth function, but don't be too smooth.
- 所以$\lambda$的选择值选择在Testing的Loss的转折点处

![Regularization Loss](/images/202211/02-regression/1.0001.jpg "Regularization Loss")

# TODO: 完成$ X \rightarrow X^x $的模型演进

# Reference Video
{{< youtube Ye018rCVvOo >}}
{{< youtube bHcJCp2Fyxs >}}

{{< youtube Dr-WRlEFefw >}}
{{< youtube ibJpTrp5mcE >}}
{{< youtube fegAeph9UaA >}}
