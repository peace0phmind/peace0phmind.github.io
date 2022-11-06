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

## newline, space, align and tag
- new line use `\cr` or `\\\\`
- space use `\\,`, `\quad`
- align use `\begin{align}`, `\end{align}` and `&`
- tag use `\tag{1}`, or [use ams automatic](https://github.com/mathjax/MathJax-demos-web/blob/master/equation-numbers.html), [equation-numbers](https://mathjax.github.io/MathJax-demos-web/equation-numbers.html)
- tag with ams automatic, will omit by `\notag` or block symbol end with `*`, for example: `\begin{align*}`, `\end{align*}` 
- `use \begin{align} and \end{align} instead of $$ or $`

```text
\begin{align}
x&=y           &  w &=z              &  a&=b+c \\\\
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b \notag \cr
-4 + 5x&=2+y   &  w+2&=-1+w          &  a \quad b&=c\\,b\tag{xyz}
\end{align}
```

\begin{align}
x&=y           &  w &=z              &  a&=b+c \\\\
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b \notag \cr
-4 + 5x&=2+y   &  w+2&=-1+w          &  a \quad b&=c\\,b\tag{xyz}
\end{align}

```text
\begin{align*}
x&=y           &  w &=z              &  a&=b+c \\\\
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b \notag \cr
-4 + 5x&=2+y   &  w+2&=-1+w          &  a \quad b&=c\\,b\tag{xyz}
\end{align*}
```

\begin{align*}
x&=y           &  w &=z              &  a&=b+c \\\\
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b \notag \cr
-4 + 5x&=2+y   &  w+2&=-1+w          &  a \quad b&=c\\,b\tag{xyz}
\end{align*}

## block symbol: equation, split, multline, gather, align

### equation
- equation can only include one equation
- or it will not render

```text
\begin{equation}
x=y         
\end{equation}
```
\begin{equation}
x=y 
\end{equation}

```text
\begin{equation}
x=y \cr y=b         
\end{equation}
```
\begin{equation}
x=y \cr y=b
\end{equation}

### split
- split can use with equation
- but the tag was only one
```text
\begin{equation}
\begin{split}
x=y \cr y=b
\end{split}       
\end{equation} 
```
\begin{equation}
\begin{split}
x=y \cr y=b
\end{split}       
\end{equation} 

### multline
- multline same as equation with split
- but with different align
```text
\begin{multline}
x=y \cr y=b
\end{multline} 
```
\begin{multline}
x=y \cr y=b
\end{multline} 

### gather
```text
\begin{gather}
x=y \cr y=b
\end{gather} 
```
\begin{gather}
x=y \cr y=b
\end{gather} 

### align
```text
\begin{align}
x=y \cr y=b
\end{align} 
```
\begin{align}
x=y \cr y=b
\end{align} 

## 参考
- [Classical ML Equations in LaTeX](https://blmoistawinde.github.io/ml_equations_latex/)
