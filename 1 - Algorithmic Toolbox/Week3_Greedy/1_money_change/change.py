# Uses python3
import sys


def money_change(money):
    assert 0 <= money <= 10 ** 3
    number_of_coins = 0
    while money > 0:
        if(money >= 10):
            money -= 10
            number_of_coins += 1
        elif(money >= 5):
            money -= 5
            number_of_coins += 1
        elif(money > 0):
            money -= 1
            number_of_coins += 1
    return number_of_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(money_change(m))
