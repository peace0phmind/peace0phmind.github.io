---
title: "Fat vs Deep Network"
description: "06-fat-vs-deep-network"
keywords: "06,fat,deep,network"

date: 2022-11-24T10:01:58+08:00
lastmod: 2022-11-24T10:01:58+08:00

author: peace0phmind
url: "posts/202211/06-fat-vs-deep-network"

draft: true

categories:
  -
tags:
  - fat
  - deep
  - network

---

## 全量空间与样本空间
- 全量空间(理想状态)： If we can collect all datasets in the universe $ D_{all} $, we can find the best threshold $h^{all}$
  - $ h^{all} = \text{arg}\min\limits_h L (h, D_{all}) $ 
- 样本空间(现实发生)： We only collect some examples $D_{train}$ from $D_{all}$
  - $ D_{train} = {(x^1, \hat{y}^1), (x^2, \hat{y}^2), \dots, (x^N, \hat{y}^N)} $
  - $ (x^n, \hat{y}^n) \sim D_{all} $, 采样满足independently and identically distributed (i.i.d.)特性
  - 通过$ D_{train} $找到最小Loss的那个h，叫$ h^{train} $： $ h^{train} = \text{arg}\min\limits_h L(h, D_{train}) $
- In most applications, you cannot obtain $ D_{all}$. (Testing data $D_{test}$ as the proxy of $D_{all}$)

We hope $ L({\color{blue}h^{train}}, {\color{red}D_{all}}) $ and $ L({\color{red}h^{all}}, {\color{red}D_{all}}) $ are close.

We want $ L({\color{blue}h^{train}}, {\color{red}D_{all}}) - L({\color{red}h^{all}}, {\color{red}D_{all}}) \leq \delta $ 

### How to make $ P(D_{train} \text{ is bad}) smaller $
- $ P(D_{train} \text{ is bad}) = |H| \cdot 2exp(-2N\varepsilon^2) $
- Larger N and smaller $ |H| $, 样本空间数量尽可能大，全量空间数量尽可能小

### If we want $ P(D_{train} \text{ is bad})  \leq \delta $
- How many training examples do we need?
- $ |H|\cdot 2exp(-2N\varepsilon^2) \leq \delta  \Rightarrow N \geq \frac{log(2|H|/\delta)}{2\varepsilon^2} $

```python
# 假设 H = 10000, delta = 0.1, epsilon = 0.1
import math
math.log(2*10000/0.1, math.e)/(2*0.1**2)
# output is: 610.3036322765086
```

### Tradeoff(权衡) of Model Complexity
- Larger N and smaller $|H| \Rightarrow L(h^{train}, D_{all}) - L(h^{all}, D_{all}) \leq \delta $
- Smaller $ |H| \Rightarrow \text{Larger }L(h^{all}, D_{all})$

## Reference video

{{< youtube _j9MVVcvyZI >}}

{{< youtube xQXh3fSvD1A >}}

{{< youtube OP5HcXJg2Aw >}}

{{< youtube yXd2D5J0QDU >}}

{{< youtube SoCywZ1hZak >}}
