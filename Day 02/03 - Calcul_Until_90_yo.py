# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Conversion en integer
age_as_int = int(age)
# Calcul des années restantes
years_remaining = 90 - age_as_int
# Calcul du temps restant en jours, semaines et mois
days_remaining = years_remaining * 365
week_remaining = years_remaining * 52
month_remaining = years_remaining * 12
# Affichage du resultat en f-String
message = f"You have {days_remaining} days, {week_remaining} weeks, and {month_remaining} months before 90 years old"
print(message)