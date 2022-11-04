---
title: "Mpv常用配置"
description: "mpv-config"
keywords: "mpv"

date: 2022-11-04T15:02:11+08:00
lastmod: 2022-11-04T15:02:11+08:00

author: peace0phmind
url: "posts/202211/mpv-config"

draft: true

categories:
  - blog
tags:
  - mpv

---

## 配置文件位置

系统范围的配置文件'mpv.conf'位于您的配置目录中（例如 /etc/mpv 或 /usr/local/etc/mpv）。
用户特定的文件是~/.config/mpv/mpv.conf。
有关详细信息和平台细节（特别是 Windows 路径），请参阅文件部分。

用户特定的选项会覆盖系统范围的选项，而命令行上给出的选项也会覆盖。配置文件的语法是 option=value。
#之后的所有内容都被视为注释。可以通过将它们设置为 yes 来启用没有值的选项，并通过将它们设置为 no 来禁用它们。

## Screenshot常用配置
```ini
screenshot-format="jpg"
screenshot-template="%F%n"
screenshot-directory="~/Pictures/mpv-shot"
screenshot-jpeg-quality=70
screenshot-png-compression=9
```

### screenshot-format

设置用于保存屏幕截图的图像文件类型。png, jpg(default), jpeg, webp, jxl

### screenshot-template

指定用于保存屏幕截图的文件名模板。模板指定没有文件扩展名的文件名，并且可以包含格式说明符，在截屏时将被替换。
默认情况下，模板是 mpv-shot%n，这会产生像mpv-shot0012.png这样的文件名。

模板可以以相对或绝对路径开头，以指定应保存屏幕截图的目录位置。

如果最终的屏幕截图文件名指向一个已经存在的文件，则该文件不会被覆盖。屏幕截图将不会被保存，或者如果模板包含%n，则使用不同的新生成的文件名保存。

- `%[#][0X]n`
一个序列号，用零填充到长度X（默认值：04）。例如。传递格式%04n将在第12个屏幕截图中产生0012。
每次截取屏幕截图或文件已存在时，该数字都会增加。长度X必须在0-9范围内。使用可选的#符号，mpv将使用最低的可用编号。
例如，如果您截取三张截图——0001、0002、0003——并删除前两张，那么接下来的两张截图将不再是0004和0005，而是再次成为0001和0002。

- `%f`
当前播放视频的文件名。

- `%F`
与 %f 相同，但去掉文件扩展名，包括点。

- `%x`
当前播放视频的目录路径。如果视频不在文件系统上（但例如 http://），则扩展为空字符串。

- `%X{fallback}`
与 %x 相同，但如果视频文件不在文件系统上，则返回 {...} 内的后备字符串。

- `%p`
当前播放时间，与 OSD 中使用的格式相同。结果是“HH:MM:SS”形式的字符串。例如，如果视频的时间位置为 5 分 34 秒，则 %p 将替换为“00:05:34”。

- `%P`
与 %p 类似，但以毫秒为单位延长播放时间。它的格式为“HH:MM:SS.mmm”，其中“mmm”是播放时间的毫秒部分。

- `%wX`
使用格式字符串 X 指定当前播放时间。%p 类似于 %wH:%wM:%wS，%P 类似于 %wH:%wM:%wS.%wT。

  有效的格式说明符:
  - `%wH` 小时（用 0 填充到两位数）
  - `%wh` 小时（无填充）
  - `%wM` 分钟 (00-59)
  - `%wm` 总分钟数（包括小时数，与 %wM 不同）
  - `%wS` 秒 (00-59)
  - `%ws` 总秒数（包括小时和分钟）
  - `%wf` 像 %ws，但返回的是浮点数
  - `%wT` 毫秒 (000-999)

- `%tX`
使用格式X指定当前本地日期/时间。此格式说明符在内部使用 UNIX strftime() 函数，并将传递“%X”的结果插入 strftime。
例如，%tm 将插入当前月份的数字作为数字。您必须使用多个 %tX 说明符来构建完整的日期/时间字符串。

- `%{prop[:fallback text]}`
插入输入属性“prop”的值。例如。 %{filename} 与 %f 相同。如果该属性不存在或不可用，则插入错误文本，除非指定了回退。

- `%%`
替换为 % 字符本身。

### screenshot-directory

将屏幕截图存储在此目录中。此路径与--screenshot-template生成的文件名相连。如果模板文件名已经是绝对的，则忽略该目录。

如果该目录不存在，则在第一个屏幕截图中创建该目录。如果不是目录，尝试写截图时会报错。

默认情况下未设置此选项，因此会将屏幕截图写入启动 mpv 的目录。在伪 gui 模式下, 它被设置为桌面。

### screenshot-png-compression=<0-9>

设置PNG压缩级别。更高意味着更好的压缩。这会影响截图文件大小和写截图的时间。过高的压缩可能会占用过多的CPU时间并中断播放。默认值为7。

### screenshot-jpeg-quality=<0-100>
设置 JPEG 质量级别。更高意味着更好的质量。默认值为 90。

## 参考
- [configuration-files](https://mpv.io/manual/master/#configuration-files)
- [screenshot](https://mpv.io/manual/master/#screenshot)