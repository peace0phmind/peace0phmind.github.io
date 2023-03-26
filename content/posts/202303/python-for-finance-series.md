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

### Part One

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


## Reference
- [Identifying Outliers — Part One](https://python.plainenglish.io/identifying-outliers-part-one-c0a31d9faefa)