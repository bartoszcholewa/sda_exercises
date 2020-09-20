import random
import smtplib
class User(object):
    def __init__(self, log, em, pas, db):
        self.login = log
        self.email = em
        self.password = pas
        self.baza_danych = db
        self.baza_danych.dodaj(self)
        self.id = random.randint(1000000, 9999999)

    def wyslij_wiadomosc(self, login="defaultuser@firma.pl", tresc='Default Content'):
        self.odbiorca = self.baza_danych.email_uzytkownika(login)
        self.nadawca = 'noreply@firma.pl'
        self.temat = 'Twoje konto zostalo zalozone'
        self.tresc_podczas_rejestracji = tresc
        self.tresc = 'Witaj ' + self.odbiorca + ', Twoje konto zostalo zalozone poprawnie,\nDziekujemy za rejestracje!\n'
        self.tresc += self.tresc_podczas_rejestracji + '\n'
        self.tresc += f"Best regards\n" + self.baza_danych.login_uzytkownika(login)

        ret = (f"[Odbiorca]: {self.odbiorca}\n"
              f"[Nadawca]: {self.nadawca}\n"
              f"[Temat]: {self.temat}\n"
              f"[Tresc]: {self.tresc}\n")
        return ret

class BazaDanych(object):
    def __init__(self):
        self.kolekcja = dict()
    def dodaj(self, user):
        self.kolekcja[user.login] = user
    def email_uzytkownika(self, user):
        return self.kolekcja[user.login].email
    def login_uzytkownika(self, user):
        return self.kolekcja[user.login].login

print("== REJESTRACJA NOWEGO UZYTKOWNIKA ==")
input_login = input('Podaj login: ')
input_email = input('Podaj Email: ')
input_password = input('Podaj Haslo: ')
input_msg = input('Tresc Wiadomosci: ')

nowa_baza = BazaDanych()

nowy_uzytkownik = User(input_login, input_email, input_password, nowa_baza)

nowy_uzytkownik.wyslij_wiadomosc(nowy_uzytkownik, input_msg)

print("WIADOMOSC WYSLANA")
