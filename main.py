import random
import math
import time
from os import system, name
def clear(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')
def randgen():
  return time.time()*1000
def lottonumbers():
  random.seed(randgen())
  return random.randint(0,99)
bal=0
clear()
print("Hello, and welcome to the Magicalus Casino!\nYou've entered with nothing, and need to make your fortune.\nDon't worry: there's no penalty for going into crushing, crushing debt. So have fun, and hit anything to start!\nNote: Due to lack of coding skill, a win state has not been added yet.")
hghg=input()
while True:
  clear()
  print("Welcome to the Magicalus Casino Lobby!\nYou have "+str(bal)+" Magicalus bucks\nPress 1 to play the Lottery\nPress 2 to hit the Slots")
  x=input()
  if x=="1":
    clear()
    playagain=""
    while True:
      price=10
      if playagain=="back":
       break
      print("You have "+str(bal)+" Magicalus Bucks. It costs "+str(price)+" to play.\nPress enter to play. Or say back to go to the casino floor.")
      back=input()
      if back=="back":
        break
      num1=lottonumbers()
      num2=lottonumbers()
      num3=lottonumbers()
      num4=lottonumbers()
      num5=lottonumbers()
      while True:
        win1=lottonumbers()
        win2=lottonumbers()
        win3=lottonumbers()
        win4=lottonumbers()
        win5=lottonumbers()
        print("Your numbers are:"+str(num1)+" "+str(num2)+" "+str(num3)+" "+str(num4)+" "+str(num5))
        hghgh=input()
  elif x=="2":
    clear()
    playagain=""
    while True:
      price=10
      if playagain=="back":
        break
      print("Welcome to the Slot Floor!\nYou have "+str(bal)+" Magicalus bucks")
      print('Press enter to play, or say "back" to go back')
      play=input()
      if play=="back":
        break
      bal=bal-price
      random.seed(randgen())
      epoch=math.floor(time.time())
      slottime=math.ceil(epoch)
      runtime=0
      s1t=random.randint(30,50)
      s2t=random.randint(52,72)
      s3t=random.randint(74,94)
      slotodds=[1,1,1,1,1,2,2,2,2,3,3,3,4,4,5]
      slot1=random.randint(1,5)
      slot2=random.randint(1,5)
      slot3=random.randint(1,5)
      slot1p=random.randint(1,5)
      slot2p=random.randint(1,5)
      slot3p=random.randint(1,5)
      slot1n=random.randint(1,5)
      slot2n=random.randint(1,5)
      slot3n=random.randint(1,5)
      winning=0
      while True:
        if s1t>runtime:
          slot1p=slot1
          slot1=slot1n
          slot1n=random.choice(slotodds)
        if s2t>runtime:
          slot2p=slot2
          slot2=slot2n
          slot2n=random.choice(slotodds)
        if s3t>runtime:
          slot3p=slot3
          slot3=slot3n
          slot3n=random.choice(slotodds, )
        print("╔═════╤═════╤═════╗\n║ ["+str(slot1n)+"] | ["+str(slot2n)+"] | ["+str(slot3n)+"] ║\n║     |     |     ║\n║     |     |     ║\n║ ["+str(slot1)+"] | ["+str(slot2)+"] | ["+str(slot3)+"] ║\n║     |     |     ║\n║     |     |     ║\n║ ["+str(slot1p)+"] | ["+str(slot2p)+"] | ["+str(slot3p)+"] ║\n╚═════╧═════╧═════╝")
        time.sleep(0.075)
        if s3t>runtime:
          clear()
          runtime=runtime+1
          continue
        time.sleep(1.5)
        clear()
        if slot1==slot2==slot3 or slot1n==slot2==slot3p or slot1p==slot2==slot3n:
          winning=slot2
        elif slot1n==slot2n==slot3n:
          winning=slot2n
        elif slot1p==slot2p==slot3p:
          winning=slot2p
        if winning==0:
          print("Better luck next time!")
        else:
          payout=10**int(winning)
          bal=bal+payout
          print("You won "+str(payout)+" Magicalus bucks!")
        print("Say back to leave, or say anything else to spin the wheels again!")
        playagain=input()
        clear()
        break
  else:
    clear()
    print("Theres nothing here. Hit enter to go back.")
    c=input()
    continue