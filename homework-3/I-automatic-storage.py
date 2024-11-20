if __name__ == "__main__":
    rover_count = int(input())
    flow_order = {"12": [0, 1, 2, 3], "13": [0, 1], "14": [3, 0, 1, 2],
                  "23": [1, 2, 3, 0], "24": [1, 0], "34": [2, 3, 0, 1]}["".join(sorted(input().split()))]
    rover_list = [[] for _ in range(rover_count)]
    road_side_stack = [[] for _ in range(4)]
    for rover_id in range(rover_count):
        arrival_side, arrival_time = list(map(int, input().split()))
        road_side_stack[arrival_side - 1].append([arrival_time, 0])
        rover_list[rover_id] = road_side_stack[arrival_side - 1][-1]
    road_side_stack = list(map(lambda x: sorted(x, key=lambda y: y[0], reverse=True), road_side_stack))
    time_interval = 0
    if len(flow_order) == 4:
        for rover_id in range(rover_count):
            time_interval = max(time_interval + 1, min(map(lambda x: x[-1][0] if x else 201, road_side_stack)))
            for road_side in flow_order:
                if road_side_stack[road_side] and road_side_stack[road_side][-1][0] <= time_interval:
                    road_side_stack[road_side].pop()[1] = time_interval
                    break
    else:
        for rover_id in range(rover_count):
            time_interval = max(time_interval + 1, min(map(lambda x: x[-1][0] if x else 201, road_side_stack)))
            for road_side in flow_order:
                is_crossed = False
                if road_side_stack[road_side] and road_side_stack[road_side][-1][0] <= time_interval:
                    road_side_stack[road_side].pop()[1] = time_interval
                    is_crossed = True
                if road_side_stack[road_side + 2] and road_side_stack[road_side + 2][-1][0] <= time_interval:
                    road_side_stack[road_side + 2].pop()[1] = time_interval
                    is_crossed = True
                if is_crossed:
                    break
    for rover in rover_list:
        print(rover[1])
