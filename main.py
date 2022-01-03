import parameters
import calculator as cl


def register_orders(current_supply, check_points, registered_orders):
    """
    by comparing current amount of products at inventory with
    order check points we can decide to register new order or not.

    :param current_supply: products left at inventory.
    :param check_points: an algorithmic generated list that helps
        us to decide register new order or not.
    :param registered_orders: a list contains registered orders.
    :return: None, just appends orders to list.
    """

    if current_supply in check_points:
        orders_should_have = (check_points.index(current_supply)) + 1
        if orders_should_have > len(registered_orders):
            receiving_date = parameters.distribution_of_lt() + day + 1
            order_list.append(receiving_date)
            all_orders_cost.append(parameters.order_cost)

    else:
        check_points.append(current_supply)
        check_points.sort()
        check_points.reverse()
        orders_should_have = check_points.index(current_supply)

        if orders_should_have > 0 \
                and (orders_should_have > len(registered_orders)):
            lead_time = parameters.distribution_of_lt()

            day2receive = lead_time + day + 1
            order_list.append(day2receive)
            all_orders_cost.append(parameters.order_cost)

        check_points.pop(check_points.index(current_supply))


# Dates that orders will receive
order_list = []

# Generating orders check points
order_check_points = [parameters.reorder_point]
for i in range(0, 8):
    parameters.reorder_point = parameters.reorder_point - parameters.quantity
    order_check_points.append(parameters.reorder_point)

# Creating lists we need
average_storing_cost = []
deficit_list = []
all_deficit_cost = []
all_orders_cost = []

# Be kind with interpreter :D
end_point_supply = None

# Printing columns titles
print("{:<8} {:<8} {:<15} {:<10}".format(
    "day", "usage", "start_point", "end_point")
     )

for day in range(1, parameters.simulation_duration + 1):
    # To divide each row
    print("-" * 43)

    # estimate today's usage
    today_usage = parameters.distribution_of_daily_usage()

    if day == 1:
        # Use (hardcoded/user inputs) for first day of simulation
        start_point_supply = parameters.initial_balance
        end_point_supply = start_point_supply - today_usage
        register_orders(end_point_supply, order_check_points, order_list)
    else:

        start_point_supply = end_point_supply
        if day in order_list:
            start_point_supply += parameters.quantity
            order_list.pop(order_list.index(day))

        end_point_supply = start_point_supply - today_usage
        register_orders(end_point_supply, order_check_points, order_list)

    deficit = cl.get_deficit(start_point_supply, today_usage)
    deficit_list.append(deficit)

    avg = cl.avg_storing_cost(start_point_supply, end_point_supply)
    average_storing_cost.append(avg)

    print("{:<8} {:<12} {:<15} {:<10}".format(
        day, today_usage, start_point_supply, end_point_supply)
    )


_index_item = []
_index_none = []
_index_counter = 0
for i in deficit_list:
    if i != 'None':
        _index_item.append(_index_counter)
    elif i == 'None':
        _index_none.append(_index_counter)
    _index_counter += 1

for item in _index_item:
    _complex = []
    for none in _index_none:
        if none > item:
            _complex.append(none)
    try:
        _min = min(_complex)
        cost = (_min - item) * deficit_list[item] * 10
        all_deficit_cost.append(cost)
    except ValueError as e:
        pass

avg_order_cost = sum(all_orders_cost)
print("\n\nOrders Cost  - ", avg_order_cost)
avg_storing_cost = sum(average_storing_cost) * 10
print("Storing Cost - ", avg_storing_cost)
avg_deficit_cost = sum(all_deficit_cost)
print("Deficit Cost - ", avg_deficit_cost)

_tmp = []
for i in deficit_list:
    if i != 'None':
        _tmp.append(i)
print("Lost profit (if expected = )", sum(_tmp) * 20)
