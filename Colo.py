#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date


expirydate = datetime.date(2022, 1, 12)
#expirydate = datetime.date(2021, 12, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum+1

    def lawde_time_pe_khel(n):
        check=0
        for digit in (n):
            if(int(digit)==0):
                check=check+1
        return check
    clear()
    y=1
    newperiod=period
    banner='figlet RXCE'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @RXCE_HACKING")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1," : RED")
            else:
                print(newperiod+1,"  :GREEN")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"   : RED")
            else:
                print(newperiod+1,"   :GREEN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @RXCE_HACKING")
            #print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=5, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=23, minute=35, second=0, microsecond=0)
    
    if (now>First and now<Firstend):
            period=217
            hero()
    
    else:
        banner='figlet Rxce 7.o '
        print("Hi!! Thanks for buying Life time the hack")
        print("----------Your play time-----------")
        print(" 10:00 PM- 10:35 PM")
        print(" 12:00 PM- 12:35 PM")
        print(" 03:00 PM- 03:35 PM")
        print(" 08:00 PM- 08:35 PM")
        print(" 11:00 PM- 12:35 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @Hackmgk ")
else:
    banner='figlet Thank '
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@hackmgk for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 2.     3000 INR -------  30 Days")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print( "Msg me on telegram @hackmgk")
