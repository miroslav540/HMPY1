def InputNumbers(inputText):
    all_fine = False
    while not all_fine:
        try:
            number = int(input(f"{inputText}"))
            all_fine = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print("в неделе всего 7 дней =)")


num = InputNumbers("Введите число: ")
checkNumber(num)