#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# On acceuill les gens comme il se doit
print("Welcome to the tip calculator")
# On pose les questions essentielles
bill = float(input("What was the total bill ? $"))
tip = int(input("How much tip do you like to give ? 10, 12 or 15 ? "))
people = int(input("how many people to split the bill ? "))
# On commence le calcul avec les pourcentages
tip_as_percent = tip / 100
# montant total du pourboire
total_tip_amount = bill * tip_as_percent
# Montant total facture + pourboire
total_bill = bill + total_tip_amount
# On divise par le nombres de convives
bill_per_person = total_bill / people
# On arrondit le montant a 2 chiffres après la virgule
final_amount = round(bill_per_person, 2)
# Comme on a qu'un seul chiffre et que ca fait moche
# on formate le resultat pour avoir 2 chiffres après la virgule
final_amount = "{:.2f}".format(bill_per_person)
# On affiche le résulta final
print(f"Each persone should pay ${final_amount}")