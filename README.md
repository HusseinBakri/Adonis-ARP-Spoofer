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

# Requirements

## Usage



# Packaging
You need the pyinstaller. You can install it via pip or pip3 or via apt package manager.
```
pip install pyinstaller
```

A program called pyinstaller is installed in the Python directory. On Windows it would be an executable: pyinstaller.exe

## Notez Bien - Antivirus won't be happy!!!

Please turn off ***any antivirus*** on the target system since the executable might be detected and the antivirus will try to delete or quarantine it. Antivirus evasion is addressed in the section titled 'Avoiding antiviruses'.

```
pyinstaller main.py --onefile
```
--onefile means  pyinstaller will package all the python files into a single executable

## How to package and run the excutable silently (without showing a terminal to the user)
If you do not want the user to see a command prompt after the .exe is run. You can add another argument called
--noconsole

```
pyinstaller main.py --onefile --noconsole
```

This can work in almost all instances except when your Python code deals with standard input/output/error. 

You have to explicitly deal with standard error and standard input so per example if we have something like (just an example)
```
result = subprocess.check_output(command, shell=True)
```

You need to handle the 'stderr' and 'stdin' by throwing them in the Abyss!

### For Python 3
```
result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL )
```
### For Python 2 (you need to import the os module)
```
DEVNULL = open(os.devnull, 'wb')
result = subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL )
```

## Create a Windows .exe executable out of a python project from a Linux OS/Mac OS
As you know to run a Windows .exe or .msi or anything similar on a Linux OS (even on Mac OS) you need a lovely program called  [wine](https://www.winehq.org/). I would assume you have installed wine on Linux. Go to the official Python Website and download the right Python 2.7.x msi installation file. Navigate on your Linux to the directory of the download directory of this file and then run the following command: (/i is for installing):
```
wine msiexec /i python-2.7.14.msi
```
You will get a normal installation process as you would have on any MS Windows OS, please follow the instruction to install the Python interpreter. All Programs are usually installed in wine in a hidden folder called '.wine' in the Home Folder of the user. So probably your Windows Python will be 
installed in ~/.wine/drive_c/Python27/ and in there all the cool executable that normally are installed like Python.exe .... Naviagate to this folder and run via wine the Python interpreter invoking pip in order for you to install as above the 'pyinstaller' module.

PS: wine does not access the pip modules of the Linux so this why you need to do this.
```
cd ~/.wine/drive_c/Python27/
wine python.exe -m pip install pyinstaller
```
After the installation of the module successively terminates, you will find the pyinstalller.exe in the Scripts directory.
To install pynput (why? as mentioned above, you need to do that as even this module is installed on Linux OS, the Windows Python interpreter needs this)

```
wine python.exe -m pip install pynput
```

You can then package Tanit Keylogger into a single executable:

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
The process is exactly similar. The good thing in Linux is that binaries in Linux don't get executed by just making the target user double click them, they need to be run from the terminal after chmod +x makes them executable. This is why Linux rocks, the good thing it is very difficult a experience Linux users (in social enginering, a white hat hacker is hired by many companies these days to test not only the security of networks and systems but also in similar vein to test the gullibility of the company's clerks by the black hat hacker pretending to be from the IT department! 

# Enhancements


## Avoiding antiviruses
I have to mention the fact that the mere act of writing your own Hacking/Security programs with your own way of coding makes these programs unique in a way and thus undetectable and you will know why when I explain the main techniques used by antiviruses. Source Codes and by consequence executable binaries generated out of them, are always detected when they are either too traditional or have been used by many people (so they ended up as a signature in Antiviruses databases). Per instance, the code here has great parts from many sources (a salad of code) and that is intentional.

Now the tricks here are really a race with time for different reasons:
- 1st technique: Anti-viruses compares your program to a huge database of signatures of other malware. By huge, I mean massive. In lay terms, huge number of signatures (i.e. snippets of logic if you want) sort of database of malware logic.
- 2nd technique: This technique is used in tandem with the first technique and works as a safe guard if the signature is not found. It compares the behaviour of your program in real-time using a sandbox or virtual environment. The comparision involves sometimes some clever machine and deep learning algorithms. Now of course every antivirus gives this technique some sort of a brand and fancy name but it boils down to the same concepts. In nutshel, the antivisus try to figure out if your program is doing something suspicious like opening a network port or downloading things or taking snapshots or capturing keystrokes, or connecting to a remote host vel cetera...

You sould be worried about the second technique when you want to evade antivirus more than the first one, becuase you have literally at your disposable a trillion methods to make your program quite unique to fool an antivirus to think it is harmless and thus no signature would be matched in this way. That does not mean the second technique could not be defeated.

Some Source Code tricks (which is a big field and an art in itself so this is just a drop from the ocean):
1. Add useless code before, in-between (if possible) and after the malicious code. Add a lot of padding logic (useless loops, useless mathematical operations etc...)
2. Play with sleep patterns of your Python scripts (pausing the program and resuming it, then pausing and resuming)
3. Play with program threading like spawning threads especially useless ones per example some weird mathematical equation calculation  in a seperate thread (this achieves amazing results)
4. Add variables that are gibberish. There are some tools that transform all your variables to shorter names or gibberish. These types of tools are called 'obfuscation tools' that fool and confuse both humans and antiviruses. Black and grey hat Hackers usually change the code of the program to the point that the padding or usefull behaviour should be far more sizable in your tool than the actual malicous code which should is notmally scattered in different places of your program.
...

Some Binaries/executable tricks:
1. Changing the Binaries and adding padding (this require knowledge in reverse enginneering and changing hex codes). Same things you did in the source code but this time on the level of the executable itself.
2. An easier way: Compressing the binaries or executables (like compressing the .exe) via tools like UPX (https://github.com/upx/upx), a tool that compresses exe files.

Scan your exe via tools and online services that scan your tool across different antiviruses (famous and non famous) WITHOUT submitting the results to antiviruses. One service that is quite handy is called NoDistribute (https://nodistribute.com/).

Please after you are successfull in running your hacking tool evading antiviruses, you are bound by an ethical code of conduct, so you are required morally and legally to submit your tool and code to antiviruses databases.

# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author (me!) and the site or the document where the program is taken from.
