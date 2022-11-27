# 🚨 Don't change the code below 👇
taille_str = input("enter your height in m: ")
poids_str = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
taille_float = float(taille_str)
poids_float = float(poids_str)
IMC = int(poids_float / pow(taille_float, 2))
print(f"Votre IMC est de {IMC}")