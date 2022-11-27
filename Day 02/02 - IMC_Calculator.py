# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# On fait le calcul de l'IMC
IMC = float(weight) / float(height) ** 2
# On transforme le résultat en integer
IMC_int = round(IMC, 2)
# On affiche le résultat
print(f"Votre IMC est de {IMC_int}")
