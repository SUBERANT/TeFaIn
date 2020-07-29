#Author this script is SUBERANT.
#infinite-bomber, Author smelhack.
#IPGeoLocation, Author maldevel
#userrecon v1.0, Author: @thelinuxchoice
#This script only for Termux.
#TeFaIn(Termux Fast Install)
import os
from colorama import Fore, Back, Style, init
init()

#Commands
print(Fore.CYAN)
choose = input("Начать установку? (y/n): ")
if choose == "y":
    os.system("apt update -y")
    os.system("pkg update -y")
    os.system("apt upgrade -y")
    os.system("pkg upgrade -y")
    os.system("pkg install git -y")
    os.system("pkg install python -y")
    os.system("pkg install python2 -y")
    os.system("pip install --upgrage pip -y")
    os.system("pip2 install --upgrade pip -y")
    os.system("pip3 install --upgrade pip -y")
    os.system("pip3 install upgrade -y")
    os.system("pip3 install colorama -y")
    os.system("pip3 install termcolor -y")
    os.system("pip install termcolor -y")
    os.system("pip install colorama -y")
    os.system("pip install requests -y")
    os.system("pip2 install requests -y")
    os.system("pkg install root-repo -y")
    os.system("pkg install unstable-repo -y")
    os.system("pkg install x11-repo -y")
    os.system("pkg install wget -y")
    os.system("cd $HOME && https://github.com/thelinuxchoice/userrecon.git -y")
    os.system("cd userrecon")
    os.system("chmod +x userrecon")
    os.system("cd $HOME && git clone https://github.com/maldevel/IPGeoLocation.git -y")
    os.system("cd IPGeoLocation")
    os.system("pip3 install -r requirements.txt --user")
    os.system("cd $HOME && git clone https://github.com/smelhack/infinite-bomber.git -y")
    os.system("cd")
    os.system("cd infinite-bomber/infinite-bomber-reborn/builds/android/Infinite-Bomber-arm/")
    os.system("chmod +x infinite-bomber")
    os.system("cd")
    os.system("cd infinite-bomber/infinite-bomber-reborn/builds/android/Infinite-Bomber-arm-without-tor/")
    os.system("chmod +x infinite-bomber")
    os.system("cd")
    os.system("clear")
    print(Fore.GREEN)
    print("=======================================")
    print("        Установка прошла успешно!")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")
if choose == "n":
    print(Fore.GREEN)
    print("=======================================")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")

    

