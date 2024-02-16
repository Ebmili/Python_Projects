print("Thank you for choosing Python Pizza Deliveries")
size = input()
add_peperoni = input() 
extra_cheese = input()


bill = 0 
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 5

if extra_cheese == "Y":
  bill += 1

print(f"Your final bil is: ${bill}")