# Returns trimmed binary array, and it's new dimensions
def binary_trim(untrimmed_arr: [[]], arr_len: int) -> [[[]], int, int]:
    top_trim, bottom_trim, left_trim, right_trim = 0, 0, 0, 0
    is_top_not_found, is_bottom_not_found, is_left_not_found, is_right_not_found = True, True, True, True
    # Vertical trimming
    for row in range(arr_len):
        for column in range(arr_len):
            # Top Trimming Condition
            if untrimmed_arr[row][column] != 0:
                is_top_not_found = False
            # Bottom Trimming Condition
            if untrimmed_arr[arr_len - row - 1][column] != 0:
                is_bottom_not_found = False
        if not is_top_not_found and not is_bottom_not_found:
            break
        if is_bottom_not_found:
            bottom_trim += 1
        if is_top_not_found:
            top_trim += 1
    # Horizontal trimming
    for column in range(arr_len):
        for row in range(top_trim, arr_len - bottom_trim):
            # Left Trimming Condition
            if untrimmed_arr[row][column] != 0:
                is_left_not_found = False
            # Right Trimming Condition
            if untrimmed_arr[row][arr_len - column - 1] != 0:
                is_right_not_found = False
        if not is_left_not_found and not is_right_not_found:
            break
        if is_left_not_found:
            left_trim += 1
        if is_right_not_found:
            right_trim += 1
    trimmed_arr = []
    for i in range(top_trim, arr_len - bottom_trim):
        trimmed_arr.append(untrimmed_arr[i][left_trim:arr_len - right_trim])
    return trimmed_arr, arr_len - top_trim - bottom_trim, arr_len - left_trim - right_trim


def convert_to_projection(tablet_array: [], tablet_array_dimensions: [int, int]) -> [{str: [[]]}]:
    horizontal_projection = []
    horizontal_projection_lengths = []
    for row in range(tablet_array_dimensions[0]):
        last_found_value = tablet_array[row][0]
        new_projection_line = [last_found_value]
        new_projection_lengths_line = [1]
        for column in range(1, tablet_array_dimensions[1]):
            if last_found_value != tablet_array[row][column]:
                last_found_value = tablet_array[row][column]
                new_projection_line.append(last_found_value)
                new_projection_lengths_line.append(1)
            else:
                new_projection_lengths_line[-1] += 1
        if (len(horizontal_projection) == 0 or
                horizontal_projection[-1] != new_projection_line or
                horizontal_projection_lengths[-1] != new_projection_lengths_line):
            horizontal_projection.append(new_projection_line)
            horizontal_projection_lengths.append(new_projection_lengths_line)
    vertical_projection = []
    vertical_projection_lengths = []
    for column in range(tablet_array_dimensions[1]):
        last_found_value = tablet_array[0][column]
        new_projection_line = [last_found_value]
        new_projection_lengths_line = [1]
        for row in range(tablet_array_dimensions[0]):
            if last_found_value != tablet_array[row][column]:
                last_found_value = tablet_array[row][column]
                new_projection_line.append(last_found_value)
                new_projection_lengths_line.append(1)
            else:
                new_projection_lengths_line[-1] += 1
        if (len(vertical_projection) == 0 or
                vertical_projection[-1] != new_projection_line or
                vertical_projection_lengths[-1] != new_projection_lengths_line):
            vertical_projection.append(new_projection_line)
            vertical_projection_lengths.append(new_projection_lengths_line)
    return [{"Horizontal": horizontal_projection, "Vertical": vertical_projection},
            {"Horizontal": horizontal_projection_lengths, "Vertical": vertical_projection_lengths}]


LETTER_PROJECTIONS = {
    'i': {"Horizontal": [[1]], "Vertical": [[1]]},
    'o': {"Horizontal": [[1], [1, 0, 1], [1]], "Vertical": [[1], [1, 0, 1], [1]]},
    'c': {"Horizontal": [[1], [1, 0], [1]], "Vertical": [[1], [1, 0, 1]]},
    'l': {"Horizontal": [[1, 0], [1]], "Vertical": [[1], [0, 1]]},
    'h': {"Horizontal": [[1, 0, 1], [1], [1, 0, 1]], "Vertical": [[1], [0, 1, 0], [1]]},
    'p': {"Horizontal": [[1], [1, 0, 1], [1], [1, 0]], "Vertical": [[1], [1, 0, 1, 0], [1, 0]]},
    # NOT FOR TASK, JUST FOR MEMES
    'q': {"Horizontal": [[1, 0], [1, 0, 1, 0], [1, 0], [0, 1]], "Vertical": [[1, 0], [1, 0, 1, 0], [1, 0], [0, 1]]},
    'a': {"Horizontal": [[1], [1, 0, 1], [1], [1, 0, 1]], "Vertical": [[1], [1, 0, 1, 0], [1]]},
    'b': {"Horizontal": [[1], [1, 0, 1], [1], [1, 0, 1], [1]], "Vertical": [[1], [1, 0, 1, 0, 1], [1]]},
    'j': {"Horizontal": [[0, 1], [1]], "Vertical": [[0, 1], [1]]},
    's': {"Horizontal": [[1], [1, 0], [1], [0, 1], [1]], "Vertical": [[1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1]]},
    'e': {"Horizontal": [[1], [1, 0], [1], [1, 0], [1]], "Vertical": [[1], [1, 0, 1, 0, 1]]},
    'm': {"Horizontal": [[1], [1, 0, 1, 0, 1], [1, 0, 1]], "Vertical": [[1], [1, 0], [1, 0], [1, 0], [1]]},
    'w': {"Horizontal": [[1, 0, 1], [1, 0, 1, 0, 1], [1]], "Vertical": [[1], [0, 1], [0, 1], [0, 1], 1]},
    't': {"Horizontal": [[1], [0, 1, 0]], "Vertical": [[1, 0], [1], [1, 0]]},
    'f': {"Horizontal": [[1], [1, 0], [1], [1, 0]], "Vertical": [[1], [1, 0, 1, 0]]},
    'g': {"Horizontal": [[1], [1, 0], [1, 0, 1], [1, 0, 1], [1]], "Vertical": [[1], [1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1]]},
    'u': {"Horizontal": [[1, 0, 1], [1]], "Vertical": [[1], [0, 1], [1]]},
    'd': {"Horizontal": [[1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0]], "Vertical": [[1], [1, 0, 1], [1, 0, 1], [0, 1, 0]]},
    'n': {"Horizontal": [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]], "Vertical": [[1], [0, 1, 0], [0, 1, 0], [1]]}
}


def identify_projection(projection: {str: []}) -> str:
    for letter in LETTER_PROJECTIONS:
        if (LETTER_PROJECTIONS[letter]["Horizontal"] == projection["Horizontal"] and
                LETTER_PROJECTIONS[letter]["Vertical"] == projection["Vertical"]):
            return letter.capitalize()
    return "X"


def string_to_binary_array(string: str, true_char: str) -> [int]:
    binary_array = []
    for char in string:
        if char == true_char:
            binary_array.append(1)
        else:
            binary_array.append(0)
    return binary_array


if __name__ == "__main__":
    tablet = []
    tablet_dimensions = int(input())
    for i in range(tablet_dimensions):
        tablet.append(string_to_binary_array(input(), '#'))
    trimmed_tablet, trimmed_tablet_rows, trimmed_tablet_columns = binary_trim(tablet, tablet_dimensions)
    tablet_projection, tablet_projection_lengths = (
        convert_to_projection(trimmed_tablet, [trimmed_tablet_rows, trimmed_tablet_columns]))
    print(identify_projection(tablet_projection))
