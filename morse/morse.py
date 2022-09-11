## Morse code encoder
def morse_it(string, code_list): 
  code = ""
  string = string.lower()
  for char in string: 
    code += code_list[char]
    if char != " ": code += "   "
  return code

## Morse code decoder
def de_morse_it(code, code_list):
  string = ""
  code = '   .......   '.join(code.split('       ')).split('   ')
  
  for code_frag in code:
    if code_frag == ".......": 
      string += " " 
    else: 
      for char, morse in code_list.items(): 
        if code_frag == morse: 
          string += char
  return string