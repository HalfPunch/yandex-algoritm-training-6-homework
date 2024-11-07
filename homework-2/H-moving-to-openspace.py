def find_efficient_movement(arr: [int], arr_len: int) -> int:
    element_sum = arr[0]
    left_side_moving_sums = [0 for _ in range(arr_len)]
    for element_id in range(1, arr_len):
        left_side_moving_sums[element_id] += left_side_moving_sums[element_id - 1] + element_sum
        element_sum += arr[element_id]
    element_sum = arr[-1]
    right_side_moving_sums = [0 for _ in range(arr_len)]
    for element_id in range(arr_len - 2, -1, -1):
        right_side_moving_sums[element_id] += right_side_moving_sums[element_id + 1] + element_sum
        element_sum += arr[element_id]
    efficient_move_cost = right_side_moving_sums[0]
    for place_id in range(1, arr_len):
        move_cost = right_side_moving_sums[place_id] + left_side_moving_sums[place_id]
        if move_cost < efficient_move_cost:
            efficient_move_cost = move_cost
    return efficient_move_cost


if __name__ == "__main__":
    array_len = int(input())
    array = list(map(int, input().split(" ")))
    print(find_efficient_movement(array, array_len))

