# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# On fait le calcul de l'imc
imc = round(weight / height ** 2)
# On transforme le résultat en integer

# On affiche le résultat en comparant les valeurs
if imc < 18.5:
    print(f"Your BMI is {imc}, you are underweight.")
elif imc < 25:
    print(f"Your BMI is {imc}, you have a normal weight.")
elif imc < 30:
    print(f"Your BMI is {imc}, you are slightly overweight.")
elif imc < 35:
    print(f"Your BMI is {imc}, you are obese.")
else:
    print(f"Your BMI is {imc}, you are clinically obese.")
