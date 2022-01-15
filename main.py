import calculator
# some parts and vars need cleaning yet

fos = calculator.Fos()
storing_costs, deficit_list, deficit_costs, orders_costs = fos.calculate()


index_item = [_i for _i, i in enumerate(deficit_list) if i != 'None']
index_none = [_i for _i, i in enumerate(deficit_list) if i == 'None']

for item in index_item:
    _complex = [none for none in index_none if none > item]
    try:
        _min = min(_complex)
        cost = (_min - item) * deficit_list[item] * 10
        deficit_costs.append(cost)
    except ValueError as e:
        pass

avg_order_cost = sum(orders_costs)
print("\n\nOrders Cost  - ", avg_order_cost)
average_storing_cost = sum(storing_costs) * 10
print("Storing Cost - ", average_storing_cost)
avg_deficit_cost = sum(deficit_costs)
print("Deficit Cost - ", avg_deficit_cost)

_tmp = [i for i in deficit_list if i != 'None']
print("Lost profit (if expected = )", sum(_tmp) * 20)
