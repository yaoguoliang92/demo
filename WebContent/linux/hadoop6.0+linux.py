在/etc/sysconfig/network-scripts/ifcfg-eth0(确认ONBOOT=yes),其中eth0是设备名；
ONBOOT是指明在系统启动时是否激活网卡，只有在激活状态的网卡才能去连接网络，进行网络通讯。
DEVICE：网卡名称(一定是写eth0)
ONBOOT=yes(相当于启动这个网卡的开关，你要用eth0这个一定要yes，表示开)BOOTPROTO=none（这个是表示你使用什么样的路由协议，有三种不同写法，如果是none和static表示你用的是静态路由，那么你在接下来的项目里就必须填写IPADDR、NETMASK、GATEWAY这三个选项。如果是dhcp表示你使用动态路由协议，那IPADDR、NETMASK、GATEWAY这些选项就可以不必填写。如果填写了，就以你填写的值为准）
HWADDR：你网卡的物理地址（可以不用写，系统自动会生成）
IPADDR：ip地址  
NETMASK：子网掩码    
GATEWAY：网关
BOOTPROTO=static
这个是网络配置参数：
BOOTPROTO=static   静态IP
BOOTPROTO=dhcp   动态IP

改网络
vi /etc/sysconfig/network-scripts/ifcfg-ens33

#重启网络
restart network

ip addr#查看iP

#安装ifconfig命令
yum -y install net-tools

#安装vim
yum install vim -y


BOOTPROTO=static
IPADDR=192.168.19.20
NETMASK=255.255.255.0
GATEWAY=192.168.19.2	#在虚拟网络编辑器查看
DNS1=1.2.4.8
DNS2=210.2.4.8

#重启网络
systemctl restart network