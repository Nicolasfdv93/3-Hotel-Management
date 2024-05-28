

### SWITCHES ###

## All Switches ##

vlan 10
name IT
vlan 20
name Admin
vlan 30
name Sales
vlan 40
name HR
vlan 50
name Finances
vlan 60
name Logistics
vlan 70
name Store
Vlan 80
Name Reception
Vlan 99
name native

## F1-Switch ##

en
conf t
hostname F1-Switch

int ran fa0/2-3
switchport mode access
switchport access vlan 80
int ran fa0/4-5
switchport mode access
switchport access vlan 70
int ran fa0/6-8
switchport mode access
switchport access vlan 60
int gi0/1
switchport mode trunk
switchport trunk native vlan 99

exit
do wr

## F2-Switch ##

en
conf t
hostname F2-Switch

int ran fa0/2-3
switchport mode access
switchport access vlan 50
int ran fa0/4-5
switchport mode access
switchport access vlan 40
int ran fa0/6-8
switchport mode access
switchport access vlan 30
int gi0/1
switchport mode trunk
switchport trunk native vlan 99

exit
do wr

## F3-Switch ##

en
conf t
hostname F3-Switch

int ran fa0/2-3
switchport mode access
switchport access vlan 10
int ran fa0/4-6
switchport mode access
switchport access vlan 20
int gi 0/1
switchport mode trunk
switchport trunk native vlan 99

exit
do wr

//Port security only for TEST-PC to access to Port Fa 0/2

int fa0/2
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address sticky
switchport port-security violation shutdown
exit
do wr

### ROUTERS ###

// Remember configure clockrate on DCE ports which have
// the clock signal on the port

## F1-ROUTER ##

en
conf t
hostname F1-Router

int se0/2/0
no shut
int se0/2/1
no shut
int g0/0
no shut
int se0/2/0
ip address 10.10.10.5 255.255.255.252
int se0/2/1
ip address 10.10.10.9 255.255.255.252

exit

//Inter-VLAN and DHCP server configuration. 

int g0/0.80
encapsulation dot1q 80
ip address 192.168.8.1 255.255.255.0
exit

service dhcp
ip dhcp pool Reception
network 192.168.8.0 255.255.255.0
default-router 192.168.8.1
dns-server 192.168.8.1
exit

int g0/0.70
encapsulation dot1q 70
ip address 192.168.7.1 255.255.255.0
exit

ip dhcp pool Store
network 192.168.7.0 255.255.255.0
default-router 192.168.7.1
dns-server 192.168.7.1
exit

int g0/0.60
encapsulation dot1q 60
ip address 192.168.6.1 255.255.255.0
exit

ip dhcp pool Logistics
network 192.168.6.0 255.255.255.0
default-router 192.168.6.1
dns-server 192.168.6.1
exit
do wr

//OSPF Configuration 
router ospf 10
network 10.10.10.4 255.255.255.252 area 0
network 10.10.10.8 255.255.255.252 area 0
network 192.168.8.0 255.255.255.0 area 0
network 192.168.7.0 255.255.255.0 area 0
network 192.168.6.0 255.255.255.0 area 0

//SSH access – User: cisco – Pass: cisco
ip domain-name cisco.com
username cisco password cisco
crypto key generate rsa
1024
line vty 0 15
login local
transport input ssh
ip ssh version 2

do wr

## F2-ROUTER ##

en
conf t
hostname F2-Router

int se0/2/0
no shut
int se0/2/1
no shut
clock rate 64000
int g0/0
no shut

int se0/2/1
ip address 10.10.10.10 255.255.255.252
int se0/2/0
ip address 10.10.10.1 255.255.255.252
exit

do wr

//Inter-VLAN & DHCP server

int g0/0.30
encapsulation dot1q 30
ip address 192.168.3.1 255.255.255.0
exit
ip dhcp pool Sales
network 192.168.3.0 255.255.255.0
default-router 192.168.3.1
dns-server 192.168.3.1
exit

int g0/0.40
encapsulation dot1q 40
ip address 192.168.4.1 255.255.255.0
exit
ip dhcp pool HR
network 192.168.4.0 255.255.255.0
default-router 192.168.4.1
dns-server 192.168.4.1
exit

int g0/0.50
encapsulation dot1q 50
ip address 192.168.5.1 255.255.255.0
exit
ip dhcp pool Finance
network 192.168.5.0 255.255.255.0
default-router 192.168.5.1
dns-server 192.168.5.1
exit
do wr

//OSPF Configuration
router ospf 10
network 10.10.10.0 255.255.255.252 area 0
network 10.10.10.8 255.255.255.252 area 0
network 192.168.3.0 255.255.255.0 area 0
network 192.168.4.0 255.255.255.0 area 0
network 192.68.5.0 255.255.255.0 area 0
do wr

//SSH – User: cisco – Pass: cisco

ip domain-name cisco
username cisco password cisco
crypto key generate rsa
1024
line vty 0 15
login local
transport input ssh
do wr

## F3-ROUTER ##

en 
conf t
hostname F3-Router

int se0/2/0
no shut
int se0/2/1
no shut
int g0/0
no shut
exit
int se0/2/0
ip address 10.10.10.6 255.255.255.252
clock rate 64000
int se0/2/1
ip address 10.10.10.2 255.255.255.252
clock rate 64000
exit
do wr

//Inter-VLAN & DHCP server.
int g0/0.10
encapsulation dot1q 10
ip address 192.168.1.1 255.255.255.0
exit

service dhcp
ip dhcp pool IT
network 192.168.1.0 255.255.255.0
default-router 192.168.1.1
dns-server 192.168.1.1
exit

int g0/0.20
encapsulation dot1q 20
ip address 192.168.2.1 255.255.255.0
exit

ip dhcp pool Admin
network 192.168.2.0 255.255.255.0
default-router 192.168.2.1
dns-server 192.168.2.1
exit

do wr

//OSPF Configuration
router ospf 10
network 10.10.10.0 255.255.255.252 area 0
network 10.10.10.4 255.255.255.252 area 0
network 192.168.1.0 255.255.255.0 area 0
network 192.168.2.0 255.255.255.0 area 0
exit
do wr

//Configure SSH access – User: cisco – Pass: cisco
hostname F3-Router
ip domain-name cisco
username cisco password cisco
crypto key generate rsa
1024
line vty 0 15
login local
transport input ssh
do wr
