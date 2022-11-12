---
title: "数据采集套件组装"
description: "data-acquisition-kit-assembly"
keywords: ""

date: 2022-11-10T09:09:34+08:00
lastmod: 2022-11-10T09:09:34+08:00

author: peace0phmind
url: "posts/202211/data-acquisition-kit-assembly"

draft: true

categories:
  -
tags:
  -

---

本文主要说明1个Dim槽满配30路电流传感器的材料准备、零部件检查与调整、零部件组装、部件之间的装配到最后验收测试的整个过程。最后顺带介绍下辅助工具。
## 名词解释
- `材料`: 材料为直接从供应商处采购，无法直接用于装配，需要二次加工的原材料。材料编号统一大写C加下标数字编号$Cn$。
- `配件`: 配件为从供应商处采购，通过简单的安装(或组装)即可正常使用的部件。配件编号统一大写P加下标数字编号$Pn$。
- `零件`: 从材料通过加工得到的部件，零件有其自己独立的编号体系。

## 材料和配件清单

| 图片 | 材料名称 | 编号 | 数量 | 用途 |
|--|--|--|--|--|
| ![](/images/202211/data-acquisition-kit-assembly/C1.jpg_160x120) | 红色电线 | $C_1$ | 200cm | 用于变送器和采集器的电源 |
| ![](/images/202211/data-acquisition-kit-assembly/C2.jpg_160x120) | 黑色电线 | $C_2$ | 200cm | 用于变送器和采集器的电源 |
| ![](/images/202211/data-acquisition-kit-assembly/C3.jpg_160x120) | 4色信号线缆  | $C_3$ | 540cm | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C4.jpg_160x120) | 3色电源线缆  | $C_4$ | 2m | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/C5.jpg_160x120) | 端子台线缆  | $C_5$ | 1根 | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/C11.jpg_160x120) | 红色接线端子E0306 | $C_{11}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C12.jpg_160x120) | 黄色接线端子E0306 | $C_{12}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C13.jpg_160x120) | 绿色接线端子E0306 | $C_{13}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C14.jpg_160x120) | 黑色接线端子E0306 | $C_{14}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C15.jpg_160x120) | 红色接线端子TE0508 | $C_{15}$ | 1个 | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/C16.jpg_160x120) | 黑色接线端子TE0508 | $C_{16}$ | 1个 | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/P1.jpg_160x120) | 220V转24VDC电源 | $P_{1}$ | 1个 | 电源 |
| ![](/images/202211/data-acquisition-kit-assembly/P2.jpg_160x120) | 数字采集器端子台 | $P_{2}$ | 1个 | 端子台 |
| ![](/images/202211/data-acquisition-kit-assembly/P3.jpg_160x120) | RJ45双端子台 | $P_{3}$ | 2个 | RJ45双端子台 |
| ![](/images/202211/data-acquisition-kit-assembly/P4.jpg_160x120) | RJ45单端子台 | $P_{4}$ | 1个 | RJ45单端子台 |
| ![](/images/202211/data-acquisition-kit-assembly/P5.jpg_160x120) | 3路变送器 | $P_{5}$ | 10个 | 3路变送器 |
| ![](/images/202211/data-acquisition-kit-assembly/P6.jpg_160x120) | 机柜用Dim槽 | $P_{6}$ | 1个 | 机柜用Dim槽 |
| ![](/images/202211/data-acquisition-kit-assembly/P7.jpg_160x120) | Dim槽 | $P_{7}$ | 1根 | Dim槽 |
| ![](/images/202211/data-acquisition-kit-assembly/P8.jpg_160x120) | Dim槽端子 | $P_{8}$ | 1根 | Dim槽端子 |
| ![](/images/202211/data-acquisition-kit-assembly/P9.jpg_160x120) | 三项交流电流传感器 | $P_{9}$ | 10组 | 1组3个，分别是红、黄、绿线 |
| ![](/images/202211/data-acquisition-kit-assembly/P10.jpg_160x120) | RJ45端子 | $P_{10}$ | 5个 | 1组3个，分别是红、黄、绿线 |

## 配件确认

### 数字采集器端子台($P_2$)配件确认与调整
- 如图示方向为端子台正确安装方向
- 4排编号如下表格所示
- 请确保贴纸与PCB板上丝印与表格顺序一致
- 如发现丝印错误请联系厂商，如发现贴纸顺序错误则可以将贴纸撕下再按正确顺序粘帖


|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|
|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|
|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|17|
|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|

{{< group >}}
![DC_1](/images/202211/data-acquisition-kit-assembly/P2.jpg "俯视图")
![DC_1](/images/202211/data-acquisition-kit-assembly/P2_1.jpg "黄色标签")
{{</ group >}}


## 零件加工

### 接线端子的安装方法

{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/DC_1.jpg "剥离线缆最外层绝缘层")
![](/images/202211/data-acquisition-kit-assembly/DC_2.jpg "继续剥离各电线自身绝缘层，让铜线裸露约1cm左右")
![](/images/202211/data-acquisition-kit-assembly/DC_3.jpg "找到对应颜色的接线端子")
![](/images/202211/data-acquisition-kit-assembly/DC_4.jpg "将裸露的铜线完全插入接线端子，使铜线头从端子顶端露出")
![](/images/202211/data-acquisition-kit-assembly/DC_5.jpg "使用打线钳将接线端子与铜线进行固定")
![](/images/202211/data-acquisition-kit-assembly/DC_6.jpg "使用剪线钳将多余的露出端子头的裸露铜线减除")
{{</ group >}}

### 端子台检查

### 

## 零部件组装


### 变送器电源线组装

#### 线缆裁剪要求
将90cm的红黑两色电线裁剪成如下尺寸和数量的电线。

| 材料名称 | 材料编号 | 长度(cm) | 数量 | 
|--|--|:--:|:--:|
| 红色电线 | $L_{6}^{red}$ | 6 | 9 |
| 黑色电线 | $L_{6}^{black}$ | 6 | 9 |
| 红色电线 | $L_{36}^{red}$ | 36 | 1 |
| 黑色电线 | $L_{36}^{black}$ | 36 | 1 |

#### 组装方式


#### 成品图片


### 变送器信号线
实际需要532cm，需要将

| 材料编号 | 长度(cm) | 数量 | 
|--|:--:|:--:|
| $SL_{16}$ | 16 | 10 |
| $SL_{24}$ | 24 | 1 |
| $SL_{30}$ | 30 | 2 |
| $SL_{36}$ | 36 | 3 |
| $SL_{42}$ | 42 | 2 |
| $SL_{48}$ | 48 | 2 |


### 接线顺序
#### 变送器顺序与线材表
- 从左向右数，1-10的变送器
- 数字下方为对应编号变送器的线材标号


|   |   |   |   |   |   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| $SL_{30}$ | $SL_{30}$ | $SL_{36}$ | $SL_{36}$ | $SL_{24}$ | $SL_{42}$ | $SL_{42}$ | $SL_{48}$ | $SL_{48}$ | $SL_{36}$ |

#### 端子台接线表：
- 数字表示端子台丝印上的编号。
- 数字的右下角数字表示对应的[变送器的编号](#变送器顺序与线材表)，如表可知对应编号所用线材标号。
- 数字自身的颜色以及右上角角标的颜色表示链接对应颜色的线缆。


|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|52|$\color{black}53_4^黑$|$\color{green}54_4^绿$|$\color{Goldenrod}55_4^黄$|$\color{red}56_4^红$|$\color{black}57_3^黑$|$\color{green}58_3^绿$|$\color{Goldenrod}59_3^黄$|$\color{red}60_3^红$|$\color{black}61_2^黑$|$\color{green}62_2^绿$|$\color{Goldenrod}63_2^黄$|$\color{red}64_2^红$|$\color{black}65_1^黑$|$\color{green}66_1^绿$|$\color{Goldenrod}67_1^黄$|$\color{red}68_1^红$|
|$\color{black}18_9^黑$|$\color{green}19_9^绿$|$\color{Goldenrod}20_9^黄$|$\color{red}21_9^红$|$\color{black}22_8^黑$|$\color{green}23_8^绿$|$\color{Goldenrod}24_8^黄$|$\color{red}25_8^红$|$\color{black}26_7^黑$|$\color{green}27_7^绿$|$\color{Goldenrod}28_7^黄$|$\color{red}29_7^红$|$\color{black}30_6^黑$|$\color{green}31_6^绿$|$\color{Goldenrod}32_6^黄$|$\color{red}33_6^红$|34|
|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|$\color{green}13_{10}^绿$|$\color{black}14_{10}^黑$|$\color{Goldenrod}15_{10}^黄$|$\color{red}16_{10}^红$|17|
|35|36|37|38|39|40|41|42|43|44|45|46|47|$\color{green}48_5^绿$|$\color{black}49_5^黑$|$\color{Goldenrod}50_5^黄$|$\color{red}51_5^红$|

