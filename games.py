import random
import emoji
import sys
sys.stdout.reconfigure(encoding="utf-8")


symbols = {
    ":growing_heart:": 1,
    ":glowing_star:": 2,
    ":ghost:": 3,
    ":eye:": 4,
    ":ribbon:": 5,
    ":trophy:": 6,
}

def getSymbol():
    choice = random.choice(list(symbols.keys()))
    symbol = emoji.emojize(choice)
    value = symbols[choice]
    return symbol, value

def match(result):
    return len(set(result))

def playSlots():

    result = []
    prize = 0

    for i in range (3):

        symbol, value = getSymbol()
        result.append(symbol)

        if value == 6:
            prize += 50

    if match(result) == 1:
            prize += 400
    elif match(result) == 2:
            prize += 10

    return result, prize
