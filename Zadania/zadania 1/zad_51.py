import math
def calculate_c_len(a_len, b_len):
    return math.sqrt(math.pow(a_len, 2) + math.pow(b_len, 2))

a = float(input("Jaka jest dl. boku a? "))
b = float(input("Jaka jest dl. boku b? "))

c = calculate_c_len(a, b)
print(f"Długość przeciwprostokatnej to {c}")