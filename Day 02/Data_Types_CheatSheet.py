#Data Types

# String

print("Hello"[-1])
print("123" + "345")

# Integer

print(123 + 345)
print(1_269_035)

# Float

print(3.14159)

# Boolean

True
False

# Conversion
# On stocke le nom de l'utilisateur
num_char = len(input("What is your name?\n"))
# On le converti en string
new_num_char = str(num_char)
# On imprime le résultat
print(f"Your name has {new_num_char} characters.")

# Plus rapide le f-string
num_char = len(input("What is your name?\n"))
print(f"Your name has {num_char} characters.")