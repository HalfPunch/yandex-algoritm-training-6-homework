def find_triple_sums(arr: [int], arr_len):
    current_sum = 0
    left_array_sum = arr[0]
    right_array_sum = sum(arr) - arr[0]
    for pointer in range(1, arr_len - 1):
        right_array_sum -= arr[pointer]
        current_sum += left_array_sum * arr[pointer] * right_array_sum
        left_array_sum += arr[pointer]
    return current_sum


if __name__ == "__main__":
    array_len = int(input())
    array = list(map(int, input().split(" ")))
    print(find_triple_sums(array, array_len) % 1000000007)
