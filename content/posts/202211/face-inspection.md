---
title: "Face Inspection"
description: "face-inspection"
keywords: "face,inspection"

date: 2022-11-04T09:31:07+08:00
lastmod: 2022-11-04T09:31:07+08:00

author: peace0phmind
url: "posts/202211/face-inspection"

draft: true

categories:
  -
tags:
  -

---
## 用户开户注册流程

```mermaid
sequenceDiagram
  participant 客服质检系统
  participant 大华AI服务器
  客服质检系统->>大华AI服务器: 1.1 发起人脸注册
  大华AI服务器->>客服质检系统: 1.2 人脸注册成功
```

### 发起人脸注册
需大华AI文档明确

### 人脸注册成功
需大华AI文档明确

## 巡检流程

```mermaid
sequenceDiagram
  participant 亿嘉和机器人
  participant 客服质检系统
  participant 大华AI服务器
  亿嘉和机器人->>+客服质检系统: 2.1 人脸巡检请求
  客服质检系统->>+大华AI服务器: 2.3 人脸情绪识别
  大华AI服务器->>-客服质检系统: 2.4 人脸情绪结果
  客服质检系统->>-亿嘉和机器人: 2.2 人脸巡检结果
```

### 人脸巡检请求（待协商）
由亿嘉和机器人发起的对客服质检系统的基于**HTTP Post**的接口调用。
- **URL**: /api/face-inspection
- **Method**: POST
- **Body**: 参见下面json格式

```json
{
  "sn": "15e6dd99-7008-4d4d-8929-797a31c005fe", // 唯一序列号, 防止重复请求
  "seat": "2排201", // 工位信息，用于描述当前工位，长度不大于255; 或是一个全局唯一的id
  "temperature": 36.5, // 表示温度
  "image": "XXXXXX"  // base64编码的人脸图片 
}
```

### 人脸巡检结果（待协商）

```json
{
  "code": "0000", // 巡检成功返回0000, 失败返回其他数值
  "message": "成功" // 巡检成功返回”成功“，失败返回失败原因
}
```

### 人脸情绪识别
需大华AI文档明确

### 人脸情绪结果
需大华AI文档明确

