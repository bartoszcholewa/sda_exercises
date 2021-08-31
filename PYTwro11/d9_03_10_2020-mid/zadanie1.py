""" Continue and brake example"""

for i in range(10):
    if i == 9:
        print("Koniec")
        break
    if i % 2 == 0:
        print(i)
    continue