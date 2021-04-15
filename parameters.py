""" the first i have to initialize R & Q & days of simulation"""
# R -> reorder point
# Q -> order quantity

r, q = int(input("Input R: ")), int(input("Input Q: "))


simulation_duration = 10  # number 10 provides simulation for 10 days

""" amount of product in inventory at start """
initial_balance = 10

""" initializing order cost and storage cost"""
order_cost, storage_cost = 200, 10