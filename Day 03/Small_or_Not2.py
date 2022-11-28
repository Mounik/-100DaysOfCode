# 🚨 Don't change the code below 👇
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ? "))
    if age <= 12:
        print("Please pay $5.")
    elif age >= 18:
        print("Please pay $12.")
    else:
        print("Please pay $7")
else:
    print("Sorry, you have to grow taller before you can ride.")
