---
title: "Python for Finance Series: Identifying outliers"
description: "python-for-finance-series-identifying-outliers"
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

### Part Two: 以移动平均数和标准差为界

```python
# 这里，我们重复使用第一部分中相同的数据集。

import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams['figure.dpi'] = 300
df = yf.download('AAPL',
                 start = '2000-01-01',
                 end= '2010-12-31')
d1 = pd.DataFrame(df['Adj Close'])
d1.rename(columns={'Adj Close':'adj_close'}, inplace=True)
d1['simple_rtn']=d1.adj_close.pct_change()
d1.head()

# 为了计算均值和标准差，选择了一个 21 天的窗口，因为它代表一个月中的平均交易日。您可以选择任何日期，但敏感度会有所不同。
d1[['mean', 'std']] = d1['simple_rtn'].rolling(window=21).agg(['mean', 'std'])
# 处理后，数据中会有很多NaNs,需要删除他们
d1.dropna(inplace=True)


# 用如下代码，结合标准差进行画图
fig, ax = plt.subplots()

ax.plot(d1.index, d1['simple_rtn'], label='simple_rtn',c='c', lw=1)
ax.plot(d1.index, d1['mean'], label= 'mean',c='r')
ax.plot(d1.index, d1[ 'std'], label= 'std',linestyle='-',c='m', lw=1 )
ax.plot(d1.index, -d1['std'],label='-std', linestyle='-',c='m', lw=1)
ax.legend(loc='lower right')

```

绘制一个图形并找出边界所在的位置：

![](/images/202303/python-for-finance-series/010.webp_640x370)

改用 std 的三倍会怎样？

![](/images/202303/python-for-finance-series/011.webp_640x370)

嗯...有些超过了。我们将其更改为两倍的标准差。

```python

fig, ax = plt.subplots()
#d1.plot(use_index=True)
#d1[['simple_rtn', 'mean', 'std', 'std']].plot(ax=ax)
ax.plot(d1.index, d1['simple_rtn'], label='simple_rtn',c='c', lw=1)
ax.plot(d1.index, d1['mean'], label= 'mean',c='r')
ax.plot(d1.index, 2*d1['std'], label= 'std',linestyle='-',c='m', lw=1 )
ax.plot(d1.index, -2*d1['std'],label='-std', linestyle='-',c='m', lw=1)
ax.legend(loc='lower right')
```

![](/images/202303/python-for-finance-series/012.webp_640x370)

现在是寻找那些异常值的时候了。

```python
def get_outliers(df, mu=mu, sigma=sigma, n_sigmas=2):
    '''
    df: the DataFrame
    mu: mean
    sigmas: std
    n_sigmas: number of std as boundary
    '''
    x = df['simple_rtn']
    mu = df['mean']
    sigma = df['std']
    
    if (x > mu+n_sigmas*sigma) | (x<mu-n_sigmas*sigma):
        return 1
    else:
        return 0
d1['outlier']=d1.apply(get_outliers, axis=1)
outliers = d1.loc[d1['outlier'] == 1, ['simple_rtn']]
outliers.head()
```

以上的代码片段可以重构如下：

```python
cond = (d1['simple_rtn'] > d1['mean'] + d1['std'] * 2) | (d1['simple_rtn'] < d1['mean'] - d1['std'] 
d1['outliers'] = np.where(cond, 1, 0)
```

看异常值信息。我们知道在2,745个数据点中有127个异常值（约占4.6％）：

如果我们将两倍的标准差作为边界值，我们得到超出范围的数据点约占4.6％。我们可以挑选这些异常值，将它们放入另一个DataFrame中，并在图表中显示出来：

```python
fig, ax = plt.subplots()
ax.plot(d1.index, d1.simple_rtn, 
        color='blue', label='Normal')
ax.scatter(outliers.index, outliers.simple_rtn, 
           color='red', label='Anomaly')
ax.set_title("Apple's stock returns outliers")
ax.legend(loc='lower right')
```

![](/images/202303/python-for-finance-series/013.webp_640x370)

看起来有点过度了。让我们将标准差调整为2.5倍。这一次，我们得到41个异常值（约占1.5％）：

![](/images/202303/python-for-finance-series/014.webp_640x370)

需要注意的一件事是，当附近有很多较大的收益时，算法将第一个收益视为异常值，第二个收益视为正常观察值（如圆圈所示）。这可能是因为第一个异常值进入了滚动窗口并影响了移动平均/标准差。

滑动窗口的大小和标准差都会影响最终结果。我们可以微调它们中的每一个来更好地满足我们的要求。与之前的方法相比，移动平均方法更为敏感。您可以查看以前的文章以获得更好的理解.
 
### Part Three: 指数移动平均
这里我们将使用指数移动平均（EMA）作为边界。方法与以前相同，区别在于计算EMA均值和标准差的方式。

```python
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams['figure.dpi'] = 300
df = yf.download('AAPL',
                 start = '2000-01-01',
                 end= '2010-12-31')
d1 = pd.DataFrame(df['Adj Close'])
d1.rename(columns={'Adj Close':'adj_close'}, inplace=True)
d1['simple_rtn']=d1.adj_close.pct_change()
d1.head()

# 下面的代码将展示如何用pandas库来计算EMA均值和标准差, 窗口大小为21天
d1[['mean', 'std']] = d1['simple_rtn'].ewm(span=21).agg(['mean', 'std'])
d1.head()

# 下面的代码将展示如何删除数据集中的NaN值
d1.dropna(inplace=True)
# 让我们绘制一张图表，找出边界的位置。

fig, ax = plt.subplots()
ax.plot(d1.index, d1['simple_rtn'], label='simple_rtn',c='c', lw=1)
ax.plot(d1.index, d1['mean'], label= 'mean',c='r')
ax.plot(d1.index, d1[ 'std'], label= 'std',linestyle='-',c='m', lw=1 )
ax.plot(d1.index, -d1['std'],label='-std', linestyle='-',c='m', lw=1)
ax.legend(loc='lower right')
```

![](/images/202303/python-for-finance-series/020.webp_640x370)

与移动平均相比，图中的峰值更加突出，但是其缩放比例保持不变。从第二部分中学习到的经验，我们知道将3倍标准差作为边界会导致过度检测。因此，我们将使用2倍标准差作为边界。

```python
fig, ax = plt.subplots()
ax.plot(d1.index, d1['simple_rtn'], label='simple_rtn',c='c', lw=1)
ax.plot(d1.index, d1['mean'], label= 'mean',c='r')
ax.plot(d1.index, 2*d1['std'], label= 'std',linestyle='-',c='m', lw=1 )
ax.plot(d1.index, -2*d1['std'],label='-std', linestyle='-',c='m', lw=1)
ax.set_title('2 times std')
ax.legend(loc='lower right')
```

![](/images/202303/python-for-finance-series/021.webp_640x370)

通过重复利用之前的代码，我们可以轻松地得到异常值。

```python
def get_outliers(df, mu=mu, sigma=sigma, n_sigmas=2):
    '''
    df: the DataFrame
    mu: mean
    sigmas: std
    n_sigmas: number of std as boundary
    '''
    x = df['simple_rtn']
    mu = df['mean']
    sigma = df['std']
    
    if (x > mu+n_sigmas*sigma) | (x<mu-n_sigmas*sigma):
        return 1
    else:
        return 0
    
d1['outlier']=d1.apply(get_outliers, axis=1)
outliers = d1.loc[d1['outlier'] == 1, ['simple_rtn']]
outliers.head()
```

以上的代码片段可以重构如下：

```python
condition = (d1['simple_rtn'] > d1['mean'] + d1['std'] * 2) | (d1['simple_rtn'] < d1['mean'] - d1['std']* 2) 
d1['outliers'] = np.where(condition, 1, 0)
```

查看数据信息，我们可以得知在2745个数据点中有58个异常值（约占2.1%）。

让我们将这些异常值绘制到一张图表上。

![](/images/202303/python-for-finance-series/022.webp_640x370)

和移动平均方法一样，该方法也存在相同的问题。在图表中，有几个较大的收益被误判为正常观测值，如圆圈区域所示。与之前的方法相比，移动平均方法更加敏感，但也会漏检一些异常值。



## Reference
- [Identifying Outliers — Part One](https://python.plainenglish.io/identifying-outliers-part-one-c0a31d9faefa)
- [Identifying Outliers — Part Two](https://betterprogramming.pub/identifying-outliers-part-two-4c00b2523362)
- [Identifying Outliers — Part Three](https://medium.com/swlh/identifying-outliers-part-three-257b09f5940b)