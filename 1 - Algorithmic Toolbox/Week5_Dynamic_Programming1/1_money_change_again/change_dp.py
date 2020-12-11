# Pierce Lovesee
# December 11th, 2020

import sys

def get_change(money, coinsList):

    # creating an empty array to hold up to money elements
    mincoins = [0] * (money + 1)

    # iterate through all icrimental values up to money
    # saving the result; starting at index 1, because the
    # base case, m = 0, is already defined, 0 coins needed
    for m in range(1, money + 1):
        # fill with infinite value (something that will never be reached)
        mincoins[m] = money +  10
        # then for each incrimental value, iterate through the mincoins
        # find the coin that minimizes the needed coins based on the
        # previous incremental coins needed values
        # i.e. minimize mincoins[m - coin(i)] + 1
        for coin in coinsList:
            # the index of the min coins array represents the incremental
            # amount of money that needs to be solved for
            # so compare the index m to the value of each coin to see
            # if that coin can be taken out of the total
            if m >= coin:
                # if it can, then store the number of coins it takes to
                # change the index value at mincoins[m - coin] and + 1
                # and store, try for all coins, and take the minimum value
                # for how many coins it takes to change m, store in array
                numcoins = mincoins[m - coin] + 1
                if numcoins < mincoins[m]:
                    mincoins[m] = numcoins

    # after each incrimental value up to money is determined, then the minimum
    # number of coins needed to change money will be stored in mincoins[money]
    return mincoins[money]

if __name__ == '__main__':

    money = int(sys.stdin.read()) # input for amount of change needed
    coins = [1, 3, 4]  # denominations of coins available for this example
    assert 1 <= money <= 10**3 # assertion based on grader
    print(get_change(money, coins))
