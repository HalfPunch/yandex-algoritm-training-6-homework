if __name__ == "__main__":
    emigrants_stack = []
    list_len, town_rent_list = int(input()), [[rent_cost, 0] for rent_cost in list(map(int, input().split()))]
    town_stack = []
    for town_id in range(list_len):
        while town_stack and town_rent_list[town_id] < town_stack[-1]:
            town_stack.pop()[1] = town_id
        town_stack.append(town_rent_list[town_id])
    while town_stack:
        town_stack.pop()[1] = -1
    for town in town_rent_list:
        print(town[1])
