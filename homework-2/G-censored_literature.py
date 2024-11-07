def find_longest_appropriate_string_length(string: str, string_len: int, max_rudeness: int) -> int:
    a_count, b_count = 0, 0
    current_rudeness, max_length = 0, 0
    l_pointer = 0
    for r_pointer in range(string_len):
        if string[r_pointer] == "a":
            a_count += 1
        elif string[r_pointer] == "b":
            b_count += 1
            current_rudeness += a_count
        if r_pointer - l_pointer + 1 > max_length and current_rudeness <= max_rudeness:
            max_length = r_pointer - l_pointer + 1
        while l_pointer < string_len and current_rudeness > max_rudeness:
            if string[l_pointer] == "a":
                a_count -= 1
                current_rudeness -= b_count
            elif string[l_pointer] == "b":
                b_count -= 1
            l_pointer += 1
    return max_length


if __name__ == "__main__":
    text_len, censor_factor = list(map(int, input().split(" ")))
    text = input()
    print(find_longest_appropriate_string_length(text, text_len, censor_factor))
