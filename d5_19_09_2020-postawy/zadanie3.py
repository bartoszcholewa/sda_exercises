def sklejacz(**kwargs):
    ret = ""
    for key, value in kwargs.items():
        ret += f"Klucz: {key}, wartosc: {value}\n"
    return ret

print(sklejacz(klej="do spodni", zielone="wschody slonca"))