def bill_split(food_type, cost):
    my_costs = 0
    friend_costs = 0
    for i in range(len(food_type)):
        if food_type[i] == 'S':
            my_costs += cost[i]
        else:
            my_costs += cost[i] / 2
            friend_costs += cost[i] / 2
    print(my_costs, friend_costs, sep=', ')


bill_split(["S", "N", "S", "S"], [13, 18, 15, 4])