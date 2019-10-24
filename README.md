# Adonis ARP Python Spoofer
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

This tool is an ARP spoofer written in Python for MS Windows, Mac OS and Linux OSs. It allows you to launch a Man-In-The-Middle attack (MITM). This is an ethical hacking educational tool used for educational purposes only (please see code of conduct). The tool is named after the mortal lover of the goddess Aphrodite.

The tool is part of an Ethical Hacker Educational toolset taught normally in ethical hacking and computer security degrees/courses (please see code of conduct). 

Tanit Keylogger is part of a toolset of Ethical Hacking tools that I will publish gradually on Github.
1. Tanit Keylogger (Language: Python) - Go to [repository URL](https://github.com/HusseinBakri/Tanit-Keylogger "Tanit Keylogger").
2. Adonis ARP Spoofer (Language: Python), ***current repository***.
3. Simple MAC Changer (Language: Python), repository URL (will be added later).
4. Anat Network Discoverer and Port Scanner (Language: Python), Go to [repository URL](https://github.com/HusseinBakri/Anat-Network-Discoverer-and-Port-Scanner "Anat Network Discoverer and Port Scanner").
5. Hadad Packet Sniffer (Language: Python), repository URL (will be added later).
6. Shahar DNS Spoofer (Language: Python), repository URL (will be added later).
7. Sweet Death Virus (Language: Python), repository URL (will be added later).
8. Baal Backdoor (Language: Python), repository URL (will be added later).
9. Vulnerability Scanner (Language: Python), repository URL (will be added later).


# Code of Conduct
**Launching this tool against unauthorised and unwilling users is both immoral and illegal. As a white hat hacker or security specialist, your job after taking permission, is to discover vulnerabilities in programs, systems and networks (white hat hacking) or help in discovering any gullibility in users (by social engineering). Thus, you can launch Adonis or any other tool I might publish later in this hacking series only when you are given explicit permission by the company that hires you or only launch it against your own servers or networks. This tool is written after taking several Ethical Hacking and Security courses. So, in other words, the code (which has a generated executable intentionally detectable by antiviruses) can be found in a form or another in many ethical hacking books and courses. I have added some enhancements to the tool. To reiterate: This is a tool written for the sole purpose of teaching you how a network ARP Spoofer work and it really shows you how much it is easy to write a simple, effective and yet powerful ARP Spoofer in Python for the purposes of Man-In-The-Middle attacks. This tool is for educational purposes only and it is not meant to be used in any harmful way. To reiterate, this tool is meant to be a tool to be studied by white hat hackers and security specialists and is not meant to be deployed or used against users that do not give you explicit permission.**


# Description
When you successfully fool the victim and the destination by making your machine the man in the middle via the tool presented here, you need to remember to make your machine forward all the packets received from the victim. In other words, you need to enable IP forwarding which is disabled by default. 

Adonis detects your operating system and if it is a Linux or a MacOS, it tries to enable IP forwarding for you. Please do not forget to launch Adonis with ***sudo privileges***. Now I would assume, well usually it is the case that the attacker is using a Linux distro for the attack (or for hacking purposes in general) such as Ubuntu, Fedora or even better more professionally a Kali Linux. I strongly advice you to enable IP forwarding in case Adonis was not successful in enabling this service. This should be done before you launch the attack. The process of enabling IP forwarding might a litle bit tricker in an MS Windows machine with a reboot probably required. 

To check whether you have IP forwarding enabled, you can issue the following command on a Linux OS:
```
cat /proc/sys/net/ipv4/ip_forward
```
If you get a 0, it means it is disabled. To enable the forwarding of packets through your machine (i.e. to make your machine play the role of router/gateway), you need to issue any of following commands:
```
sudo sysctl -w net.ipv4.ip_forward=1
```
OR

```
sudo echo 1 > /proc/sys/net/ipv4/ip_forward 
```

During the attack always keep an eye on ***the arp table***, to see that the MAC address of the destination host or usually the router have changed to your machine MAC Address. 
```
arp -a
```

Adonis has the ability to find the gateway IP or router IP for you to automate things further so you have to only provide the victim IP but this is not always guaranteed to work. If you find any problems comment out the function that deals with that in the code.

# Requirements
You need to install the Python modules: scapy, netifaces and optparse

```
sudo pip3 scapy netifaces optparse
```
## Usage
Run the tool using ***sudo*** in Linux/MacOS since it enables IP forwarding automatically for you: if you are on Linux/MacOS machine. Otherwise, if it detects another OS like MS Windows, it then asks you to make sure that you enable IP forwarding and then ask you to continue using the tool.

***Usage 1: Victim IP and Gateway/Destination IP are needed***

```
sudo python3 ARPSpoofer.py -t 172.18.47.254 -s 224.0.0.252 
```

***Usage 2: Only Victim IP is needed***
You can only specify only a victim IP or target IP and Adonis try to find the IP of your gateway or router for you which facilitate life I guess. This might not work in some situations so amend the code as needed.

```
sudo python3 ARPSpoofer.py -t 172.18.47.254
```
When you close Adonis via a Ctrl-C or a keyboard Interrupt from the terminal, it restores back the ARP table for you (by sending necessary ARP packets to return everything back to the way it was). I guess this is a classical thing that all ARP spoofers should do when the attack is finished.

# Packaging Adonis
You need the Python module pyinstaller. You can install it via pip or pip3 or via apt package manager.
```
pip3 install pyinstaller
```

A program called pyinstaller is installed in the Python directory. On Windows it would be an executable: pyinstaller.exe

## Notez Bien - Antivirus might not be happy!!!

Please turn off ***any antivirus***  especially if you are on a Windows since the executable generated **might be detected** and the antivirus will try to delete or quarantine it. Antivirus evasion is addressed in a section titled 'Avoiding antiviruses' in the Tanit Keylogger Repository. For the purpose of this program which is a tool you as an attacker will be using, so there is no need to be concerned by this. But if you are creating a virus or a trojan horse or a keylogger then Antivirus evation is a serious concern. 

```
pyinstaller main.py --onefile
```
--onefile means  pyinstaller will package all the python files into a single executable. Your .exe file will be found in the dist folder.

## Create a Windows .exe executable out of a python project from a Linux OS/Mac OS
As you know to run a Windows .exe or .msi or anything similar on a Linux OS (even on Mac OS) you need a lovely program called  [wine](https://www.winehq.org/). I would assume you have installed wine on Linux. Go to the official Python Website and download the right Python 2.7.x msi installation file or whatever Python 3.x.x version you need. Navigate on your Linux to the directory of the download directory of this file and then run the following command: (/i is for installing):
```
wine msiexec /i python-2.7.14.msi
```
You will get a normal installation process as you would have on any MS Windows OS, please follow the instructions to install the Python interpreter. All Programs that are installed in wine are located in a hidden folder called '.wine' in the Home Folder of the user. So probably your Windows Python will be 
installed per example in ~/.wine/drive_c/Python27/ and in there all the cool executables that normally are installed like Python.exe, pip.exe .... Navigate to this folder and run via wine the Python interpreter invoking pip in order for you to install as above the 'pyinstaller' module.

NB: wine does not and can not by default access the pip modules of the Linux OS so this why you need to do this.
```
cd ~/.wine/drive_c/Python27/
wine python.exe -m pip install pyinstaller
```
After the installation of the module terminates successively, you will find the pyinstalller.exe in the Scripts directory.
To install pynput (why? as I have mentioned above, you need to do that since even this module is installed on the Linux OS, the Windows Python interpreter can not access OS Python level modules.)

```
wine python.exe -m pip install pynput
```

You can then package Adonis into a single executable:

```
wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe main.py --onefile --noconsole
```
The binary will be stored in the dist folder.

## Creating a Mac OS executable of Adonis
If you are on a Mac OS, the process is the same for installing 'pyinstaller'. First install pyinstaller through latest pip - with sudo privileges. NB: it is better to get the latest pip so to avoid errors. 

```
sudo pip install pyinstaller
```

Then run pyinstaller on main.py

```
pyinstaller main.py --onefile --noconsole
```
The binary will be stored in the dist folder.

## Creating a Linux OS executable of Adonis
The process is exactly similar. The good thing in Linux is that binaries like Adonis in Linux don't get executed by double click from the the user, they need to be run from the terminal after chmod +x makes them executable. 

# Enhancements
* Integrate a scanner into Adonis

# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author (me!) and the site or the document where the program is taken from.
