open_bracket_set = {"(", "[", "{"}
bracket_pair_dict = {"(": ")", "[": "]", "{": "}"}
if __name__ == "__main__":
    brackets_stack = []
    is_correct_sequence = True
    for bracket in input():
        if bracket in open_bracket_set:
            brackets_stack.append(bracket)
        else:
            if not brackets_stack or not bracket_pair_dict[brackets_stack.pop()] == bracket:
                is_correct_sequence = False
                break
    print("yes" if is_correct_sequence and not brackets_stack else "no")
