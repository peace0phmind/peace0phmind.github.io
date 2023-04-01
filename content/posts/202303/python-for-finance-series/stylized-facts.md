---
title: "Python for Finance Series: Stylized Facts"
description: "stylized-facts"
keywords: "stylized,facts"

date: 2023-04-01T14:43:43+08:00
lastmod: 2023-04-01T14:43:43+08:00

author: peace0phmind
url: "posts/202303/python-for-finance-series/stylized-facts"

draft: true

categories:
  -
tags:
  - stylized
  - facts

---

我们常说“让数据自己说话”。但是数据可以大声喊叫，也可以低声细语。有些数据特征容易发现，而其他一些特征则不太明显并深埋在噪音中。就像在你耳边低语一样，你必须努力去弄清楚它们在说什么。一旦你从数据中揭示出隐藏的信息，在某些情况下，你可能有机会通过寻找你认为将持续到未来的当前可用数据中的统计模式来预测未来。换句话说，找出一种方式，使未来看起来与现在非常相似，只是更长时间。本文的目的是向您展示如何获取那些通常被忽略但有用的数据特征。

在我们开始之前，让我们花一分钟时间思考一个简单的问题，即从一组随机生成的数据中我们能提取多少信息。大多数人可能可以列出一长串，如最大值、最小值、平均数、众数、中位数、方差、标准差、范围等等。人类的大脑可以进行抽象思考，其他动物无法做到这一点。这就是统计学有用的原因，因为它可以将数据转化为对人们有意义的信息。更重要的是，这些信息可以被利用来推断一些实证发现，即所谓的金融中的定式化实证事实。

本文末尾的参考文献¹给出的定式化事实的定义是：“资产价格的表面上随机波动确实共享一些相当非平凡的统计属性。这些属性在各种工具、市场和时间段中都很常见，被称为定式化实证事实。”

简单来说，它就是说，如果你想利用过去的数据来预测未来，未来的数据必须与过去的数据有一些共同点。否则，就没有意义。因此，过去和未来数据中的这些共同模式被称为定式化事实。在参考文献¹中还详细解释了金融资产中的广泛定式化事实。

有了定式化事实的概念，就有了另一个概念：平稳。对于时间序列数据，平稳时间序列是指其统计属性（如均值、方差、自相关等）随时间保持不变的时间序列。大多数统计预测方法基于这样的假设：通过使用数学转换，时间序列可以近似为平稳的。对于平稳序列的预测可以通过反转之前使用的任何数学转换来获得原始序列的预测。

好了，关于“定式化事实”和“平稳”就说这么多，现在让我们编写一些代码来说明这两个概念。

## 数据准备

```python
#import all the libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import scipy.stats as scs
import yfinance as yf  #the stock data from Yahoo Finance
import matplotlib.pyplot as plt #set the parameters for plotting
plt.style.use('seaborn')
plt.rcParams['figure.dpi'] = 300
df = yf.download('AAPL',
                 start = '2000-01-01',
                 end= '2010-12-31') #download Apple stock price
d1 = pd.DataFrame(df['Adj Close'])#create a df with only stock price
d1.rename(columns={'Adj Close':'adj_close'}, inplace=True)
d1['simple_rtn']=d1.adj_close.pct_change()#percentage return
d1['log_rtn'] = np.log(d1.adj_close/d1.adj_close.shift(1))
#log return with 1 day lag
d1.head()
```

我还想处理数据的一件事是去除异常值，我使用简单的均值和2倍标准差来设置边界。

```python
#get mean and std
mu = d1.describe().loc['mean', 'log_rtn']
sigma = d1.describe().loc['std', 'log_rtn']
condition = (d1['log_rtn'] > mu + sigma * 2) | (d1['log_rtn'] < mu - sigma * 2) #set the condition to be 2 times of std around mean
d1['outliers'] = np.where(condition, 1, 0)#like an if, else 
d1.head()

# 移除所有的异常值。
d1_removed_outliers = d1.loc[d1['outliers'] == 0].iloc[:, :-1]
d1_removed_outliers.head()

d1_removed_outliers.info()
# 正如您所看到的，剩下了2667个数据点，而原来有2765个数据点。为了方便，让我们再次将DataFrame命名为d1。
d1 = d1_removed_outliers

```

对数收益率和简单百分比收益率的区别可以在这里找到。简而言之，自然对数的微小变化可以直接解释为百分比变化。换句话说，只要变化足够小（在+/- 5%的范围内），百分比变化和自然对数变化几乎完全相同。事实上，如上表所示，simple_rtn和log_rtn中的数字非常接近。

我们可以检查simple_rtn和log_rtn之间的相关性：
```python
#计算皮尔逊相关系数。
d1[['simple_rtn', 'log_rtn']].corr()

# 这两个回报之间高度相关。甚至从热力图上也可以看出来。

# 使用Seaborn绘制热力图
cmap = sns.diverging_palette(220, 20, as_cmap=True)
ax = sns.heatmap(corr, annot=True, cmap=cmap,
                 square=True, linewidths=3,
                 linecolor='w')
ax.set_title('Autocorrelation Plots', fontsize=26)
sns.set(font_scale=2);

# Pandas的一个优点是可以很容易地立即获取这些描述性统计信息。
d1.describe().round(4)
```

## 收益的正态（高斯）分布
最常被讨论的一个特征是收益的正态（高斯）分布。许多重要的金融模型都建立在股票收益正态分布的假设基础上，然而在本文结尾你将看到，这并不一定成立。因此，正态分布可以被认为是金融中最重要的分布之一，也是许多金融理论的主要统计基石之一。

让我们来看看调整后价格、百分比收益和自然对数收益的正态性。首先，我们定义一个函数从d1.describe（）中提取描述性统计信息。

```python
# 从describe()函数中提取所有统计信息。
def extract_data_stats(col):
    d_stat = col.describe()
    mu = d_stat['mean']
    sigma = d_stat['std']
    rtn_range = np.linspace(d_stat['min'], d_stat['max'], num=1000)
    norm_pdf = scs.norm.pdf(rtn_range, loc=mu, scale=sigma)
    
    return mu, sigma, rtn_range, norm_pdf


# 有了均值、标准差和正态概率密度函数（PDF），我们就可以绘制直方图和PDF。

# 绘制带有概率密度函数的直方图。
def draw_hist(col, xlim=(-0.2, 0.2)):
    mu, sigma, rtn_range, norm_pdf = extract_data_stats(col)
    sns.distplot(col, kde=True, norm_hist=True, label='Hist')   
    plt.plot(rtn_range, norm_pdf, 'r', lw=3, 
             label=f'N({mu:.3f}, {sigma**2:.4f})')
    plt.axvline(x=0, c='c',linestyle='--', lw=3)
    plt.title(f'Distribution of {col.name}', fontsize=24)
    plt.xlim(xlim)
    plt.legend(loc='upper right', fontsize=20, 
               frameon=True,fancybox=True, 
               framealpha=1, shadow=True, borderpad=1);

# 百分比回报的直方图和概率密度函数（PDF）: 下图1
draw_hist(d1.simple_rtn)

# 自然对数回报的直方图和概率密度函数（PDF）: 下图2
draw_hist(d1.log_rtn)

# 调整后价格的直方图和概率密度函数（PDF）: 下图3
draw_hist(d1.adj_close,xlim=(-10,50))
```

![](/images/202303/python-for-finance-series/030.webp_640x370)
![](/images/202303/python-for-finance-series/031.webp_640x370)
![](/images/202303/python-for-finance-series/032.webp_640x370)

显然，股票价格存在趋势或周期，使其远离正态分布。而对数收益和百分比收益非常相似且接近于正态分布。但是正态性能够被检验吗？

如果您的图形看起来不同，这是我使用的matplotlib参数：
```python
plt.rcParams['figure.figsize'] = [16, 9]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 24
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['font.family'] = 'serif'
```

## 聚合高斯性
参考文献¹末尾有一个与正态性相关的笔调化事实，它说：
“4. 聚合高斯性：随着计算回报的时间尺度增加，它们的分布看起来越来越像正态分布。特别地，分布的形状在不同的时间尺度上不同。”

让我们看看这个说法是否成立。我们创建一个新的 DataFrame 来保存所有滞后的股价回报。