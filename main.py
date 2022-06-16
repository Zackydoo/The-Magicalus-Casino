import random
import time
import math
from os import system, name
won=False
bal=100
handval=0
chandval=0
acemods=0
cacemods=0
done=False
def ignoreinput():
  try:
    import msvcrt
    while msvcrt.kbhit():
      msvcrt.getch()
  except ImportError:
    import sys, termios 
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
singdc=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
doubdc=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
slotpos=[0,1,2,3,4,5,6,7,8]
bjreg=100
def clear(): 
    if name=="nt": 
        system("cls") 
    else: 
        system("clear")
def randgen():
  return time.time()*1000
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
  return [denomsp[draw],suitsp[suit],draw+1,suit]
def shuffle():
  if len(cards)<=26 and (game=="blackjack"):
    return doubdc[:]
  elif len(cards)<=13:
    return [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
  else:
    return cards
class achievements:
  def __init__(self,n,d,r,rp,rt,rq,a):
    self.n=n
    self.d=d
    self.r=r
    self.rp=rp
    self.rt=rt
    self.rq=rq
    self.a=a
sweep=False
herd=achievements("Herd Mentality", "Have every number in the slot machine be the same.",0,"x","reward type","sweep==True",False)
debt1=achievements("And So Began the Debt", "Go into debt.",0,"You don't get a prize for being bad at this.","none","bal<0",False)
debt2=achievements("Crushing Debt", "Have 10,000 Magicalus Bucks of debt.",0,"Rewards aren't finished yet, screw you.","reward type", "bal<=-10000",False)
bincheck=False
bin=achievements("01001110 01100101 01110010 01100100 00101110", "Get all 1s and 0s on the slot machine.",0,"Binary joke here.","reward type","bincheck==True",False)
wwcheck=False
ww=achievements("Wrong Way","Get a match on the slot machine vertically.",0,"Horizontal Progression! You unlocked (not programmed sorry)","reward type","wwcheck==True",False)
slot0check=0
slot01=achievements("Computers Count From 0", "Have a 0 when the slot machine stops spinning.",0,"I haven't got an idea what to put here.","reward type","slot0check>=1",False)
slot02=achievements("You win?", "Get a winning payout on the slot machines with zeroes.",0,"I haven't got an idea what to put here.","reward type","slot0check>=2",False)
slot03=achievements("Base 1", "Have the entire slot machine filled with zeroes.",0,"0000000","reward type","slot0check>=3",False)
awfcheck=False
awf=achievements("Avid Wiki Fan", "Translate the morse code on the achievements page of the Github wiki.",0,"Get prize","reward type","awfcheck==True",False)
achievementlist=[debt1,debt2,ww,slot01]
egachievementlist=[slot02,slot03,bin,herd,awf]
unearned=[0,1,2,3]
unearnedeg=[0,1,2,3,4]
def achievecheck():
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
  i=0
  while i<len(unearnedeg):
    x=unearnedeg[i]
    if eval(egachievementlist[x].rq)==True:
      print(" [Endgame Achievement unlocked! "+egachievementlist[x].n+": "+egachievementlist[x].d+" Reward: "+egachievementlist[x].rp+"]")
      egachievementlist[x].a=True
      del unearnedeg[i]
      if egachievementlist[x].rt=="":
        pass
      continue
    i+=1
  if len(unearned)==0 and won==False:
    clear()
    print("Congratulations! You have just completed The Magicalus Casino! \nI bet you feel pretty satisfied right now, eh? \nI hope you do, because that satisfaction is all you get. Also, I have some good news! \nThere's more. Like, a lot more. \nGood luck!")
    input()
    clear()
    return True
  elif len(unearned)==0:
    return True
  return False
clear()
print("Hello, and welcome to the Magicalus Casino!\nYou've come to our casino with "+str(bal)+" bucks, and have entered our contest. \nFirst to achieve everything in our *extensive* list wins! \nWhat's the prize? Uhhhh... self satisfaction? Doesn't matter, just start spending. \nDon't worry: there's no penalty for going into crushing, crushing debt. \nIn fact, it's encouraged!(and necessary to win) \nSo have fun, and hit enter to start!\n(Note: this game runs in python, so all inputs require you to hit return)")
input()
while True:
  clear()
  won=achievecheck()
  print("Welcome to the Magicalus Casino Lobby!\nYou have "+str(bal)+" Magicalus bucks")
  print("Press 1 to hit the Slots\nPress 2 to play some Blackjack\nSay Achievements to see how you're doing.")
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
      slotnum=[0,1,2,3,4,5]
      weights=[1,13,10,7,4,2]
      i=0
      while i<=8:
        slotpos[i]=random.randint(1,5)
        i+=1
      winning=-1
      while True:
        if s1t>runtime:
          slotpos[3]=slotpos[0]
          slotpos[0]=slotpos[6]
          slotpos[6]=int(str(random.choices(slotnum,weights)[0
                         ]).replace("[",""). replace("]",""))
        if s2t>runtime:
          slotpos[4]=slotpos[1]
          slotpos[1]=slotpos[7]
          slotpos[7]=int(str(random.choices(slotnum,weights)[0]).replace("[",""). replace("]",""))
        if s3t>runtime:
          slotpos[5]=slotpos[2]
          slotpos[2]=slotpos[8]
          slotpos[8]=int(str(random.choices(slotnum,weights)[0]).replace("[",""). replace("]",""))
        print("╔═════╤═════╤═════╗\n║     |     |     ║\n║ ["+str(slotpos[6])+"] | ["+str(slotpos[7])+"] | ["+str(slotpos[8])+"] ║\n║     |     |     ║\n║     |     |     ║\n║ ["+str(slotpos[0])+"] | ["+str(slotpos[1])+"] | ["+str(slotpos[2])+"] ║\n║     |     |     ║\n║     |     |     ║\n║ ["+str(slotpos[3])+"] | ["+str(slotpos[4])+"] | ["+str(slotpos[5])+"] ║\n║     |     |     ║\n╚═════╧═════╧═════╝")
        time.sleep(0.075)
        if s3t>runtime:
          clear()
          runtime+=random.randint(1,2)
          continue
        break
      time.sleep(2)
      clear()
      slotwon=True
      if slotpos[6]==slotpos[0]==slotpos[3] or slotpos[7]==slotpos[1]==slotpos[4] or slotpos[8]==slotpos[2]==slotpos[5]: 
        wwcheck=True
      if slotpos[0]==slotpos[1]==slotpos[2] or slotpos[6]==slotpos[1]==slotpos[5] or slotpos[3]==slotpos[1]==slotpos[8]:
        winning=slotpos[1]
      elif slotpos[6]==slotpos[7]==slotpos[8]:
        winning=slotpos[7]
      elif slotpos[3]==slotpos[4]==slotpos[5]:
        winning=slotpos[4]
      else:
        slotwon=False
      if slotpos.count(0)>0:
        slot0check=1
        if winning==0:
          slot0check=2
      if (slotpos.count(0)+slotpos.count(1))==9:
        bincheck=True
      if all(x == slotpos[0] for x in slotpos):
        if slotpos[0]==0:
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
      ignoreinput()
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
      print("You have "+str(bal)+" Magicalus Bucks. There's no flat price, just betting.\nAll tables have 2 decks and 75% penetration, and dealers hit on 17.\nSay back at anytime to leave at the end of the hand.\nPress enter to play, or say back to go to the casino floor.")
      back=input()
      if back=="back"or back=="Back":
        break
      clear()
      cards=doubdc[:]
      while True:
        handval=0
        chandval=0
        if done==True:
          break
        print("You have "+str(bal)+" Magicalus bucks")
        print("How much would you like to bet on this hand? \nYou can press enter to use the regular bet, which is currently "+str(bjreg)+". \nYou can change the regular bet by putting an r after your bet. \nSay stand to take no more cards and end the hand.")
        while True:
          drawn=[False,False]
          acemods=0
          cacemods=0  
          try:
            bet=input()
            if bet=="":
              bet=bjreg
            if "r" in str(bet):
              bet=int(bet.replace("r",""))
              if bet>0:
                bjreg=bet
                print("Your new regular bet is "+str(bet))
            else:
              bet=int(bet)
            if int(bet)<=0:
              print("Your bet cannot be negative")
              continue
            elif -50<=bal<=50 and int(bet)>100:
              print("Your bet cannot be more then 100 when near 0 Magicalus Bucks.")
              continue
            elif -50<=bal<=50 and int(bet)<=100:
              break
            elif int(bet)>math.floor(bal*-0.8) and bal<0:
              print("While in debt, you cannot bet more then 80% of your current debt at once.")
              continue
            elif int(bet)<math.floor(bal*-0.8) and bal<0:
              break
            elif int(bet)>bal*2:
              print("Your bet cannot be more then twice your balance.")
              continue
            break
          except ValueError:
            if bet=="back" or bet=="Back":
              done=True
              break
            print("Please input a valid integer")
        if done==True:
          break
        clear()
        print("Your current bet is: "+str(bet),end="\n\n")
        print("The house's cards are:")
        cdraw1=drawcard()
        if cdraw1[2]==1:
          chandval+=11
          cacemods+=1
        elif cdraw1[2]<=10:
          chandval+=cdraw1[2]
        else:
          chandval+=10
        print(cdraw1[0]+cdraw1[1])
        cdraw2=drawcard()
        if cdraw2[2]==1:
          chandval+=11
          cacemods+=1
        elif cdraw2[2]<=10:
          chandval+=cdraw2[2]
        else:
          chandval+=10
        if chandval>21:
          cacemods-=1
          chandval-=10
        print("Hidden Card\n")
        print("Your cards are:")
        initdraw1=drawcard()
        if initdraw1[2]==1:
          handval+=11
          acemods+=1
        elif initdraw1[2]<=10:
          handval+=initdraw1[2]
        else:
          handval+=10
        print(initdraw1[0]+initdraw1[1])
        initdraw2=drawcard()
        if initdraw2[2]==1:
          handval+=11
          acemods+=1
        elif initdraw2[2]<=10:
          handval+=initdraw2[2]
        else:
          handval+=10
        print(initdraw2[0]+initdraw2[1])
        if handval>21:
          acemods-=1
          handval-=10
        elif handval==21:
          print("You got a natural blackjack!")
        else:
          while True:
            if drawn[0]!=False:
              print(drawn[0]+drawn[1])
              if drawn[2]==1:
                handval+=11
                acemods+=1
              elif drawn[2]<=10:
                handval+=drawn[2]
              else:
                handval+=10
              if handval>21 and acemods>0:
                acemods-=1
                handval-=10
              elif handval>21 or handval==21:
                break
            play=input()
            if play=="back" or play=="Back":
              done=True
              play=input()
            if play=="stand" or play=="Stand":
              break
            cards=shuffle()
            drawn=drawcard()
        while chandval<=17 and handval<=21:
          cdraw=drawcard()
          chandval+=cdraw[2]
          if cdraw2[2]==1:
            chandval+=11
            cacemods+=1
          elif cdraw2[2]<=10:
            chandval+=cdraw2[2]
          else:
            chandval+=10
        if handval==21:
          print("You got a blackjack!")
        if handval<=21 and chandval>21:
          bal+=math.floor(bet/2)
          print("The casino busted and you won "+str(bet)+" Magicalus Bucks!")
        elif handval>21 and chandval<=21:
          bal-=int(bet)
          print("You busted and lost "+str(bet)+" Magicalus Bucks.")
        elif chandval<handval:
          bal+=math.floor(int(bet)/2)
          print("You beat the casino "+str(handval)+" to "+str(chandval)+", and you won "+str(bet)+" Magicalus Bucks!")
        elif chandval>handval:
          bal-=int(bet) 
          print("The casino beat you "+str(chandval)+" to "+str(handval)+", and you lost "+str(bet)+" Magicalus Bucks.")
        else:
          print("You tied the house and get your money back.")
        input()
        clear()
  elif nav=="Achievements" or nav=="achievements":
    clear()
    i=0
    while i<len(achievementlist):
      if achievementlist[i].a==True:
        print("- "+achievementlist[i].n+": "+achievementlist[i].d+" Reward: "+achievementlist[i].rp+" [✓]")
      else:
        print("- "+achievementlist[i].n+": ??? Reward: ??? [X]")
      i+=1
    i=0
    while i<len(egachievementlist):
      if egachievementlist[i].a==True:
        print("- "+egachievementlist[i].n+": "+egachievementlist[i].d+" Reward: "+egachievementlist[i].rp+" [✓]")
      elif won==True:
        print("- "+egachievementlist[i].n,end=": ")
        print(" ??? ",end="")
        print("Reward: ??? [X]")
      i+=1
    input()
  elif nav=="magicalus" or nav=="Magicalus":
    awfcheck=True
    continue
  else:
    clear()
    print("Theres nothing here. Hit enter to go back.")
    input()
    continue