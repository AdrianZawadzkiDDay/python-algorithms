
def funkcja():
    notReady = True;
    while notReady:
        try:
            a = int(input("Proszę wprowadzić liczbę: "))
            notReady = False
        except ValueError:
            print("to nie  poprawna liczba")

    return a;

liczba = funkcja()
print("Wybrana liczba: ", liczba)