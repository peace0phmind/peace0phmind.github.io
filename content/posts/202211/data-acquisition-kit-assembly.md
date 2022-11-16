---
title: "数据采集套件组装"
description: "data-acquisition-kit-assembly"
keywords: ""

date: 2022-11-10T09:09:34+08:00
lastmod: 2022-11-15T19:08:00+08:00

author: peace0phmind
url: "posts/202211/data-acquisition-kit-assembly"

draft: false

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
| ![](/images/202211/data-acquisition-kit-assembly/C11.jpg_160x120) | 红色接线端子E0306 | $C_{11}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C12.jpg_160x120) | 黄色接线端子E0306 | $C_{12}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C13.jpg_160x120) | 绿色接线端子E0306 | $C_{13}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C14.jpg_160x120) | 黑色接线端子E0306 | $C_{14}$ | 40个 | 用于变送器信号线 |
| ![](/images/202211/data-acquisition-kit-assembly/C15.jpg_160x120) | 红色接线端子TE0508 | $C_{15}$ | 1个 | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/C16.jpg_160x120) | 黑色接线端子TE0508 | $C_{16}$ | 1个 | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/C17.jpg_160x120) | 红色接线端子E0508 | $C_{17}$ | 1个 | 用于电源线 |
| ![](/images/202211/data-acquisition-kit-assembly/C18.jpg_160x120) | 黑色接线端子E0508 | $C_{18}$ | 1个 | 用于电源线 |
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
| ![](/images/202211/data-acquisition-kit-assembly/C5.jpg_160x120) | 端子台线缆  | $P_{11}$ | 1根 | 用于电源线 |

## 配件确认
### 数字采集器端子台($P_2$)配件确认与调整
- 如图示方向为端子台正确安装方向
- 4排编号如下表格所示
- 请确保贴纸与PCB板上丝印与表格顺序一致
- 如发现丝印错误请联系厂商，如发现贴纸顺序错误则可以将贴纸撕下再按正确顺序粘帖

#### $P_2$正面与侧面图
{{< group layout="2" indexShape="corner" >}}
![DC_1](/images/202211/data-acquisition-kit-assembly/P2.jpg "俯视图")
![DC_1](/images/202211/data-acquisition-kit-assembly/P2_1.jpg "黄色标签")
{{</ group >}}

#### $P_2$丝印编号表
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|
|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|
|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|17|
|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|

### RJ45端子台$P_3(或P_4)$配件确认与调整
#### $P_3(或P_4)$错误与正确方向图，以及调整方式
- 将$P_3(或P_4)$侧面放置，螺丝左侧有凹槽的为上端(如图1或3左上)，螺丝左侧有突起的为下端(如图1或3左下)
- 将端子台按正确方向放置并检查，RJ45口在上端的为错误，RJ45口在下端的为正确
- 调整方式见图2,将一侧螺丝卸下，将pcb板调整方向，最后将螺丝和边盖重新装配上
- $P_4$的侧面图与$P_3$类似，调整方式一致

{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P3_1.jpg "错误的侧面")
![](/images/202211/data-acquisition-kit-assembly/P3_2.jpg "调整方式")
![](/images/202211/data-acquisition-kit-assembly/P3_3.jpg "正确的侧面")
{{</ group >}}

#### $P_3(或P_4)$正确线序
- 按图1所示方向放置$P_3(或P_4)$
- 如图2,端子顺序按从上层到下层，从左侧向右侧数分别为：8,7,6,5; 4,3,2,1
- RJ45口从左侧向右侧数顺序为：8,7,6,5,4,3,2,1
- 请用万用表检测最左上的接线端子与RJ45最左侧的线是否联通来检测顺序是否正确

{{< group layout="2" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P3.jpg "正面图")
![](/images/202211/data-acquisition-kit-assembly/P3_4.jpg "接线顺序图")
{{</ group >}}

### RJ45端子($P_{10}$)线序确认
- 如图1和图2所示，从左向右数，端子与RJ45的线序为: 8,7,6,5,4,3,2,1
- 请用万用表检测最左侧的接线端子与RJ45最左侧的线是否联通来检测顺序是否正确

{{< group layout="2" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P10.jpg "正面")
![](/images/202211/data-acquisition-kit-assembly/P10_1.jpg "正面俯看图")
{{</ group >}}

## 零件加工
### 电源线加工与安装(接线端子的详细安装步骤为图1-5)
{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/DC_2.jpg "材料($C_4$)：剥离各电线自身绝缘层，让铜线裸露约1cm左右")
![](/images/202211/data-acquisition-kit-assembly/DC_3.jpg "材料($C_{15}+2\times C_{16}$)：找到对应颜色的接线端子")
![](/images/202211/data-acquisition-kit-assembly/DC_4.jpg "将裸露的铜线完全插入接线端子，使铜线头从端子顶端露出")
![](/images/202211/data-acquisition-kit-assembly/DC_5.jpg "使用打线钳将接线端子与铜线进行固定")
![](/images/202211/data-acquisition-kit-assembly/DC_6.jpg "使用剪线钳将多余的露出端子头的裸露铜线减除")
![](/images/202211/data-acquisition-kit-assembly/DC_7.jpg "将电线按如图所示链接到电源($P_1$)上")
{{</ group >}}

### Dim槽裁剪
- 从$P_7$的原材料上，截取10个孔的Dim槽(见图2)，零件编号$D_{10}$
- 裁剪时，从$P_7$的左侧开始数10个孔，在10和11孔中间使用锯子将零件截取下来

{{< group layout="2" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P7.jpg "材料($P_7$)")
![](/images/202211/data-acquisition-kit-assembly/P7_1.jpg "加工得到零件$D_{10}$")
{{</ group >}}

### 变送器电源线线缆裁剪与加工
#### 变送器电源线线缆裁剪
将90cm的红黑两色电线裁剪成如下尺寸和数量。

| 材料名称 | 长度(cm) | 数量 |
|--|:-:|:-:|
| 红色电线($C_1$) | 6 | 9 |
| 黑色电线($C_2$) | 6 | 9 |
| 红色电线($C_1$) | 36 | 1 |
| 黑色电线($C_2$) | 36 | 1 |

#### 变送器电源线线缆加工
{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/L_1.jpg "材料($C_1, C_2$)：裁剪后材料图")
![](/images/202211/data-acquisition-kit-assembly/L_2.jpg "调整剥线钳限位器到1/2")
![](/images/202211/data-acquisition-kit-assembly/L_3.jpg "电线顶住位置器进行剥线")
![](/images/202211/data-acquisition-kit-assembly/L_4.jpg "所有电线两头剥除绝缘层")
![](/images/202211/data-acquisition-kit-assembly/L_5.jpg "两端使用E0508，中间使用TE0508")
![](/images/202211/data-acquisition-kit-assembly/L_6.jpg "零件成品，黑色零件与红色一致")
{{</ group >}}

### 变送器信号线
#### 变送器信号线裁剪
需要将540cm(实际需要532cm)4芯信号线($C_3$)裁剪成如下尺寸和数量。

| 材料编号 | 长度(cm) | 数量 | 
|--|:--:|:--:|
| $SL_{16}$ | 16 | 10 |
| $SL_{24}$ | 24 | 1 |
| $SL_{30}$ | 30 | 2 |
| $SL_{36}$ | 36 | 3 |
| $SL_{42}$ | 42 | 2 |
| $SL_{48}$ | 48 | 2 |

#### 变送器信号线加工
{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/SL_1.jpg "材料($C_3$)：按尺寸要求裁剪信号线")
![](/images/202211/data-acquisition-kit-assembly/SL_2.jpg "调整剥线钳限位器到最大")
![](/images/202211/data-acquisition-kit-assembly/SL_3.jpg "将线缆头与限位器右外侧对齐并剥线")
![](/images/202211/data-acquisition-kit-assembly/SL_4.jpg "剥离外侧绝缘层的线缆")
![](/images/202211/data-acquisition-kit-assembly/SL_5.jpg "调整剥线钳限位器到1/2")
![](/images/202211/data-acquisition-kit-assembly/SL_6.jpg "将线缆头与限位器左内侧对齐并剥线")
![](/images/202211/data-acquisition-kit-assembly/SL_7.jpg "剥离内侧绝缘层的线缆")
![](/images/202211/data-acquisition-kit-assembly/SL_8.jpg "使用对应颜色E0306材料")
![](/images/202211/data-acquisition-kit-assembly/SL_9.jpg "使用夹线钳对材料进行加工")
{{</ group >}}

#### 变送器信号线阶段效果图
{{< group layout="2" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/SL_11.jpg "按照加工步骤1得到结果")
![](/images/202211/data-acquisition-kit-assembly/SL_13.jpg "完成所有步骤得到结果")
{{</ group >}}

## 部件装配
### 组装Dim槽
{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/D_1.jpg "配件($P_6$)：将Dim槽倒放，注意左右下脚的三角铁为下边")
![](/images/202211/data-acquisition-kit-assembly/D_2.jpg "零件($D_{10}$)：从左向右数，将2,3号螺丝卸下")
![](/images/202211/data-acquisition-kit-assembly/D_3.jpg "将$D_{10}$的3,8号孔与$P_6$的2,3号孔对齐")
![](/images/202211/data-acquisition-kit-assembly/D_4.jpg "拧入螺丝，将$D_{10}$固定在$P_6$上")
![](/images/202211/data-acquisition-kit-assembly/D_5.jpg "准备配件($2\times P_3 + P_4 + 2\times P_8$)")
![](/images/202211/data-acquisition-kit-assembly/D_6.jpg "将配件按如图位置安装")
![](/images/202211/data-acquisition-kit-assembly/D_7.jpg "翻转$P_6$，准备配件($P_2 + 10\times P_5 + P_1$)")
![](/images/202211/data-acquisition-kit-assembly/D_8.jpg "按顺序从左到右依次安装。注意$P_{5}$的1-6号口在上，7-12号口在下")
![](/images/202211/data-acquisition-kit-assembly/D_9.jpg "成品顶视图，注意背面$P_{3},P_{4}$按$P_{5}$居中")
{{</ group >}}

### RJ45端子台(RJ45双端子台$P_3或RJ45单端子台P_4$)到变送器($P_5$)信号线接线方式
#### 注意事项与接线方式
- 此处将一个$P_3$当作两个$P_4$，即此处一共有5个$P_4$ (见上图9成品顶视图)
- 按上图9成品顶视图从左向右进行编号
- 一个$P_4$加2个$P_5$组成一组。即：$(P_41, P_5[1,2]),(P_42, P_5[3,4]),\cdots,(P_45, P_5[9,10])$
- 下面表格接线按照一组配件($P4+2\times P_5$)进行说明
- 表格中左和右分别表示每组$P_5$中的左右$P_5$
- 文字下标数字表示$P_5$的接口编号
- 文字上标数字表示$P_4$的接口编号
- 文字颜色表示使用的$C3$线缆中的4种颜色
- 此处统一使用$SL_{16}$线缆进行连接
- 注：为了方便$P_4$线缆连接，建议先接5,6,7,8口，再接1,2,3,4口
- 注：为了方便$P_5$线缆连接，建议先接1,3口，再接4,6口

|   |   |   |   |
|:-:|:-:|:-:|:-:|
| $\color{red}左_6^1$ | $\color{Goldenrod}左_4^2$ | $\color{green}左_3^3$ | $\color{black}左_1^4$ | 
| $\color{red}右_6^5$ | $\color{Goldenrod}右_4^6$ | $\color{green}右_3^7$ | $\color{black}右_1^8$ |

#### 端口照片以及接线示例
{{< group layout="2" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P5i_1.jpg "$P_5$输入端口编号:1,2,3,4,5,6")
![](/images/202211/data-acquisition-kit-assembly/P5i_2.jpg "$P_5$对应接线图")
![](/images/202211/data-acquisition-kit-assembly/P5i_3.jpg "$P_4$端口编号:1,2,3,4,5,6,7,8")
![](/images/202211/data-acquisition-kit-assembly/P5i_4.jpg "$P_4$对应接线图")
![](/images/202211/data-acquisition-kit-assembly/P5i_5.jpg "总装效果图")
{{</ group >}}

### 数字采集器端子台($P_2$)到变送器($P_5$)接线方式
#### 变送器编号与线材表
- 按Dim槽装配图9顶视图从左向右对$P_5$编号1-10
- 表头上标为$P_5$的编号，内容为对应$P_5$编号所使用的线材编号

|   |   |   |   |   |   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $P_5^1$ | $P_5^2$ | $P_5^3$ | $P_5^4$ | $P_5^5$ | $P_5^6$ | $P_5^7$ | $P_5^8$ | $P_5^9$ | $P_5^{10}$ |
| $SL_{30}$ | $SL_{30}$ | $SL_{36}$ | $SL_{36}$ | $SL_{24}$ | $SL_{42}$ | $SL_{42}$ | $SL_{48}$ | $SL_{48}$ | $SL_{36}$ |

#### $P_5$输出接口接线方式
|   |   |   |
|:-:|--:|:-:|
|![](/images/202211/data-acquisition-kit-assembly/P5o_0.jpg_320x240)| 7: $\color{red}信号(红色)$  </br> 8: $\color{Goldenrod}信号(黄色)$  </br> 9: $\color{green}信号(绿色)$  </br> 10: $\color{black}信号(黑色)$  </br> 11: $\color{black}电源(黑色)$  </br> 12: $\color{red}电源(红色)$  | ![](/images/202211/data-acquisition-kit-assembly/P5o_01.jpg_320x240)|

#### $P_2$接线表
- 数字表示$P_2$丝印上的编号。
- 数字的下标数字表示对应的[$P_5$的编号](#变送器编号与线材表)，如上表可知对应[编号所用线材标号](#变送器编号与线材表)。
- 数字自身的颜色以及上标角标的颜色表示连接线对应的颜色。
- 具体接线效果见下图5效果

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|52|$\color{black}53_4^黑$|$\color{green}54_4^绿$|$\color{Goldenrod}55_4^黄$|$\color{red}56_4^红$|$\color{black}57_3^黑$|$\color{green}58_3^绿$|$\color{Goldenrod}59_3^黄$|$\color{red}60_3^红$|$\color{black}61_2^黑$|$\color{green}62_2^绿$|$\color{Goldenrod}63_2^黄$|$\color{red}64_2^红$|$\color{black}65_1^黑$|$\color{green}66_1^绿$|$\color{Goldenrod}67_1^黄$|$\color{red}68_1^红$|
|$\color{black}18_9^黑$|$\color{green}19_9^绿$|$\color{Goldenrod}20_9^黄$|$\color{red}21_9^红$|$\color{black}22_8^黑$|$\color{green}23_8^绿$|$\color{Goldenrod}24_8^黄$|$\color{red}25_8^红$|$\color{black}26_7^黑$|$\color{green}27_7^绿$|$\color{Goldenrod}28_7^黄$|$\color{red}29_7^红$|$\color{black}30_6^黑$|$\color{green}31_6^绿$|$\color{Goldenrod}32_6^黄$|$\color{red}33_6^红$|34|
|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|$\color{green}13_{10}^绿$|$\color{black}14_{10}^黑$|$\color{Goldenrod}15_{10}^黄$|$\color{red}16_{10}^红$|17|
|35|36|37|38|39|40|41|42|43|44|45|46|47|$\color{green}48_5^绿$|$\color{black}49_5^黑$|$\color{Goldenrod}50_5^黄$|$\color{red}51_5^红$|

#### 阶段图片示例
{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P5o_1.jpg "底视图")
![](/images/202211/data-acquisition-kit-assembly/P5o_2.jpg "先链接所有$P_5$的电源线")
![](/images/202211/data-acquisition-kit-assembly/P5o_3.jpg "电源线另一头连接到$P_1$")
![](/images/202211/data-acquisition-kit-assembly/P5o_4.jpg "根据《变送器编号与线材表》连接信号线到所有$P_5$")
![](/images/202211/data-acquisition-kit-assembly/P5o_5.jpg "再根据《$P_2$接线表》连接信号线到$P_2$")
![](/images/202211/data-acquisition-kit-assembly/P5o_6.jpg "注意$P_2$信号线在Dim槽上的走线")
{{</ group >}}

#### 阶段检测
- 使用万用表的检测功能检测$P_4$到$P_5$之间的接线顺序是否正确
- 使用万用表的检测功能检测$P_2$到$P_5$之间的接线顺序是否正确

### RJ45端子($P_{10}$)与电流传感器($P_9$)的组装
#### $P_{10}$到$P_9$的组装步骤
- 红、黄、绿三色传感器为一组，使用1个$P_9$表示。每$P_9$需使用TE0508与E0306对导线头重新处理，如图1-4
- 2个$P_9$加一个$P_{10}$为一个六轴机器人采集单元
- 下表中，表头上标为$P_{10}$的端口编号，按从左向右编号为8-1
- 表格内容中的数字为传感器组的编号，1即为第一组，2即为第二组
- 表格内容中的数字颜色与上标表示接线颜色，有下标为"负"的表示每组传感器共负极导线(即图2中，三色花线合并起来的线)

| $P_{10}^8$ | $P_{10}^7$ | $P_{10}^6$ | $P_{10}^5$ | $P_{10}^4$ | $P_{10}^3$ | $P_{10}^2$ | $P_{10}^1$ |
|--|--|--|--|--|--|--|--|
| $\color{black}2_负^黑$ | $\color{green}2^绿$ | $\color{Goldenrod}2^黄$ | $\color{red}2^红$ | $\color{black}1_负^黑$ | $\color{green}1^绿$ | $\color{Goldenrod}1^黄$ | $\color{red}1^红$ |

#### $P_{10}$RJ45端子与$P_9$电流传感器图例
{{< group layout="3" indexShape="corner" >}}
![](/images/202211/data-acquisition-kit-assembly/P9_1.jpg "红、黄、绿三色传感器一组为一个$P_9$")
![](/images/202211/data-acquisition-kit-assembly/P9_2.jpg "将每组的花色线使用剥线钳处理后，用打线钳加装TE0508组成共负极导线")
![](/images/202211/data-acquisition-kit-assembly/P9_3.jpg "三色纯色线用剥线钳处理后，用打线钳加装E0306")
![](/images/202211/data-acquisition-kit-assembly/P9_4.jpg "每组传感器装完端子后的效果图")
![](/images/202211/data-acquisition-kit-assembly/P9_5.jpg "$2\times P_9+P_{10}$为一个六轴机器人采集单元")
![](/images/202211/data-acquisition-kit-assembly/P9_6.jpg "按如图颜色和顺序固定$P_9和p_{10}$")
{{</ group >}}

## 数据采集套件组装完成
![](/images/202211/data-acquisition-kit-assembly/ALL.jpg "包括一个Dim槽(包括端子台、变送器和电源)+5个六轴机器人采集单元")