def sorted_array_to_meridian_array(sorted_arr: [int], arr_len: int) -> [int]:
    meridian_arr = []
    if arr_len % 2 != 0:
        meridian_arr.append(sorted_arr[arr_len // 2])
        l_pointer, r_pointer = arr_len // 2 - 1, arr_len // 2 + 1
    else:
        l_pointer, r_pointer = arr_len // 2 - 1, arr_len // 2
    while r_pointer != arr_len:
        meridian_arr.append(sorted_arr[l_pointer])
        meridian_arr.append(sorted_arr[r_pointer])
        l_pointer -= 1
        r_pointer += 1
    return meridian_arr


if __name__ == "__main__":
    array_len = int(input())
    array = sorted(list(map(int, input().split(" "))))
    for elem in sorted_array_to_meridian_array(array, array_len):
        print(elem)
