import random
import time
from os import system, name
bal=50
handval=0
done=False
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
cards=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
suitsp=[" of Hearts"," of Diamonds"," of Spades"," of Clubs"]
suits=[0,1,2,3]
denomsp=["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
def drawcard():
  randgen()
  draw=random.choice(cards)
  cards.remove(draw)
  suit=0
  while draw>12:
    if draw>51:
      draw-=52
      continue
    suit+=1
    draw-=13
  return [denomsp[draw],suitsp[suit],draw,suit]
def shuffle():
  if len(cards)<=13 and game=="blackjack":
    return [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
  elif len(cards)<=13:
    return [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
  else:
    return cards
class achievements:
  def __init__(self,n,d,r,rp,rt,rq,a,sn,sd):
    self.n=n
    self.d=d
    self.r=r
    self.rp=rp
    self.rt=rt
    self.rq=rq
    self.a=a
    self.sn=sn
    self.sd=sd
sweep=False
herd=achievements("Herd Mentality", "Have every number in the slot machine be the same.",0,"Insert funny quip here","reward type","sweep==True",False,False,False)
debt1=achievements("And So Began the Debt", "Go into debt.",0,"You don't get a prize for being bad at this.","none","bal<0",False,False,False)
debt2=achievements("Crushing Debt", "Have 10,000 Magicalus Bucks of debt.",0,"Rewards aren't finished yet, screw you.","reward type", "bal<=-10000",False,False,False)
bincheck=False
bin=achievements("01001110 01100101 01110010 01100100 00101110", "Get all 1s and 0s on the slot machine.",0,"Binary joke here.","reward type","bincheck==True",False,True,False)
rpscheck=False
rps=achievements("Rotato Potato","Get a match on the slot machine vertically.",0,"Rotato Potato.","reward type","rpscheck==True",False,True,False)
slot0check=False
slot01=achievements("Computers Count From 0", "Have a 0 when the slot machine stops spinning.",0,"I haven't got an idea what to put here.","reward type","slot0check>=1",False,False,True)
slot02=achievements("You win?", "Get a winning payout on the slot machines with 0s.",0,"I haven't got an idea what to put here.","reward type","slot0check>=2",False,False,True)
slot03=achievements("Base 1", "Have every number on the final slot machine be a 0.",0,"I haven't got an idea what to put here.","reward type","slot0check>=3",False,False,True)
achievementlist=[herd,debt1,debt2,bin,rps,slot01,slot02,slot03]
unearned=[0,1,2,3,4,5,6]
def achievecheck():
  if len(unearned)==0 and won==False:
    clear()
    print("Congratulations! You have just completed The Magicalus Casino! I bet you feel pretty satisfied right now, eh? I hope you do, because that satisfaction is all you get.")
    input()
    clear()
    return True
  elif len(unearned)==0:
    return True
  i=0
  while i<len(unearned):
    x=unearned[i]
    if eval(achievementlist[x].rq)==True:
      print(" [Achievement unlocked! "+achievementlist[x].n+": "+achievementlist[x].d+" Reward: "+achievementlist[x].rp+"]")
      achievementlist[x].a=True
      del unearned[i]
      if achievementlist[x].rt=="":
        pass
      continue
    i+=1
  return False
clear()
print("Hello, and welcome to the Magicalus Casino!\nYou've entered with 50 bucks, and have entered our contest. First to achieve everything in our *extensive* list wins! What's the prize? Uhhhh... self satisfaction? Doesn't matter, just start spending. \nDon't worry: there's no penalty for going into crushing, crushing debt. In fact, it's encouraged!(and necessary to win) So have fun, and hit anything to start!")
input()
while True:
  clear()
  won=achievecheck()
  print("Welcome to the Magicalus Casino Lobby!\nYou have "+str(bal)+" Magicalus bucks")
  print("Press 1 to hit the Slots\nPress 2 to play some Black Jack\nSay Achievements to see how you're doing.")
  nav=input()
  if nav=="1":
    clear()
    while True:
      price=10
      won=achievecheck()
      print("Welcome to the Slot Floor!\nYou have "+str(bal)+" Magicalus bucks")
      print('Press enter to play, or say "back" to go back')
      back=input()
      if back=="back"or back=="Back":
        break
      bal-=price
      random.seed(randgen())
      runtime=0
      s1t=random.randint(20,35)
      s2t=random.randint(37,52)
      s3t=random.randint(54,69)
      slotodds=[0,1,2,3,4,5]
      weights=[0.1,5,4,3,2,1]
      slot1=random.randint(1,5)
      slot2=random.randint(1,5)
      slot3=random.randint(1,5)
      slot1p=random.randint(1,5)
      slot2p=random.randint(1,5)
      slot3p=random.randint(1,5)
      slot1n=random.randint(1,5)
      slot2n=random.randint(1,5)
      slot3n=random.randint(1,5)
      winning=-1
      while True:
        if s1t>runtime:
          slot1p=slot1
          slot1=slot1n
          slot1n=random.choices(slotodds,weights)
          slot1n=int(str(slot1n[0]).replace("[",""). replace("]",""))
        if s2t>runtime:
          slot2p=slot2
          slot2=slot2n
          slot2n=random.choices(slotodds,weights)
          slot2n=int(str(slot2n[0]).replace("[",""). replace("]",""))
        if s3t>runtime:
          slot3p=slot3
          slot3=slot3n
          slot3n=random.choices(slotodds,weights)
          slot3n=int(str(slot3n[0]).replace("[",""). replace("]",""))
        print("╔═════╤═════╤═════╗\n║     |     |     ║\n║ ["+str(slot1n)+"] | ["+str(slot2n)+"] | ["+str(slot3n)+"] ║\n║     |     |     ║\n║     |     |     ║\n║ ["+str(slot1)+"] | ["+str(slot2)+"] | ["+str(slot3)+"] ║\n║     |     |     ║\n║     |     |     ║\n║ ["+str(slot1p)+"] | ["+str(slot2p)+"] | ["+str(slot3p)+"] ║\n║     |     |     ║\n╚═════╧═════╧═════╝")
        time.sleep(0.075)
        if s3t>runtime:
          clear()
          runtime+=random.randint(1,2)
          continue
        break
      time.sleep(2)
      clear()
      slotwon=True
      if slot1==slot2==slot3 or slot1n==slot2==slot3p or slot1p==slot2==slot3n:
        winning=slot2
      elif slot1n==slot2n==slot3n:
        winning=slot2n
      elif slot1p==slot2p==slot3p:
        winning=slot2p
      else:
        slotwon=False
      if slot1==0 or slot1n==0 or slot1p==0 or slot2==0 or slot2n==0 or slot2p==0 or slot3==0 or slot3n==0 or slot3p==0:
        slot0check=1
      if (slot1==0 or slot1==1) and (slot1n==0 or slot1n==1) and (slot1p==0 or slot1p==1) and (slot2==0 or slot2==1) and (slot2n==0 or slot2n==1) and (slot2p==0 or slot2p==1) and (slot3==0 or slot3==1) and (slot3n==0 or slot3n==1) and (slot3p==0 or slot3p==1):
        bincheck=True
      if winning==0:
        slot0check=2
      if slot1==slot1n==slot1p==slot2==slot2n==slot2p==slot3==slot3n==slot3p:
        if slot1==0:
          slot0check=3
        print("Congratulations! You got a full sweep of "+str(winning)+" Your winning number will be multiplied by three!")
        winning*=3
        sweep=True
      if slotwon==False:
        print("Better luck next time!")
      else:
        payout=10**winning
        bal+=payout
        print("You got the "+str(winning)+" Jackpot!")
        print("You won "+str(payout)+" Magicalus bucks!")
      won=achievecheck()
      print("You have "+str(bal)+" Magicalus bucks")
      print("Say back to leave, or say anything else to spin the wheels again!")
      back=input()
      if back=="back" or back=="Back":
        break
      clear()
      continue
  elif nav=="2":
    clear()
    while True:
      if done==True:
        done=False
        break
      game="blackjack"
      clear()
      won=achievecheck()
      print("You have "+str(bal)+" Magicalus Bucks. There's no flat price, just betting.\nAll tables have 2 decks and 75% penetration.\nSay back at anytime to leave at the end of the hand(including on the winstate).\nPress enter to play, or say back to go to the casino floor.")
      back=input()
      if back=="back"or back=="Back":
        break
      cards=shuffle()
      while True:
        handval=0
        end=[False,0]
        if done==True:
          break
        print("How much would you like to bet on this hand?(You can press enter to just bet 100)")
        while True:
          try:
            bet=input()
            if bet=="":
              bet=100
            else:
              bet=int(bet)
            break
          except ValueError:
            if bet=="back" or bet=="Back":
              done=True
              break
            print("Please input a valid integer")
        if done==True:
          break
        bal=bal-bet
        clear()
        print("Your current bet is: "+str(bet))
        while True:
          cards=shuffle()
          drawn=drawcard()
          print(drawn[0]+drawn[1])
          handval+=drawn[2]+1
          if handval>21:
            print("You busted!")
            end=[True,0]
          if handval==21:
            print("You got 21!")
            end=[True,1]
          play=input()
          if play=="back" or play=="Back":
            done=True
          if end[0]==True:
            clear()
            break
  elif nav=="Achievements" or nav=="achievements":
    clear()
    i=0
    while i<len(achievementlist):
      if achievementlist[i].a==True:
        print("- "+achievementlist[i].n+": "+achievementlist[i].d+" Reward: "+achievementlist[i].rp+" [✓]")
      else:
        if achievementlist[i].sn==True:
          print("- ???: ",end="")
        else:
          print("- "+achievementlist[i].n,end=": ")
        if achievementlist[i].sd==True:
          print(" ??? ",end="")
        else:
          print(achievementlist[i].d,end=" ")
        print("Reward: ??? [X]")
      i+=1
      continue
    input()
  else:
    clear()
    print("Theres nothing here. Hit enter to go back.")
    input()
    continue