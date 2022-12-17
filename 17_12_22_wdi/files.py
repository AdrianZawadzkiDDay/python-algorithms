
def wiersz():
    with open("text.txt") as infile:
       return infile.read()


def statistic(a):
    tekst = wiersz();
    wystapienia = 0;
    for i in range(len(tekst)):
        if tekst[i] == a:
            wystapienia += 1
    return wystapienia;


print("Statystyka wiersza")

litera = "g"
wystapienia = statistic(litera)
print(wystapienia)
print("Wysatąpienia w wierszu litery " + litera +" wynosi: " + str(wystapienia))


# print(test("test", "t"))
# print(tekst)

# tekst = wiersz()

# f=open("text.txt")
# print(f.read())
#
# f.close()

def test(test, t):
    wystapienia = 0;
    for i in range(len(test)):
        if test[i] == t:
            wystapienia +=1
        print(test[i])
    return wystapienia;