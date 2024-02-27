target = 100

##doesn't include fulll but adds one

for number in range(1, target +1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)