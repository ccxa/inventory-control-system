import random

# Getting reorder point and order quantity from user
reorder_point = int(input("Input reorder_point: "))
quantity = int(input("Input quantity: "))

# Days to simulate
simulation_duration = 10

# The amount of product in stock at start
initial_balance = 10

# Init order cost and storage cost : Optional
order_cost, storage_cost = 200, 10

# Order cost
order_cost = 200


def distribution_of_daily_usage():
    """
    This function generates a random number as product usage
    in a single day, i.e. it may produce number 5 with probability
    of 10% also it shows 5 products used at inventory!

    HINT: YOU CAN PERSONALIZE THIS PARAMETER TO GET YOUR RESULT
    :return:
    Integer number in range 0 - 5 that shows usage of
    product at inventory in that day.
    """
    random_number = random.randint(0, 100)

    # If generated number become 0, then we generate a new one
    # between 0.1 - 0.9 to guess number of used products.
    if random_number < 1:
        random_number = (random.randint(1, 9)) / 10

    if 0.1 <= random_number <= 0.5:
        return 0
    elif 0.6 <= random_number <= 15:
        return 1
    elif 16 <= random_number <= 35:
        return 2
    elif 36 <= random_number <= 75:
        return 3
    elif 76 <= random_number <= 90:
        return 4
    elif 91 <= random_number <= 100:
        return 5


def distribution_of_lt():
    """
    LT is load time
    The time that you have to wait to receive your orders

    definitely you can personalize this parameters too
    :return:
    days to wait for orders to receive as integer number
    """

    random_number = random.randint(1, 10)
    if 1 <= random_number <= 2:
        return 1
    elif 3 <= random_number <= 7:
        return 2
    elif 8 <= random_number <= 10:
        return 3
