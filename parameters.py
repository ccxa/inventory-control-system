import random

""" the first i have to initialize R & Q & days of simulation"""
# R -> reorder point
# Q -> order quantity

r, q = int(input("Input R: ")), int(input("Input Q: "))


simulation_duration = 10  # number 10 provides simulation for 10 days

""" amount of product in inventory at start """
initial_balance = 10

""" initializing order cost and storage cost"""
order_cost, storage_cost = 200, 10


def distribution_of_daily_usage():
    random_number = random.randint(0, 100)

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
    random_number = random.randint(1, 10)
    if 1 <= random_number <= 2:
        return 1
    elif 3 <= random_number <= 7:
        return 2
    elif 8 <= random_number <= 10:
        return 3
