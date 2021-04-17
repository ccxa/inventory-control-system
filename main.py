import random
from parameters import r, q, simulation_duration, initial_balance, order_cost, storage_cost
import parameters

def register_orders(current_supply, check_points, registered_orders, day_to_register):
    if current_supply in check_points:
        orders_should_have = (check_points.index(current_supply)) + 1
        if orders_should_have > len(registered_orders):
            day2receive = parameters.distribution_of_lt() + day + 1
            order_list.append(day2receive)
            all_orders_cost.append(200)

    else:
        check_points.append(current_supply)
        check_points.sort()
        check_points.reverse()
        orders_should_have = check_points.index(current_supply)

        if orders_should_have > 0 and (orders_should_have > len(registered_orders)):
            dol = parameters.distribution_of_lt()
            day2receive = dol + day + 1
            order_list.append(day2receive)
            all_orders_cost.append(200)

        check_points.pop(check_points.index(current_supply))



order_list = []  # list of days which orders will receive

order_check_points = [r]
for i in range(0, 8):
    r = r - q
    order_check_points.append(r)

average_storing_cost = []
deficit_list = []
all_deficit_cost = []
all_orders_cost = []

print("{:<8} {:<8} {:<15} {:<10}".format("day", "usage", "start_point", "end_point"))
for day in range(1, simulation_duration + 1):
    print("-" * 43)
    today_usage = parameters.distribution_of_daily_usage()

    if day == 1:
        start_point_supply = initial_balance
        end_point_supply = start_point_supply - today_usage
        register_orders(end_point_supply, order_check_points, order_list, day)
    else:
        start_point_supply = end_point_supply
        if day in order_list:
            start_point_supply += q
            order_list.pop(order_list.index(day))

        end_point_supply = start_point_supply - today_usage
        register_orders(end_point_supply, order_check_points, order_list, day)

    if start_point_supply <= 0:
        deficit_list.append(today_usage)
    elif today_usage > start_point_supply:
        deficit = today_usage - start_point_supply
        deficit_list.append(deficit)
    else:
        deficit_list.append("None")

    if start_point_supply <= 0 and end_point_supply > 0:
        avg = (0 + end_point_supply) / 2
        average_storing_cost.append(avg)
    elif start_point_supply > 0 and end_point_supply <= 0:
        avg = (start_point_supply + 0) / 2
        average_storing_cost.append(avg)
    elif start_point_supply <= 0 and end_point_supply <= 0:
        avg = (0 + 0) / 2
        average_storing_cost.append(avg)
    else:
        avg = (start_point_supply + end_point_supply) / 2
        average_storing_cost.append(avg)

    print("{:<8} {:<12} {:<15} {:<10}".format(day, today_usage, start_point_supply, end_point_supply))

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
    except Exception as e:
        None

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
