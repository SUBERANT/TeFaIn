#Author this script is SUBERANT.
#userrecon, Author is @thelinuxchoice.
#infinite-bomber, is smelhack.
#IPGeoLocation, is maldevel.
#This script only for Termux.
#TeFaIn(Termux Fast Install)
import os

#Commands
choose = input("Начать установку? (y/n): ")
if choose == "y":
    os.system("apt update -y")
    os.system("pkg update -y")
    os.system("apt upgrade -y")
    os.system("pkg upgrade -y")
    os.system("pkg install curl -y")
    os.system("pkg install toilet -y")
    os.system("pkg install bash-completion -y")
    os.system("pkg install ifconfig -y")
    os.system("pkg install git -y")
    os.system("pkg install nano -y")
    os.system("pkg install python -y")
    os.system("pkg install python2 -y")
    os.system("apt-get install python3-setuptools")
    os.system("pkg install zsh -y")
    os.system("pkg install micro -y")
    os.system("pkg install nmap -y")
    os.system("pkg install ngrok -y")
    os.system("pip3 install colorama")
    os.system("pip3 install termcolor")
    os.system("pip install termcolor")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip2 install requests")
    os.system("pkg install root-repo -y")
    os.system("pkg install unstable-repo -y")
    os.system("pkg install x11-repo -y")
    os.system("pkg install wget -y")
    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
    os.system("cd /data/data/com.termux/files/home && cd /data/data/com.termux/files/home/IPGeoLocation")
    os.system("chmod +x ipgeolocation.py")
    os.system("pip install -r requirements.txt")
    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/wishihab/userrecon.git")
    os.system("cd /data/data/com.termux/files/home && cd /data/data/com.termux/files/home/userrecon")
    os.system("chmod +x userrecon.sh")
    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/smelhack/infinite-bomber.git")
    os.system("cd /data/data/com.termux/files/home && cd /data/data/com.termux/files/home/infinite-bomber/infinite-bomber-reborn/builds/android/Infinite-Bomber-arm/")
    os.system("chmod +x infinite-bomber")
    os.system("cd /data/data/com.termux/files/home && cd /data/data/com.termux/files/home/infinite-bomber/infinite-bomber-reborn/builds/android/Infinite-Bomber-arm-without-tor/")
    os.system("chmod +x infinite-bomber")
    os.system("cd /data/data/com.termux/files/home")
    os.system("clear")
    print("=======================================")
    print("        Установка прошла успешно!")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")
if choose == "n":
    os.system("clear")
    print("=======================================")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")
    

    

