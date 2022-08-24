riddle = "\033[1m#Riddle:\n--------\033[0m\n\"If you have one, you don\'t share it, if you share it you don\'t have it. What is it?\" \033[34m[source: google assistant]\033[0m\n\nYou have\033[32m 3 \033[0mchances!!!\n"
guess = ""
count = 0
limit = 3
lost = False

print (riddle)

s = "t@e$rc-+e&s"
v=['!','@','#','$','%','&','<','>','/','*',';',':','+','-','1','2','3','4','5','6','7','8','9','0','=','^','`','(',')','~']
for i in v:
    s= s.replace(i,'')
a = s[::-1]

while guess != a and not(lost):
  if count < limit:
   if count > 0:
     print(f'\033[31m!WRONG ANSWER!\033[0m\nRemaining Tries:\033[92m {limit-count}\033[0m!\n\n---------Retry----------')
   guess = input("\033[93mEnter your answer: \033[0m")
   guess = guess.lower()
   count += 1
  else:
   lost = True 
   
if lost:
 print ("\033[31m of Chances! You LOST!!\033[0m")
else:
 print ("\033[32mCongratulations! You have WON!!!\033[0m\n")
