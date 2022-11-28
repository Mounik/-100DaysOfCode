# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# On fait le calcul de l'imc
imc = round(weight / height ** 2)
# On affiche le résultat
print(f"Votre IMC est de {imc}")
