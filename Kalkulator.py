def dodaj(a, b):
    return a + b

def odejmi(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Nie można dzielić przez zero!"

def kalkulator():
    print("-------kalkulator-------")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    try:
        choice = int(input("Wpisz numer operacji (1-4): "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))

            if choice == 1:
                print(f"Wynik: {dodaj(num1, num2)}")
            elif choice == 2:
                print(f"Wynik: {odejmi(num1, num2)}")
            elif choice == 3:
                print(f"Wynik: {pomnoz(num1, num2)}")
            elif choice == 4:
                print(f"Wynik: {podziel(num1, num2)}")
        else:
            print("Nieprawidłowy wybór operacji.")
    except ValueError:
        print("Błąd: Wprowadź poprawną liczbę.")



if __name__ == "__main__":
    kalkulator()
