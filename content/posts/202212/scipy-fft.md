---
title: "Scipy Fft"
description: "scipy-fft"
keywords: "scipy,fft"

date: 2022-12-20T09:53:03+08:00
lastmod: 2022-12-20T09:53:03+08:00

author: peace0phmind
url: "posts/202212/scipy-fft"

draft: true

categories:
  -
tags:
  - scipy
  - fft

---

傅里叶分析是一种将函数表示为周期分量之和并从这些分量中恢复信号的方法。当函数及其傅里叶变换都被离散化的对应物替换时，它被称为离散傅里叶变换(DFT)。
DFT已成为数值计算的中流砥柱，部分原因在于FFT。FFT称为快速傅立叶变换,它的计算速度非常快，它的计算结果同时又与DFT等价。

## 快速傅里叶变换(Fast Fourier transforms)

### 一维离散傅立叶变换(1-D discrete Fourier transforms)
长度为N的序列x[n]的长度为N的FFT y[k]定义为:
$$
y[k] = \sum_{n=0}^{N-1}e^{-2\pi j \frac{kn}{N}}x[n]
$$
逆变换定义如下:
$$
x[n] = \frac{1}{N}\sum_{k=0}^{N-1}e^{2\pi j\frac{kn}{N}}y[k]
$$

这些变换可以分别通过`fft`和`ifft`计算，如下例所示:

```python
from scipy.fft import fft, ifft
import numpy as np
from scipy.fft import fft, ifft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
yinv = ifft(y)
```

从FFT的定义可以看出:
$$
y[0] = \sum_{n=0}^{N-1}x[n]
$$

此例中：
```python
np.sum(x)
# output is : 4.5
```

对应于y[0]。当N为偶数时，元素$y[1] \dots y[\sfrac{N}{2}−1]$包含正频率项，元素$y[\sfrac{N}{2}] \dots y[N−1]$包含负频率项，按负频率递减的顺序排列。
当N为奇数时，元素$y[1]...y[\sfrac{N−1}{2}]$包含正频率项，元素$y[\sfrac{N+1}{2}] \dots y[N−1]$包含负频率项，按负频率递减的顺序排列。

如果序列x是实值，则正频率的y[n]值是负频率值y[n]的共轭（因为频谱是对称的）。通常，仅绘制对应于正频率的FFT。

该示例绘制了两个正弦之和的FFT。

```python
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

# 采样点数
N = 600
# 采样频率
t = 800.0
# 样本间距, 单位s
T = 1.0 / t
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]

plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
```

FFT输入信号固有地被截断。这种截断可以建模为无限信号与矩形窗函数的乘积。在频谱域中，这种乘法成为信号频谱与窗函数频谱的卷积，形式为$sin(x)/x$。
这种卷积是称为频谱泄漏的效应的原因（参见[WPW]）。使用专用窗函数对信号加窗有助于减少频谱泄漏。下面的示例使用scipy.signal中的`blackman`窗口并显示了窗口效果（为了说明目的，FFT的零分量已被截断）。

```python
from scipy.fft import fft, fftfreq
import numpy as np
from scipy.signal.windows import blackman
import matplotlib.pyplot as plt

# 采样点数
N = 600
# 采样频率
t = 800.0
# 样本间距, 单位s
T = 1.0 / t
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)

w = blackman(N)
ywf = fft(y*w)
xf = fftfreq(N, T)[:N//2]

plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), '-b')
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), '-r')
plt.legend(['FFT', 'FFT w. window'])
plt.grid()
plt.show()
```

如果序列x是复值，则频谱不再对称。为了简化FFT函数的使用，scipy提供了以下两个辅助函数。

函数`fftfreq`返回FFT采样频率点:
```python
from scipy.fft import fftfreq
freq = fftfreq(8, 0.125)
freq
```

本着类似的精神，函数fftshift允许交换矢量的下半部分和上半部分，使其适合显示。
```python
from scipy.fft import fftshift
import numpy as np
x = np.arange(8)
fftshift(x)
```

下面的示例绘制了两个复指数的 FFT；注意不对称光谱。

```python
from scipy.fft import fft, fftfreq, fftshift
import numpy as np

# number of signal points
N = 400
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.exp(50.0 * 1.j * 2.0*np.pi*x) + 0.5*np.exp(-80.0 * 1.j * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)
import matplotlib.pyplot as plt
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()
```

函数`rfft`计算实数序列的FFT，并输出仅一半频率范围的复数FFT系数y[n]。对于实数输入(y[n]=conj(y[-n]))，FFT的厄米特对称性暗示了剩余的负频率分量。
如果N为偶数：[Re(y[0])+0j,y[1],...,Re(y[N/2])+0j]；如果N为奇数[Re(y[0])+0j,y[1],...,y[N/2]。
明确显示为Re(y[k])+0j的项被限制为纯实数，因为根据埃尔米特性质，它们是它们自己的复共轭。

相应的函数`irfft`计算具有这种特殊排序的FFT系数的IFFT。
```python
from scipy.fft import fft, rfft, irfft
import numpy as np
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5, 1.0])
fft(x)
yr = rfft(x)
yr
irfft(yr)
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
fft(x)
yr = rfft(x)
yr
```

请注意，奇数和偶数长度信号的`rfft`具有相同的形状。默认情况下，`irfft`假定输出信号的长度应该是偶数。因此，对于奇数信号，它会给出错误的结果：
```python
irfft(yr)
```

要恢复原始的奇数长度信号，我们必须通过n参数传递输出形状
```python
irfft(yr, n=len(x))
```

### 2维和N维离散傅立叶变换(2- and N-D discrete Fourier transforms)

函数`fft2`和`ifft2`分别提供二维FFT和IFFT。同样，`fftn`和`ifftn`分别提供N维FFT和IFFT。

对于实数输入信号，类似于`rfft`，我们有函数`rfft2`和`irfft2`用于二维实数变换；`rfftn`和`irfftn`用于N维实变换。

下面的示例演示了2维IFFT并绘制了生成的2维时域信号。

```python
from scipy.fft import ifftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

N = 30
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N,N))
xf[0, 5] = 1
xf[0, N-5] = 1
Z = ifftn(xf)
ax1.imshow(xf, cmap=cm.Reds)
ax4.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 0] = 1
xf[N-5, 0] = 1
Z = ifftn(xf)
ax2.imshow(xf, cmap=cm.Reds)
ax5.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 10] = 1
xf[N-5, N-10] = 1
Z = ifftn(xf)
ax3.imshow(xf, cmap=cm.Reds)
ax6.imshow(np.real(Z), cmap=cm.gray)
plt.show()
```

## Reference

- [fft-tutorial](https://docs.scipy.org/doc/scipy/tutorial/fft.html#)
- [fft-reference](https://docs.scipy.org/doc/scipy/reference/fft.html)
