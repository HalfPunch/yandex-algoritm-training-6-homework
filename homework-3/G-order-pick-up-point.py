if __name__ == "__main__":
    opp_worktime, client_flow_cap = list(map(int, input().split()))
    client_income = list(map(int, input().split()))
    client_queue, queue_pointer = [], 0
    minutes_spent = 0
    for i in range(len(client_income)):
        client_queue.append(client_income[i])
        remaining_client_flow = client_flow_cap
        while len(client_queue) > queue_pointer and remaining_client_flow > client_queue[queue_pointer]:
            minutes_spent += (i - queue_pointer + 1) * client_queue[queue_pointer]
            remaining_client_flow, client_queue[queue_pointer] = remaining_client_flow - client_queue[queue_pointer], 0
            queue_pointer += 1
        if len(client_queue) > queue_pointer and remaining_client_flow:
            minutes_spent += (i - queue_pointer + 1) * remaining_client_flow
            client_queue[queue_pointer] -= remaining_client_flow
    while len(client_queue) > queue_pointer:
        minutes_spent += (opp_worktime - queue_pointer + 1) * client_queue[queue_pointer]
        queue_pointer += 1
    print(minutes_spent)
