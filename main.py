import random
import time
from os import system, name
bal=9
def clear(): 
    if name=="nt": 
        system("cls") 
    else: 
        system("clear")
def randgen():
  return time.time()*1000
def lottonumbers():
  random.seed(randgen())
  return random.randint(0,99)
class achievements:
  def __init__(self,n,d,r,rp,rt,rq,a):
    self.n=n
    self.d=d
    self.r=r
    self.rp=rp
    self.rt=rt
    self.rq=rq
    self.a=a
debt1=achievements("And So Began the Debt", "Go into debt",0,"You don't get a prize for being bad at this","none","bal<0", "[X]")
debt2=achievements("Crushing Debt", "Have 10,000 Magicalus Bucks of debt",0,"reward","reward type","bal<=-10000","[X]")
achievementlist=[debt1,debt2]
unearned=[0,1]
def achievecheck():
  i=0
  while i<len(unearned):
    x=unearned[i]
    if eval(achievementlist[x].rq)==True:
      print(" [Achievement unlocked! "+achievementlist[x].n+": "+achievementlist[x].d+" Reward: "+achievementlist[x].rp+"]")
      achievementlist[x].a="[✓]"
      del unearned[i]
      if achievementlist[x].rt=="":
        pass
      continue
    i=i+1
clear()
print("Hello, and welcome to the Magicalus Casino!\nYou've entered with 50 bucks, and need to make your fortune.\nDon't worry: there's no penalty for going into crushing, crushing debt. So have fun, and hit anything to start!\nNote: Due to lack of coding skill, a win state has not been added yet.")
hghg=input()
while True:
  clear()
  print("Welcome to the Magicalus Casino Lobby!\nYou have "+str(bal)+" Magicalus bucks")
  achievecheck()
  print("Press 1 to play the Lottery\nPress 2 to hit the Slots")
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
      bal=bal-price
      num1=lottonumbers()
      num2=lottonumbers()
      num3=lottonumbers()
      num4=lottonumbers()
      num5=lottonumbers()
      while True:
        win1t=random.randint()
        win1=lottonumbers()
        win2=lottonumbers()
        win3=lottonumbers()
        win4=lottonumbers()
        win5=lottonumbers()
        print("Your numbers are: "+str(num1)+", "+str(num2)+", "+str(num3)+", "+str(num4)+", and "+str(num5))
        hghgh=input()
  elif x=="2":
    clear()
    playagain=""
    while True:
      price=10
      if playagain=="back":
        break
      print("Welcome to the Slot Floor!\nYou have "+str(bal)+" Magicalus bucks")
      achievecheck()
      print('Press enter to play, or say "back" to go back')
      play=input()
      if play=="back":
        break
      bal=bal-price
      random.seed(randgen())
      runtime=0
      s1t=random.randint(20,35)
      s2t=random.randint(37,52)
      s3t=random.randint(54,69)
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
          runtime=runtime+random.randint(1,2)
          continue
        break
      time.sleep(2)
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
        payout=10**winning
        bal=bal+payout
        print("You won "+str(payout)+" Magicalus bucks!")
      print("You have "+str(bal)+" Magicalus bucks")
      achievecheck()
      print("Say back to leave, or say anything else to spin the wheels again!")
      playagain=input()
      clear()
      continue
  else:
    clear()
    print("Theres nothing here. Hit enter to go back.")
    c=input()
    continue