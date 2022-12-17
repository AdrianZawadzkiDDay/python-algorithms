
def armstrong(a):
    for i in range(10, a):
        stringNumber = str(i)
        length = len(stringNumber)
        result = 0

        for a in range(length):
            number = int(stringNumber[a])
            result += number**length

        if i == result:
            print(i)


def armstrong2(a):
    for i in range(100, a):
        length = len(str(i))
        power = int(length)
        result = 0
        number = i
        while number > 0:
            digit = number % 10
            result += pow(digit, power)
            number //= 10 # np 153 3**3 5**3 1**3

        if i == result:
            print(i)


armstrong(1000)
print("------")
armstrong2(1000)

