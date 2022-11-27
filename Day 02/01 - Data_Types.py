# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# On récupère les chiffres un par un et on les transforme en integer
one = int(two_digit_number[0])
two = int(two_digit_number[1])
# On affiche l'opération complète pour la forme et pour s'entrainer au f-string
print(f"{one} + {two} = {one + two}")
# On affiche le résultat
print(one + two)
