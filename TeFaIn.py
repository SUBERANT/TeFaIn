#Author this script is SUBERANT.
#Author infinite-bomber is smelhack.
#Author sAINT is tiagorlampert.
#This script only for Termux.
#TeFaIn(Termux Fast Install)
import os

choose = input("Начать установку (y/n): ")
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
    os.system("git clone https://github.com/smelhack/infinite-bomber -y")
    os.system("git clone https://github.com/tiagorlampert/sAINT -y")
    os.system("cd")
    os.system("cd infinite-bomber/infinite-bomber-reborn/builds/android/Infinite-Bomber-arm/")
    os.system("chmod +x infinite-bomber")
    os.system("cd")
    os.system("cd infinite-bomber/infinite-bomber-reborn/builds/android/Infinite-Bomber-arm-without-tor/")
    os.system("chmod +x infinite-bomber")
    os.system("cd")
    os.system("clear")
    print("=======================================")
    print("        Установка прошла успешно!")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")
else:
    print("Ошибка!")
    input("Нажмите ENTER чтобы выйти.")
if choose == "n":
    print("=======================================")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")
else:
    print("Ошибка")
    input("Нажмите ENTER чтобы выйти.")

    

