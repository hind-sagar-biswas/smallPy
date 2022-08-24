import functions as f

running = True
list = """\033[32m
no.	| name
----|----------------------------------
    |
00  | HELP
0   | EXIT
1   | FIZZBUZZ
2   | MULTIPLICATION TABLE
3   | CALCULATOR
4   | CELCIUS TO FAHRENHEIT CONVERTER
5   | EMAIL FILTER
____|_________________________________\033[0m
"""
print(list)

while running:
  app = input('\033[34mEnter application no:\033[0m ')

  if app == '00':
    print('\033[1mHELP\033[0m')
    print(list)
  elif app == '1':
    f.fizz_buzz()
  elif app == '2':
    f.create_table()
  elif app == '3':
    f.calculator()
  elif app == '4':
    f.cf_converter()
  elif app == '5':
    f.email_filter()
  elif app == "0":
    running = False
    print('Exiting Programme....')
    print('\033[31mProgramm Ended Successfully!\033[0m')
  else:
    print(f'\033[31mERROR: Couldn’t find application no. {app}!\033[0m\nRequesting for retry....')

  if input('Re-run Programme? [Y/n]\n> ').lower() != 'y':
    running = False
    print('Exiting Programme....')
    print('\033[31mProgramm Ended Successfully!\033[0m')
