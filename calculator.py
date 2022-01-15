import parameters as params


def get_storing_cost(start_point_supply, end_point_supply):
    if start_point_supply <= 0 < end_point_supply:
        avg = (0 + end_point_supply) / 2
    elif start_point_supply > 0 >= end_point_supply:
        avg = (start_point_supply + 0) / 2
    elif start_point_supply <= 0 and end_point_supply <= 0:
        avg = (0 + 0) / 2
    else:
        avg = (start_point_supply + end_point_supply) / 2
    return avg


def get_deficit(start_point_supply, today_usage):
    if start_point_supply <= 0:
        return today_usage
    elif today_usage > start_point_supply:
        deficit = today_usage - start_point_supply
        return deficit
    else:
        return "None"


def register_orders(current_supply, check_points, registered_orders, day):
    """
    by comparing current amount of products at inventory with
    order check points we can decide to register new order or not.
    :param current_supply: products left at inventory.
    :param check_points: an algorithmic generated list that helps
        us to decide register new order or not.
    :param registered_orders: a list contains registered orders.
    :param day: the iterated day by for loop
    :return: None, just appends orders to the list.

    """
    _pop = False
    if current_supply in check_points:
        orders_should_have = (check_points.index(current_supply)) + 1
        if orders_should_have > len(registered_orders):
            receiving_date = params.distribution_of_lt() + day + 1
            param = params.order_cost

            return receiving_date, param, _pop
        receiving_date, param = 'None', 'None'
        return receiving_date, param, _pop
    else:

        _pop = True
        check_points.append(current_supply)
        check_points.sort()
        check_points.reverse()
        orders_should_have = check_points.index(current_supply)

        if orders_should_have > 0 \
                and (orders_should_have > len(registered_orders)):
            lead_time = params.distribution_of_lt()

            day2receive = lead_time + day + 1
            param = params.order_cost
            return day2receive, param, _pop
        day2receive, param = 'None', 'None'
        return day2receive, param, _pop


class Fos:

    # Generating orders check points
    order_check_points = [params.reorder_point]
    for i in range(0, 8):
        params.reorder_point = params.reorder_point - params.quantity
        order_check_points.append(params.reorder_point)

    # Creating lists we need
    storing_costs, deficit_list = [], []
    all_deficit_cost, all_orders_cost = [], []
    # Dates that orders will receive
    order_list = []
    # Be kind with interpreter :D
    end_point_supply = None

    # Printing columns titles
    print("{:<8} {:<8} {:<15} {:<10}".format(
        "day", "usage", "start_point", "end_point")
    )

    def the_loop(self):
        for day in range(1, params.simulation_duration + 1):
            # To divide each row
            print("-" * 43)

            # estimate today's usage
            today_usage = params.distribution_of_daily_usage()

            if day == 1:
                # Use (hardcoded/user inputs) for first day of simulation
                start_point_supply = params.initial_balance
                end_point_supply = start_point_supply - today_usage

                _receiving_date, par, _pop = register_orders(end_point_supply, self.order_check_points, self.order_list, day)
                if _receiving_date != 'None:':
                    self.order_list.append(_receiving_date)
                    self.all_orders_cost.append(par)
                if _pop:
                    self.order_check_points.pop(self.order_check_points.index(end_point_supply))
            else:

                start_point_supply = end_point_supply
                if day in self.order_check_points:
                    start_point_supply += params.quantity
                    self.order_check_points.pop(self.order_check_points.index(day))

                end_point_supply = start_point_supply - today_usage
                _receiving_date, par, _pop = register_orders(end_point_supply, self.order_check_points, self.order_list, day)
                if _receiving_date != 'None':
                    self.order_list.append(_receiving_date)
                    self.all_orders_cost.append(par)
                if _pop:
                    self.order_check_points.pop(self.order_check_points.index(end_point_supply))

            deficit = get_deficit(start_point_supply, today_usage)
            self.deficit_list.append(deficit)

            avg = get_storing_cost(start_point_supply, end_point_supply)
            self.storing_costs.append(avg)

            print("{:<8} {:<12} {:<15} {:<10}".format(
                day, today_usage, start_point_supply, end_point_supply)
            )

        return self.storing_costs, self.deficit_list, self.all_deficit_cost, self.all_orders_cost
