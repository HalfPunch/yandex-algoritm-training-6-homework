def two_pointer_search(array: [int], array_len: int, distance: int) -> int:
    l_pointer = 0
    count = 1
    for r_pointer in range(1, array_len):
        if array[r_pointer] - array[l_pointer] > distance:
            l_pointer += 1
        else:
            count += 1
    return count


if __name__ == "__main__":
    task_count, diversity_coefficient = list(map(int, input().split(" ")))
    task_list = sorted(list(map(int, input().split(" "))))
    print(two_pointer_search(task_list, task_count, diversity_coefficient))
