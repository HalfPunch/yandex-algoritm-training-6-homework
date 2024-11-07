if __name__ == "__main__":
    array_len = int(input())
    interest_sorted_array = [[i, 0, 0, False] for i in range(1, array_len + 1)]
    for container, interest, usefulness in zip(interest_sorted_array,
                                               list(map(int, input().split())),
                                               list(map(int, input().split()))):
        container[1], container[2] = interest, usefulness
    interest_sorted_array.sort(key=lambda x: (x[1], x[2], -x[0]), reverse=True)
    usefulness_sorted_array = sorted(interest_sorted_array, key=lambda x: (x[2], x[1], -x[0]), reverse=True)
    int_pointer, use_pointer = 0, 0
    for decision in list(map(int, input().split())):
        if decision:
            while usefulness_sorted_array[use_pointer][3]:
                use_pointer += 1
            print(usefulness_sorted_array[use_pointer][0])
            usefulness_sorted_array[use_pointer][3] = True
            use_pointer += 1
        else:
            while interest_sorted_array[int_pointer][3]:
                int_pointer += 1
            print(interest_sorted_array[int_pointer][0])
            interest_sorted_array[int_pointer][3] = True
            int_pointer += 1
