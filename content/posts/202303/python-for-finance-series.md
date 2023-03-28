---
title: "Python for Finance Series"
description: "python-for-finance-series"
keywords: "python,for,finance,series"

date: 2023-03-25T09:40:10+08:00
lastmod: 2023-03-25T09:40:10+08:00

author: peace0phmind
url: "posts/202303/python-for-finance-series"

draft: true

categories:
  -
tags:
  - python
  - finance
  - series

---

## Identifying Outliers

### Part One: 以均值和标准差为界

Pandas有很多方便的方法来清理混乱的数据，比如dropna、drop_duplicates等。但是，查找和删除异常值是我们希望拥有但目前还不存在的功能之一。在这里，我想与大家详细分享如何一步一步地做到这一点：

定义异常值的关键在于我们采用的边界。这里我将给出3种不同的方式来定义边界，分别是Average mean、Moving Average mean和Exponential Weighted Moving Average mean。

```python
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

# 数据准备
# 这里我以苹果10年的股票历史价格和雅虎财经的回报为例，当然你可以使用任何数据。

plt.style.use('seaborn')
plt.rcParams['figure.dpi'] = 300
df = yf.download('AAPL',
                 start = '2000-01-01',
                 end= '2010-12-31')

# 由于我们只关心回报，因此DataFrame (d1)创建了一个新的来保存调整后的价格和回报。

d1 = pd.DataFrame(df['Adj Close'])
d1.rename(columns={'Adj Close':'adj_close'}, inplace=True)
d1['simple_rtn']=d1.adj_close.pct_change()
d1.head()

# 以均值和标准差为界
# 计算simple_rtn的均值和标准差
d1_mean = d1['simple_rtn'].agg(['mean', 'std'])

# 如果我们使用均值和一个标准差作为边界，结果将如下所示
fig, ax = plt.subplots(figsize=(10,6))
d1['simple_rtn'].plot(label='simple_rtn', legend=True, ax = ax)
plt.axhline(y=d1_mean.loc['mean'], c='r', label='mean')
plt.axhline(y=d1_mean.loc['std'], c='c', linestyle='-.',label='std')
plt.axhline(y=-d1_mean.loc['std'], c='c', linestyle='-.',label='std')
plt.legend(loc='lower right')

```

标准差如下图：

![](/images/202303/python-for-finance-series/001.webp_640x370)

3倍标准差如下图：

![](/images/202303/python-for-finance-series/002.webp_640x370)

看起来不错！现在是时候寻找那些异常值了

```python
mu = d1_mean.loc['mean']
sigma = d1_mean.loc['std']

def get_outliers(df, mu=mu, sigma=sigma, n_sigmas=3):
    '''
    df: the DataFrame
    mu: mean
    sigmas: std
    n_sigmas: number of std as boundary
    '''
    x = df['simple_rtn']
    mu = mu
    sigma = sigma
    
    if (x > mu+n_sigmas*sigma) | (x<mu-n_sigmas*sigma):
        return 1
    else:
        return 0

# 将规则应用于get_outliers股票价格回报后，将创建一个新列

d1['outlier'] = d1.apply(get_outliers, axis=1)
d1.head()

```

```python
# 上面代码片段可以重构为：

import numpy as np

mu = d1_mean.loc['mean']
sigma = d1_mean.loc['std']

cond = (d1['simple_rtn'] > mu + sigma * 2) | (d1['simple_rtn'] < mu - sigma * 2)
d1['outlier'] = np.where(cond, 1, 0)
```


```python
# 我们可以通过计算值来检查我们发现了多少异常值。
d1.outlier.value_counts()

# 如果我们将 std 的 3 倍设置为边界，我们会发现 30 个异常值。
# 我们可以把那些离群值挑出来，放到另一个里DataFrame，然后显示在图表中
outliers = d1.loc[d1['outlier'] == 1, ['simple_rtn']]
fig, ax = plt.subplots()
ax.plot(d1.index, d1.simple_rtn, 
        color='blue', label='Normal')
ax.scatter(outliers.index, outliers.simple_rtn, 
           color='red', label='Anomaly')
ax.set_title("Apple's stock returns")
ax.legend(loc='lower right')
plt.tight_layout()

plt.show()
```

![](/images/202303/python-for-finance-series/003.webp_640x370)

在上图中，我们可以观察到标有红点的异常值。

Winsorization是用较小的数据值替换指定数量的极端值的过程。它是以工程师转型生物统计学家查尔斯·P·温索尔（1895-1951）的名字命名的。其效果类似于信号处理中的裁剪。

一种典型的策略是将所有异常值设置为数据的指定百分位数；例如，95％的Winsorization会将所有低于第5个百分位数的数据设置为第5个百分位数，并将高于第95个百分位数的数据设置为第95个百分位数。可以在pandas中使用clip()函数实现这个过程。

```python
outlier_cutoff = 0.01
d1.pipe(lambda x:x.clip(lower=x.quantile(outlier_cutoff),
                        upper=x.quantile(1-outlier_cutoff),
                        axis=1,
                        inplace=True))
d1
```

在进行Winsorization操作后，DataFrame的形状（即列数和行数）不会改变，但是其中的数据值会发生变化。具体来说，原始数据中低于第5个百分位数的数值会被替换为第5个百分位数，而高于第95个百分位数的数值会被替换为第95个百分位数。

```python
fig, ax = plt.subplots()
ax.plot(d.index, d.simple_rtn, 
        color='red', label='Normal')
ax.plot(d1.index, d1.simple_rtn, 
        color='blue', label='Anomaly_removed')
ax.set_title("stock returns outliers_winsorize returns")
ax.legend(loc='lower right');
```

![](/images/202303/python-for-finance-series/004.webp_640x370)

我更喜欢使用Winsorization的原因是，在同时使用多个特征进行机器学习模型训练时，相比简单的去除异常值（simple return），Winsorization不会意外地移除任何信息。


## Reference
- [Identifying Outliers — Part One](https://python.plainenglish.io/identifying-outliers-part-one-c0a31d9faefa)