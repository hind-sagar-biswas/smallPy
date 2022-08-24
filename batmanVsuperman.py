'''
  -> BATMAN Vs. SUPERMAN <-
         version: 1.0
                        
AUTHOR: Hind Sagar Biswas
Date: September 24th, 2020
Email: hindsbhk@gmail.com

'''


#imports
import random
import time

game_on = True
playing = True
none_zero = True

player = ""
computer = "BATMAN"

chosen_move = 1
primary_dmg = 0
final_dmg = 0
bat_life = 200
armour = 60
sup_life = 300
heal = 40


#divider========>
def divide ():
    print ("========================")

#getting input=======>
def get_input():
    global player
    global computer
    w = True
    while w:
        choose = input("©hoose your hero (Batman/Superman)\n>>> ").upper()
        if choose == "BATMAN" or choose == "SUPERMAN":
            player = choose
            if choose == "BATMAN":
                computer = "SUPERMAN"
            else:
                computer = computer
            w = False
            time.sleep(0.5)
            divide()
            print ("Loading.....")
            divide ()
            time.sleep(1)
            print ('')
            divide()
            print ("You have chosen: " + player)
            print ("Computer will play with: " + computer)
            divide()
        else:
            print ("Invalid input! Choose again!")
        

#powers print=======>
def bat_powers():
    print ("[1] Batarang;\n[2] Kryptonite Granade\n[3] Spear\n")
def sup_powers():
    print ("[1] Fists;\n[2] Laser Beam\n[3] Sun Heal")

#show powers=======>
def show():
  global game_on
  print ("Loading... Please wait....")
  time.sleep(1)
  divide()
  print ("LIFES and POWERS:\n\n BATMAN:\n  Life: 200; Armour: 60\n  Powers:")
  print ("[1] Batarang;\n[2] Kryptonite Granade\n[3] Spear\n   SPECIAL ABILITY: Dodge\n")
  print (" SUPERMAN:\n  Life: 300; Armour: Null\n  Powers:")
  print ("[1] Fists;\n[2] Laser Beam\n[3] Sun Heal\n   SPECIAL ABILITY: Steel Body (i.e. 25% less damage when not vulnerable)\n   WEAKNESS: Occasionally gets Vulnarable!")
  p = input("\nContinue? (Y/N)\n>>> ").upper()
  if p == "Y":
      divide ()
      print ("\nWait... Loading.....")
      time.sleep(1)
      print ("Starting Game....")
      divide ()
      time.sleep(0.5)
  else:
      divide ()
      print ("Game Ended!")
      divide ()
      game_on = False
      
#ask for turn========>
def ask_turn(plr):
      global chosen_move
      print ("Available Attacks:")
      if plr == "B":
          bat_powers()
      else:
          sup_powers()
      illegal = True
      while illegal:
          g = input("Choose an attack: ")
          if g == "1" or g == "2" or g == "3":
              chosen_move = int(g)
              illegal = False
          else:
              print ("Illegal Move! Choose Move Again")
              illegal = True
      
#primary damage calculation====>
def set_pd(m, p):
    global primary_dmg
    global heal
    if p == "B":
        if m == 1:
            primary_dmg = 15
        elif m == 2:
            primary_dmg = 25
        else :
            primary_dmg = 75
    else:
        if m == 1:
            primary_dmg = 15
        elif m == 2:
            primary_dmg = 25
        else :
            primary_dmg = 0
            heal = 40

#final damage calculation=====>
def set_fdb(pd):
    global final_dmg
    global sup_life
    #check if vulnarable>
    l = [True, False, False, True, False, True]
    vulnarable = l[random.randint(1,6)-1]
    if vulnarable and pd != 75:
        print ("Wow! Superman got Vulnerable!")
        if pd == 15:
            final_dmg = pd*2
        else:
            final_dmg = pd + 10
    else :
        dp = round(pd - 0.25*pd)
        if pd == 75:
            sd = [True, True, False, True, False, True, False, True, True, False]
            s = sd[random.randint(1,10)-1]
            if s:
                print ("Incredible! Spear hitted at Target...")
                final_dmg = dp
            else:
                print ("Oops! Spear missed!!!")
                final_dmg = 0
        else:
            final_dmg = dp
    print ("Damage delt: " + str(final_dmg))
    sup_life -= final_dmg
    divide ()
    time.sleep(1)

def set_fds(pd):
    global final_dmg
    global bat_life
    global sup_life
    global armour
    global heal
    a = [True, True, False, True, False, True]
    b = [False, True, False, True, False, False, True, False, True, False ]
    a_hit = a[random.randint(1,6)-1]
    dodged = b[random.randint(1,8)-1]
    if dodged:
        print ("Batman Doged the Attack!!!")
        final_dmg = 0
    elif a_hit and dodged == False:
        print ("The attack hitted armour!")
        if armour > 0:
            print ("Armour absorbed 15 shots and repelled 5 shot")
            armour -= 15
            h = pd-20
            if h > 0:
                final_dmg = h
            else:
                print ("Armour absorbed all!!!")
                final_dmg = 0
        else:
            print ("Alas for BATMAN!!!\nThe armour is damaged!! it can't save him!")
            final_dmg = pd
    else:
        print ("Direct Hit!!! Didn't hitted armour!")
        final_dmg = pd
    print ("Damage delt: " + str(final_dmg))
    bat_life -= final_dmg
    divide ()
    time.sleep(1)


#echo current situation===>
def curr_st(d):
    global bat_life
    global sup_life
    global armour
    time.sleep(0.2)
    print ("BATMAN: " + str(bat_life) + " Armour: " + str(armour))
    print ("SUPERMAN: " + str(sup_life))
    divide ()
    print ("")
    
#check for win=====>
def check_win(x, y):
    global player
    global computer
    global none_zero
    if x < 1 or y < 1:
        none_zero = False
    else :
        none_zero = True

# Match if player = Batman ======>
def bat_match():
      ask_turn("B")
      set_pd(chosen_move, "B")
      set_fdb(primary_dmg)
      curr_st(final_dmg)
      check_win(bat_life, sup_life)
      time.sleep(1)

# Match if player = Superman ======>
def sup_match():
      global heal
      global sup_life
      ask_turn("S")
      if chosen_move == 3:
          print("H..E..A..L..I..N..G.......")
          time.sleep(1.3)
          sup_life += heal
      else:
          set_pd(chosen_move, "S")
          set_fds(primary_dmg)
      curr_st(final_dmg)
      check_win(bat_life, sup_life)
      time.sleep(1)
      
#Computer match=======>
def sup_com():
    global sup_life
    global bat_life
    divide()
    print ("\nSuperman's Turn......\n")
    sup_powers()
    divide()
    time.sleep(1.5)
    t = [0,1,2,0,1,2,0,1,2,0,1,0]
    turn = t[random.randint(1,12)-1]
    
    if turn == 2:
        print ("Superman healed himself!")
        sup_life += 40
    else:
        if turn == 0:
            print ("Superman chose: Fists")
        elif turn == 1:
            print ("Superman chose: Laser")
        time.sleep(1)
        set_pd(turn+1, "S")
        set_fds(primary_dmg)
    curr_st(final_dmg)
    check_win(bat_life, sup_life)
    
def bat_com():
    global bat_life
    global sup_life
    divide()
    print ("\nBatman's Turn......\n")
    bat_powers()
    divide()
    time.sleep(1.5)
    turn = random.randint(1,3)-1
    if turn == 0:
        print ("Batman chose: Batarang")
    elif turn == 1:
        print ("Batman chose: Kryptonite Granade")
    else:
        print ("Batman chose: Spear")
    time.sleep(1)
    set_pd(turn+1, "B")
    set_fdb(primary_dmg)
    curr_st(final_dmg)
    check_win(bat_life, sup_life)
    
 
#Select Match===========>
def select_match(plr):
  global none_zero
  while none_zero:
    if plr == "BATMAN":
        bat_match()
        if none_zero:
            sup_com()
        else:
            divide ()
            
    else:
       sup_match()
       if none_zero:
            bat_com()
       else:
            divide ()
            
            
#results ===========>
def results (p):
       global sup_life
       global bat_life
       global game_on
       if p == "SUPERMAN":
           if sup_life < 1:
               print ("Alas!! SUPERMAN lost!!")
               print ("You have Lost!!!")
               divide ()
           else:
               print ("COÑGRATS!!!")
               print ("Batman lost!!!")
               print ("You have won.........")
       else:
           if bat_life < 0:
               print ("Alas!! BATMAN lost!!")
               print ("You have Lost!!!")
               divide ()
           else:
               print ("COÑGRATS!!!")
               print ("Superman lost!!!")
               print ("You have won.........")
       game_on = False
       divide ()
       divide ()
       print ("Next part is coming soon........")


def restart ():
       global game_on
       global playing
       k = input("Want to Restart?\n>>> "). lower()    
       if k == "y":
           playing = True
           game_on = True
           divide ()
           print("Restarting.....Wait......")
           divide ()
           divide()
           time.sleep(1.5)
       else :
           playing = False
           game_on = False
           divide ()
           print ("Game Over!")
           print ("Thanks for playing....")
           divide ()
           print ("AUTHOR: Hind Sagar Biswas")
           print ("Email: hindsbhk@gmail.com")
           divide()
           time.sleep(1.5)
           print ("GOOD BYE")
       
while playing:
    while game_on:
        show()
        get_input()
        select_match(player)
        divide ()
        divide ()
        results (player)
    restart()
