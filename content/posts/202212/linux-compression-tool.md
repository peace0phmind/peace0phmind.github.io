---
title: "Linux Compression Tool"
description: "linux-compression-tool"
keywords: "linux,compression,tool"

date: 2022-12-13T11:43:12+08:00
lastmod: 2022-12-13T11:43:12+08:00

author: peace0phmind
url: "posts/202212/linux-compression-tool"

draft: true

categories:
  - blog
tags:
  - linux
  - compression
  - tool
---

## ubuntu 22.04默认安装

### Zstandard
[Zstandard](https://facebook.github.io/zstd/): Zstandard是一种快速压缩算法，可提供高压缩比。它还为小数据提供了一种特殊模式，称为字典压缩。
参考库提供了非常广泛的速度/压缩权衡，并由极快的解码器支持）。Zstandard库作为开源软件使用BSD许可证提供。其格式稳定并作为IETF RFC 8878发布。

### Gzip
[Gzip](https://www.gzip.org/):  gzip 是一种单文件/流无损数据压缩实用程序，其中生成的压缩文件通常具有后缀 .gz。
gzip还指该实用程序使用的相关压缩数据格式。

### bzip2
[bzip2](https://www.sourceware.org/bzip2/): 是免费提供的、无专利（见下文）的高质量数据压缩器。它通常将文件压缩到最佳可用技术（PPM 统计压缩器系列）的 10% 到 15% 以内，同时压缩速度大约是其两倍，解压缩速度大约是其六倍。

### p7zip
[p7zip](https://sourceforge.net/projects/p7zip/): p7zip 是用于 Unix 的 7z.exe 和 7za.exe（7zip 的命令行版本，请参阅 www.7-zip.org）的快速移植。
7-Zip 是具有最高压缩比的文件归档器。

### pigz
[pigz](https://zlib.net/pigz/): 是gzip的并行实现，是gzip的全功能替代品，它在压缩数据时充分利用多个处理器和多个内核。 

tar with pigz
```bash
# uncompress
tar -I pigz -xf <filename.tar.gz>
# compress
tar -I pigz -cf <filename.tar.gz> <dir or file>
# compress with options
tar cf - <paths-to-archive> | pigz -9 -p 32 > <archive.tar.gz>
```

### XZ Utils
[XZ Utils](https://tukaani.org/xz/): XZ Utils 是一款免费的通用数据压缩软件，具有高压缩比。 XZ Utils 是为类 POSIX 系统编写的，但也适用于一些不太 POSIX 的系统。
XZ Utils 是 LZMA Utils 的继承者。

## ubuntu 22.04未默认安装

### LZ4
[lz4](https://github.com/lz4/lz4): LZ4 是无损压缩算法，提供每核 > 500 MB/s 的压缩速度，可通过多核 CPU 进行扩展。它具有极快的解码器，每个内核的速度可达数 GB/s，通常在多核系统上达到 RAM 速度限制。

### lzop
[lzop](https://www.lzop.org/): 是一种强大的压缩工具，它使用 Lempel-Ziv-Oberhumer (LZO) 压缩算法。它通过交易压缩比提供极快的压缩速度。
例如，与gzip相比，它生成的文件稍大，但只需要10%的CPU运行时间。此外，lzop可以通过多种方式处理系统备份，包括备份模式、单文件模式、存档模式和管道模式。

### pixz
[pixz](https://github.com/vasi/pixz): 是XZ压缩器的并行实现，支持数据索引。它不是生成像xz这样的一大块压缩数据，而是创建一组较小的块。
这使得随机访问原始数据变得简单明了。此外，pixz 还确保文件权限在压缩和解压缩期间保持原样。

### plzip
[plzip](https://www.nongnu.org/lzip/plzip.html): 是一种无损数据压缩工具，它创造性地利用了现代 CPU 支持的多线程功能。它建立在 lzlib 库之上，提供类似于 gzip 和 bzip2 的命令行界面。 plzip 的一个主要优点是它能够充分利用多处理器机器。对于需要高性能 Linux 压缩工具来支持并行压缩的管理员来说，plzip 绝对值得一试。

## Reference
[10 Best Compression Tools for Linux](https://www.maketecheasier.com/best-compression-tools-linux/)
