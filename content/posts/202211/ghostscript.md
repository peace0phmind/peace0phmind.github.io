---
title: "Using Ghostscript"
description: "ghostscript"
keywords: "ghostscript,pdf"

date: 2022-11-08T22:29:48+08:00
lastmod: 2022-11-08T22:29:48+08:00

author: peace0phmind
url: "posts/202211/ghostscript"

draft: true

categories:
  -
tags:
  - ghostscript
  - pdf

---

## Ghostscript介绍

Ghostscript 是 PostScript®和可移植文档格式(PDF)文件的解释器。

Ghostscript 由 PostScript解释器层和图形库组成。图形库与Ghostscript系列中的所有其他产品共享，因此所有这些技术有时都称为 Ghostscript，而不是更正确的 GhostPDL。

- `GhostPDF`: GhostPDF是PDF页面描述语言的解释器。
- `GhostPDL`: 我们使用 GhostPDL 作为一个总称来涵盖我们的整个产品线。现在，我们将所有这些不同的产品整合到一个包中，恰当地称为 GhostPDL。除了我们现有的 PDL 模块（PS、PDF、PCL、PXL 和 XPS）之外，我们现在还添加了新模块来处理一系列常见的图像格式。安装这些后，GhostPDL 将处理 JPEG（JFIF 和 EXIF）、PWG、TIFF、PNG、JBIG2 和 JPEG2000。
- `GhostPCL`: GhostPCL是PCL™和PXL文件的解释器。这包括一个连接到Ghostscript图形库的PCL/PXL解释器。
- `GhostXPS`: GhostXPS是XPS（XML Paper Specfication）文件的解释器。这包括一个连接到Ghostscript图形库的XPS解释器。
- `URW Font Information`: urwfonts 目录中的一组truetype字体是PCL/XL解释器正常运行所必需的，但它们不是免费软件，也不是在GNU GPL/AGPL下分发的。相反，它们可以根据禁止商业用途的AFPL许可证重新分发。

## Convert PDF to Images
这里使用该[input.pdf](https://speech.ee.ntu.edu.tw/~tlkagk/courses/ML_2016/Lecture/Logistic%20Regression%20(v3).pdf)文件作为转换研究。测试时，现将该文件保存为input.pdf。

### 常用参数与含义
- `-dBATCH`: 在处理完所有在命令行中命名的文件后退出，而不是进入读取 PostScript 命令的交互式循环。相当于将-c quit放在命令行末尾。
- `-dNOPAUSE`: 禁用提示和每页末尾的暂停。可以理解为连续打印或连续转换文件，不会在每页渲染完毕后有命令行提示出现。
- `-sDEVICE=`: 对应不同的输出类型，可以是打印机，文件类型等
- `-sOutputFile=`: 输出文件参数。可以使用`%d`或`%03d`作为文件模板的一部分，Ghostscript将用页码替换该部分。但请注意，并非所有设备都支持该模板。此外，由于某些设备在打开时会写入输出文件，因此可能会写入额外的空白页（pdfwrite、ps2write、eps2write、pxlmono、pxlcolor）
- `-o`: 作为输出文件的一种简写。使用该参数时，会自动设置-dBATCH和-dNOPAUSE选项。
- `-r`: 可以使用`-rXRESxYRES`或`-rres`的格式设置输出的大小。单位： dots (or pixels) per inch
- `-sPAPERSIZE=`: Ghostscript默认使用美国信纸作为其页面大小。可以使用例如`-sPAPERSIZE=a4`的设置进行页面大小的调整。如果不使用这个参数，则使用下面两个参数：
  - `-dDEVICEWIDTHPOINTS=`: 宽度
  - `-dDEVICEHEIGHTPOINTS=`: 高度
  - `-dFIXEDMEDIA`: 系统默认使用`-sPAPERSIZE=`设置页面大小，如果要启用宽度和高度设置，则需要包含该开关项。
- `-sPageList=`: 页面范围用逗号“,”分隔。每个页面范围可以包括：
  - 单个页码。例如： -sPageList=1,3,5 ；表示只处理1,3,5页
  - 起始页码-结束页码。例如： -sPageList=5-10 ；表示从第5页开始，处理到第10页。
  - 起始页码-。例如：-sPageList=12- ；表示从第12页开始，一直处理到最后一页。

### Convert PDF to png
- `-sDEVICE=png16m`: 8-bit/color RGB
- `-sDEVICE=pnggray`: 8-bit grayscale

```bash
gs -sDEVICE=png16m -sPageList=4 -o png-01.%03d.png input.pdf
gs -sDEVICE=pnggray -sPageList=4 -o png-02.%03d.png input.pdf
gs -sDEVICE=png16m -sPageList=4 -dDEVICEWIDTHPOINTS=960 -dDEVICEHEIGHTPOINTS=720 -dFIXEDMEDIA -o png-03.%03d.png input.pdf
gs -sDEVICE=pnggray -sPageList=4 -dDEVICEWIDTHPOINTS=960 -dDEVICEHEIGHTPOINTS=720 -dFIXEDMEDIA -o png-04.%03d.png input.pdf
gs -sDEVICE=png16m -sPageList=4 -r96 -o png-05.%03d.png input.pdf
gs -sDEVICE=pnggray -sPageList=4 -r96 -o png-06.%03d.png input.pdf
```

### Convert PDF to jpeg
- `-sDEVICE=jpeg`: JFIF standard 1.01

```bash
gs -sDEVICE=jpeg -sPageList=4 -o jpg-01.%03d.jpg input.pdf
gs -sDEVICE=jpeg -sPageList=4 -dDEVICEWIDTHPOINTS=960 -dDEVICEHEIGHTPOINTS=720 -dFIXEDMEDIA -o jpg-02.%03d.jpg input.pdf
gs -sDEVICE=jpeg -sPageList=4 -r96 -o jpg-03.%03d.jpg input.pdf
```

## Show PDF
- `-dBATCH`: 在处理完所有在命令行中命名的文件后退出，而不是进入读取 PostScript 命令的交互式循环。相当于将-c quit放在命令行末尾。

```bash
gs -dBATCH input.pdf
```


## Reference
[ghostscript reference](https://ghostscript.readthedocs.io/en/latest/Use.html)