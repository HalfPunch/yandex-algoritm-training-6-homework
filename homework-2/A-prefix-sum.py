def prefix_sum(array: [int], array_len: int) -> [int]:
    prefix_sum_arr = [0 for _ in range(array_len)]
    prefix_sum_arr[0] = array[0]
    for i in range(1, array_len):
        prefix_sum_arr[i] = array[i] + prefix_sum_arr[i - 1]
    return prefix_sum_arr


if __name__ == "__main__":
    arr_len = int(input())
    arr = list(map(int, input().split(" ")))
    for elem in prefix_sum(arr, arr_len):
        print(elem)
