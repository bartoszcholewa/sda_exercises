def get_reward(times:int) -> None:
    """
    Na podstawie ilosci losowan uzytkownika wybiera rodzaj nagrody
    :param times:
    :return:
    """
    if times <= 10:
        print("Gratulacje, wygrałeś samochód!")
    elif 10 < times <= 25:
        print("Gratulacje, wygrałeś wycieczke!")
    elif 25 < times <= 50:
        print("Gratulacje, wygrałeś nagrode pocieszenia!")
    else:
        print("Niestety, moze nastepnym razem Ci sie poszczesci...")