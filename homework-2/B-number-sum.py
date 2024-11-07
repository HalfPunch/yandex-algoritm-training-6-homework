def count_subsequences_with_sum(array: [int], array_len, sub_sum: int) -> int:
    sequence_counter = 0
    current_sub_sum = 0
    r_pointer = 0
    l_pointer = 0
    while l_pointer < array_len:
        while r_pointer == l_pointer or (r_pointer < array_len and current_sub_sum < sub_sum):
            current_sub_sum += array[r_pointer]
            r_pointer += 1
        if current_sub_sum == sub_sum:
            sequence_counter += 1
        current_sub_sum -= array[l_pointer]
        l_pointer += 1
    return sequence_counter


if __name__ == "__main__":
    arr_len, seq_sum = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    print(count_subsequences_with_sum(arr, arr_len, seq_sum))
