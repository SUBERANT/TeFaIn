#Author this script is SUBERANT.
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
    os.system("pkg install bash-completion -y")
    os.system("pkg install ifconfig -y")
    os.system("pkg install git -y")
    os.system("pkg install python -y")
    os.system("pkg install python2 -y")
    os.system("pkg install nmap -y")
    os.system("pkg install ngrok -y")
    os.system("pip install --upgrage pip")
    os.system("pip2 install --upgrade pip")
    os.system("pip3 install --upgrade pip")
    os.system("pip3 install upgrade")
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
    os.system("cd")
    os.system("clear")
    print("=======================================")
    print("        Установка прошла успешно!")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")
if choose == "n":
    print("=======================================")
    print("Нажмите ENTER чтобы выйти из программы.")
    print("=======================================")
    input()
    os.system("clear")

    

