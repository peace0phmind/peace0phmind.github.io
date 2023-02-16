---
title: "Ubuntu as Switch"
description: "ubuntu-as-switch"
keywords: "ubuntu,as,switch"

date: 2023-02-16T16:38:11+08:00
lastmod: 2023-02-16T16:38:11+08:00

author: peace0phmind
url: "posts/202302/ubuntu-as-switch"

draft: false

categories:
  -
tags:
  - ubuntu
  - switch

---

## use netplan to config bridge
```bash
/etc/netplan
sudo nano 00-installer-config.yaml
```

```text
network:
  version: 2
  ethernets:
    enp2s0:
      dhcp4: no
    enp3s0:
      dhcp4: no
    enp4s0:
      dhcp4: no
    enp5s0:
      dhcp4: no
  bridges:
    br0:
      dhcp4: yes
      interfaces:
        - enp2s0
        - enp3s0
        - enp4s0
        - enp5s0
      parameters:
        stp: true
```

## config sysctl to disable ubuntu ethernet filtering
```bash
cd /etc
sudo nano sysctl.conf
```

```text
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
```

## add crontab to enable sysctl config
```bash
sudo crontab -e
```

```text
@reboot /bin/sleep 5 && /sbin/sysctl -p
```

## reboot to check
```bash
sudo reboot
```

## Reference
- [netplan: Configuring network bridges](https://netplan.io/examples#configuring-network-bridges)
- [Bridged Networking](https://wiki.libvirt.org/page/Networking#Bridged_networking_(aka_"shared_physical_device"))
- [No traffic gets trough (except ARP and STP)](https://wiki.linuxfoundation.org/networking/bridge#no_traffic_gets_trough_except_arp_and_stp)
- [Linux Bridge (brctl) not passing the traffic](https://unix.stackexchange.com/questions/544766/linux-bridge-brctl-not-passing-the-traffic)
- [Some sysctls are ignored on boot](https://bugs.launchpad.net/ubuntu/+source/procps/+bug/50093)
- [BridgeNetworkConnections](https://wiki.debian.org/BridgeNetworkConnections)