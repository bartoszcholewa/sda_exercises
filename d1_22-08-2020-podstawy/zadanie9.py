a = input("Podaj input:")
counter = 0

for znak in a.lower():
    if znak == 'a':
        counter+=1
print(f"Ilosc znakow 'a' w {a}: {counter}")


#fstring = f"FString ze zmiennej {a}"
#print(fstring)