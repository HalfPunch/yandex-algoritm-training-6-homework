from random import randint

TESTS_AMOUNT = 20
NUMBERS_AMOUNT = 10

if __name__ == "__main__":
    print(TESTS_AMOUNT)
    for i in range(TESTS_AMOUNT):
        new_line = [str(NUMBERS_AMOUNT)]
        for j in range(NUMBERS_AMOUNT):
            new_line.append(str(randint(-100, 100)))
        print(" ".join(new_line))
