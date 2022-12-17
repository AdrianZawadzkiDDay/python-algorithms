
def funkcja():
    notReady = True;
    while notReady:
        try:
            a = int(input("Proszę wprowadzić liczbę: "))
            notReady = False
        except ValueError:
            print("to nie  poprawna liczba")

    return a;

def funkcja2(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("to nie  poprawna liczba")

liczba = funkcja2("Podaj a -> ")
print("Wybrana liczba: ", liczba)