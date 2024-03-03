def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name("Billie")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What it like in {location}")

greet_with("Emilia", "Warsaw")

# or greet_with(location="London", name="Angela")

import math

def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(heieght=test_h, width=test_w, cover=coverage)


def prime_checker(number):
  is_prime = True

n = int(input())
prime_checker(number=n)

