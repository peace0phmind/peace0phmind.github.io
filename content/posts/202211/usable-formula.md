---
title: "有用的公式"
description: "usable-formula"
keywords: "formula"

date: 2022-11-04T23:29:09+08:00
lastmod: 2022-11-04T23:29:09+08:00

author: peace0phmind
url: "posts/202211/usable-formula"

draft: false
weight: 2

categories:
  - blog
tags:
  - formula

---

## Use $\Sigma$ in different mode
- sum mode [making-the-subscript-under-the-summation](https://tex.stackexchange.com/questions/218603/making-the-subscript-under-the-summation)
- use color [Using_colours_in_LaTeX](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX)

### inline math
```text
$\sum_{i=1}^{\infty}|x_i-y_i|$
```
$\sum_{i=1}^{\infty}|x_i-y_i|$

### display math
```text
$$
\sum_{i=1}^{\infty}|x_i-y_i|
$$
```
$$
\sum_{i=1}^{\infty}|x_i-y_i|
$$

### use \limits
```text
$\sum\limits_{i=1}^{\infty}|x_i-y_i|$
```
$\sum\limits_{i=1}^{\infty}|x_i-y_i|$

## use color
```text
${\color{red}\eta}\frac{{\delta}L}{{\delta}W}|_{w=w^0}$
```
${\color{red}\eta}\frac{{\delta}L}{{\delta}W}|_{w=w^0}$

## newline, space and align
- new line use `\cr`
- space use `\\,`
- align use `\begin{align}`, `\end{align}` and `&`
```text
$$
\begin{align}
x&=y           &  w &=z              &  a&=b+c \cr
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b \cr
-4 + 5x&=2+y   &  w+2&=-1+w          &  ab&=c\\,b
\end{align}
$$
```
$$
\begin{align}
x&=y           &  w &=z              &  a&=b+c \cr
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b \cr
-4 + 5\\,x&=2+y   &  w+2&=-1+w          &  ab&=c\\,b
\end{align}
$$



## 参考
[Classical ML Equations in LaTeX](https://blmoistawinde.github.io/ml_equations_latex/)