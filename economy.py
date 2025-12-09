#--------- Coin System ---------
# every message sent gives users 2 coins
# getBalance: get user balance
# addBalance: add amount to balance
# !balance: users can see their balance

COINS_PER_MESSAGE = 1

coins = {}

def getBalance(user_id: int) -> int:

    """Returns coin balance of user."""

    user_id = str(user_id)
    return coins.get(user_id, 0)

def addBalance(user_id: int, amount: int):

    """Adds specified amount of coins to user's balance."""

    user_id = str(user_id)
    coins[user_id] = getBalance(user_id) + amount