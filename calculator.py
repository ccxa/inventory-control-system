def avg_storing_cost(start_point_supply, end_point_supply):
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
