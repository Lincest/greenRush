# coding=utf-8
import random

if __name__ == '__main__':

    randDate = random.randint(0,365)
    with open("./date", "w", encoding="utf-8") as f:
        f.write(str(randDate))

    date = ""
    with open("./runtimes", "r", encoding="utf-8") as f:
        date = f.read()

    date = str(int(date) + 1)
    with open("./runtimes", "w", encoding="utf-8") as f:
        f.write(date)

