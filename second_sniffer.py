#! /usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()
pkt=sniff(iface='br-c912b7f540a9', filter='tcp and port 23 and host 10.9.0.6', prn=print_pkt)