from art import *
from morse import morse_it, de_morse_it

morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-",
  ":":"---...",
  ";":"-.-.-.",
  "'":".----.",
  "&":".--...",
  "_":"..--.-",
  "=":"-...-",
  "+":".-.-.",
  "-":"-....-",
  "/":"-..-.",
  '"':'.-..-.',
  "$":"...-..-",
  " ":"    ",
}

def main():
  print('[1]: Encode\n[2]: Decode\n[3]: Quit')
  dec = input('> ').lower().strip()
  
  if dec == '1' or dec == 'encode':
    code = morse_it(input('\nEnter the sentence\n> '), morse_code) 
    print('Encoded Morse:\n\n' + code + '\n')
    return True 
  elif dec == '2' or dec == 'decode':
    sent = de_morse_it(input('\nEnter the code\n> '), morse_code) 
    print('Decoded Sentence:\n\n' + sent + '\n')
    return True
  elif dec == '3' or dec == 'quit' or dec == 'exit' or dec == 'die': 
    print('Quitting.....')
    return False 
  else: 
    print('Invalid Input!')
    return True 

title = text2art("Morse", font='cybermedum', chr_ignore=True) 
print(title)
  

running = True 
while running: 
  running = main()
print('Program successfully terminated!')
print(text2art("The End", font='cybermedum', chr_ignore=True))
