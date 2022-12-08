---
title: "Unified Auth"
description: "unified-auth"
keywords: "unified,auth"

date: 2022-12-07T10:25:03+08:00
lastmod: 2022-12-07T10:25:03+08:00

author: peace0phmind
url: "posts/202212/unified-auth"

draft: true

categories:
  - work
tags:
  - unified
  - auth

---

<center><h1>南京市统一身份认证项目</h1></center>

## 已经完成的工作

### 项目启动
- 和图慧沟通项目的背景、现状以及目标
- 从图慧获取文档，代码等
- 从平安获取环境初始化脚本等
- 从信息中心现网拷贝必要的文件
  - 研究现网云环境，找到需要支撑打包的文件
    - 被harbor托管的40个docker镜像
    - 被portainer托管的23个stack文件
    - 导出2个apollo运行需要的数据库文件
    
### 第一周
- 所有的JAVA工程可以打出jar包
  - 从13个docker镜像中导出业务jar包
  - 用golang开发了一个工具，匹配jar包和源码，将源码中不包含的jar，并且不是共有jar包的，上传到私有maven仓库
  - 用golang开发了另一个工具，匹配jar包、源码和maven仓库，将缺少代码的模块列举出来
  - 逐个修改13个工程的代码，确保使用docker中自带的jar包可以让工程编译通过
- 小程序工程编译成功
- ios工程编译成功
  - 检查了所有的pod依赖，保证库的完整性。
- android工程编译成功
  - 修改了打包使用的android studio版本，解决版本过低无法打包的问题
- 尝试对前端工程打包，需要smi和smi-cli，无法打包
- 将以上所有完成的代码修改后的工程，全部推送到图慧git仓库
- 在图慧提供的jenkins服务器上实现了CMS项目的jar包和docker包的打包工作

### 第二周
- 继续到信息中心现网寻找并复制必要的文件
  - 未被harbor托管的docker镜像
  - 线上Web服务和相关配置
  - wiki对应的docker容器
  - wiki对应的工程目录压缩包
  - 运行必要的线上服务器主机中的一些文件
    - auditbeat: /pasc/apm/auditbeat
    - elk/kafka[1-3]: /etc/hosts
    - elk/es[1-3]: /pasc/apm/es/conf
    - elk/es[1-3]: /data/apm/jar/x-pack-core-7.2.0.jar
    - elk/kibana: /pasc/apm/kibana/plugins
    - elk/kibana: /pasc/apm/kibana/conf/kibana.yml
    - elk/logstash: /pasc/apm/logstash/conf/pipeline/logstash.conf
    - elk/logstash: /pasc/apm/logstash/data
    - kafka/kafka[1-3]: /etc/hosts
    - kafka/kafka[1-3]: /pasc/apm/kafka
    - nginx/nginx-1: /pasc/nginx/nginx.conf
    - nginx/nginx-1: /pasc/nginx/conf.d
    - nginx/nginx-1: /pasc/nginx/web
    - nginx/nginx-1: /pasc/nginx/ssl
    - nginx/nginx-2: /pasc/nginx/nginx.conf
    - nginx/nginx-2: /pasc/nginx/conf.d
    - nginx/nginx-2: /pasc/nginx/web
    - nginx/nginx-2: /pasc/nginx/ssl
    - nginx/nginx-3: /pasc/nginx/nginx.conf
    - nginx/nginx-3: /pasc/nginx/conf.d
    - nginx/nginx-3: /pasc/nginx/web
    - nginx/nginx-3: /pasc/nginx/ssl
- 由于图慧环境遭到破坏，重新搭建本地分布式环境
  - jenkins环境搭建
  - nexus环境搭建
  - harbor环境搭建
  - 在本地环境中完成所有后端服务器的打包工作
- 使用5本地服务器，完成集群搭建
  - docker swarm集群设置
    - 1台PC-Server完成部署，作为swarm的manager
    - 4台高性能边缘计算单元的初始化,作为swarm集群的worker
  - portainer平台搭建
- 初步完成项目需要的周边配套环境的搭建
  - elk_es
  - elk_filebeat
  - elk_kibana
  - elk_logstash
  - apollo
  - eureka_server
  - kafka集群
  - mysql
  - rabbitmq
  - redis集群
  - zookeeper集群

### 第三周（本周正在进行）
- 完成剩余部件的搭建和配置工作(使用线上docker镜像通过修改配置文件完成启动)
  - app-front
  - cms-front
  - trust-front
  - web-front
  - nfs
  - nginx
  - service_adm
  - service_auth
  - service_cms
  - service_miniApp
  - service_opm
  - service_sds
  - service_ums
  - zag
- 进行简单的测试
  - 研读admin代码，找到登录用户名和密码，点击界面，没有明显的错误提示
  - 研读web api代码，进行简单的post测试，确保后端接口调用正常（只做简单的几个用例的测试）
- 使用jenkins流水线打包出来的docker image部署到测试环境
  - 此处略，参见上面列表
  - 进行必要的测试

## 后续工作（预计还需要2个月左右）
- 发现代码中调用到了一些外部接口（目前已知的是人脸和短信接口），为了能够在测试环境完成测试，处理方式如下二选一：
  - 找相关接口提供方提供外网测试接口，在系统中进行配置并使用
  - 开发必要的mock server，方便系统进行测试
- 结合现有代码和文档，以编写测试用例为手段，研读代码，对所有接口进行自动化测试脚本全覆盖
  - 初读代码即发现一些安全隐患，这块需要后续项目推进
  - 根据接口和对应代码，编写必要的集成测试用例，该用例需要可以能够集成到jenkins服务器中运行，并确保所有测试顺利通过
- 查漏补缺，可能还有一些周边配套运行环境未完成部署
  - 比如：告警服务器，grafana,告警服务器mysql等
- 线上系统运行情况调研，对需要进行运维的模块输出必要的运维文档
  - 进行线上系统运行情况调研，主要关注cpu,内存，磁盘，接口调用次数，接口调用平均响应时长等
  - 有针对性的输出必要的运维文档，比如：在拷贝文件时，无意间发现某台es服务器磁盘使用率在60%以上，需要观察其增长规律，在预计磁盘满80%前的提前3个月输出。

## 工作目标
- 最终做到对所有模块，全局掌控。包括：
  - 架构、代码、配置、组网、部署、云管理、运维、安全
  - 线上问题定位及修复能力
  - 具备二次开发及优化能力
