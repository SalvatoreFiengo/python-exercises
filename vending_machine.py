    
from byotest import *

usd_coins = [100, 50, 25, 10, 5, 2, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

def dict_from_list(myList, key=0, keyValue=0):
    """
    get dictionary from a list.
    update a key if needed
    """
    dictionary={}
    for item in myList:
        dictionary.update({item:20})
        if key != 0:
            dictionary.update({key:keyValue})

    return dictionary

def get_change(amount, coins=eur_coins):
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)
    Returns a list of coin values
    """
    change = []
    current_coins_available = dict_from_list(coins, 2, 1)
    
    for coin in sorted(current_coins_available, reverse=True):
        print(current_coins_available)
        while coin <= amount:
            if current_coins_available[coin]>0:
                print("{0} is {1}".format(coin,current_coins_available[coin]))
                current_coins = current_coins_available[coin]
                amount -= coin
                change.append(coin)
                current_coins -=1
                current_coins_available.update({coin:current_coins})
            else:
                print("coins of %s are not available" % coin)
                break
    return change


#  Write our tests for our code
test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 1,1])
test_are_equal(get_change(35, usd_coins), [25, 10])
test_are_equal(get_change(30), [20,10])


print("All tests pass!")
print(get_change(9))

