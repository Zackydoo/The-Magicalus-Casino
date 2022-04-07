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
bal=0
loan=0
print("Hello, and welcome to the Magicalus Casino!\nYou've entered with nothing, and need to make your fortune.\nDon't worry: there's no penalty for going into curshing, crushing debt. So have fun, and hit anything to start!")
hghg=input
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
     print("You have "+str(bal)+" Magicalus Bucks. It costs "+str(price)+" to play.")
     print("Press enter to play. Or say back to go to the casino floor.")
     back=input()
     if back=="back":
      break
  elif x=="2":
    clear()
    playagain=""
    while True:
      price=10
      if playagain=="back":
        break
      print("Slot Machine Wing\nYou have "+str(bal)+" Magicalus bucks")
      print("Press enter to play, or say "+'"back"'+" to go back")
      play=input()
      if play=="back":
        break
      bal=bal-price
      random.seed(randgen())
      epoch=math.floor(time.time())
      slottime=math.ceil(epoch)
      runtime=0
      s1t=random.randint(10,20)*0.1
      s2t=random.randint(21,30)*0.1
      s3t=random.randint(31,40)*0.1
      slotodds=[1,2,3,4,5,6,7,8,9]
      rigging=[9,8,7,6,5,4,3,2,1]
      slot1=random.randint(1,5)
      slot2=random.randint(1,5)
      slot3=random.randint(1,5)
      slot1p=random.randint(1,5)
      slot2p=random.randint(1,5)
      slot3p=random.randint(1,5)
      slot1n=random.randint(1,5)
      slot2n=random.randint(1,5)
      slot3n=random.randint(1,5)
      while True:
       epoch=math.floor(time.time())
       if slottime<epoch:
         slottime=math.ceil(time.time())
         runtime=runtime+1 
       if s1t>runtime:
         slot1p=slot1
         slot1=slot1n
         slot1n=random.choices(population=slotodds, weights=rigging)
       if s2t>runtime:
         slot2p=slot2
         slot2=slot2n
         slot2n=random.choices(population=slotodds, weights=rigging)
       if s3t>runtime:
         slot3p=slot3
         slot3=slot3n
         slot3n=random.choices(population=slotodds, weights=rigging)
       print("╔═════╤═════╤═════╗\n║ "+str(slot1n)+" | "+str(slot2n)+" | "+str(slot3n)+" ║\n║     |     |     ║\n║     |     |     ║\n║ "+str(slot1)+" | "+str(slot2)+" | "+str(slot3)+" ║\n║     |     |     ║\n║     |     |     ║\n║ "+str(slot1p)+" | "+str(slot2p)+" | "+str(slot3p)+" ║\n╚═════╧═════╧═════╝")
       if s1t>runtime or s2t>runtime or s3t>runtime:
         clear()
         continue
       time.sleep(1.5)
       clear()
       if slot1==slot2==slot3 or slot1n==slot2==slot3p or slot1p==slot2==slot3n:
        paya=str(slot2)
       elif slot1n==slot2n==slot3n:
        paya=str(slot2n)
       elif slot1p==slot2p==slot3p:
        paya=str(slot2p) 
       else:
         paya=0
       if paya==0:
         print("Better luck next time!")
       else:
        paya=paya.replace("[","")
        payout=10**int(paya.replace("]",""))
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