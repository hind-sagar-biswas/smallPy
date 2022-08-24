#FIZZBUZZ <Ex-09>
def fizz_buzz():
  num =  int(input("Enter a number: "))
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')

#MULT TABLE <Ex-14>
def create_table():
  num = int(input('Enter the number: '))
  print(f'Table for {num}:\n')
  for i in range(10):
    print(f'> {num} × {i+1} = {num*(i+1)}')

#CALCULATOR
def calculator():
  num1 = int(input('Enter 1st number (X): '))
  num2 = int(input('Enter 2nd number (Y): '))
  
  print('\nEnter operator:\n\tadd = X + Y\n\tsub = X - Y\n\tmul = X × Y\n\tdiv = X ÷ Y\n\trem = X ÷ Y \'s reminder\n\texp = X ^ Y\n')
  
  op = input('>> ')
  sol = 0

  if op == 'and':
    sol = num1 + num2
  elif op == 'sub':
    sol = num1 - num2
  elif op == 'mul':
    sol = num1 * num2
  elif op == 'div':
    sol = num1 / num2
  elif op == 'rem':
    sol = num1 % num2
  elif op == 'exp':
    sol = pow(num1, num2)
  else:
    sol = 'ERROR: Invalid Operator!'

  print(f'\nSolution: {sol}')

#CELCIUS TO FAHRENHEIT CONVERTER
def cf_converter():
  print("Result is: " + str(1.8 * int(input('Enter temperature in Celcius: ')) + 32) + "°F")

#EMAIL FILTER
def email_filter():
  forbidden = ['\'', '\"', '#', ',', ';', ':', '&', '\\', '$', ' ']
  email = input("Enter your email address: ").lower()
  output = ""

  email = email.split('@')
  
  email[-1] = email[-1].split('.')
  email[-1][-1] = '.' + email[-1][-1]
  email[-1] = ''.join(email[-1])
  
  email[-1] = '@' + email[-1]
  email = ''.join(email)    
    
  for char in email:
    if char not in forbidden:
      output += char

  print(output)
