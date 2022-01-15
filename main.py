import calculator

register_an_order = calculator.Fos()
storing_costs, deficit_list, all_deficit_cost, all_orders_cost = register_an_order.the_loop()

_index_item = []
_index_none = []
for _index, i in enumerate(deficit_list):
    if i != 'None':
        _index_item.append(_index)
    elif i == 'None':
        _index_none.append(_index)

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
average_storing_cost = sum(storing_costs) * 10
print("Storing Cost - ", average_storing_cost)
avg_deficit_cost = sum(all_deficit_cost)
print("Deficit Cost - ", avg_deficit_cost)

_tmp = [i for i in deficit_list if i != 'None']
print("Lost profit (if expected = )", sum(_tmp) * 20)
