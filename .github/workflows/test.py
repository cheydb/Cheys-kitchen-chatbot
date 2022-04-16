print("Hello, welcome to Chey's Kitchen!")
name = input("What is your name?\n")

#if name == "Bob":
#  evil_status = input("Are you evil?\n")
#  if evil_status == "Yes":
#    print("You're not welcome here, Evil Bob!")
#    exit()
#  else:
#    print("Great!")
#else:
print("Hello, " + name + "! It's nice to see you")
    
menu = "burgers, chips, pizza, and milkshake,"

order = input(print("\n What can I get you? Today's specials are " + menu))

print("okay, your " + order + " is coming right up")

if order == "burger":
  price = 20
elif order == "chips":
  price = 10
elif order == "pizza":
  price = 25
elif order == "milkshake":
  price = 10

num = input(print("how many would you like? "))

total = price * int(num)
   
print("Okay, your total is R" + str(total))
