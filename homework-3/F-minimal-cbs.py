brackets = {"(": ")", "[": "]"}
alphabet_weights = {"(": 0, ")": 0, "[": 0, "]": 0}


def set_weights(seq_alphabet: str) -> None:
    global alphabet_weights
    weight = 0
    for bracket in seq_alphabet:
        alphabet_weights[bracket] = weight = weight + 1


def is_layered(seq_alphabet: str) -> bool:
    return seq_alphabet[0] in brackets or seq_alphabet[1] in brackets and brackets[seq_alphabet[1]] != seq_alphabet[0]


def filling_brackets(seq_alphabet: str):
    for bracket in seq_alphabet:
        if bracket in brackets:
            return bracket


def get_min_correct_bracket_sequence(seq_len: int, seq_alphabet: str, seq_beginning: str) -> str:
    set_weights(seq_alphabet)
    seq_is_layered, filling_pattern_opener = is_layered(seq_alphabet), filling_brackets(seq_alphabet)
    stack, sequence = [], ""
    for char in seq_beginning:
        if char in {"(", "["}:
            stack.append(char)
        else:
            stack.pop()
        sequence += char
    while stack and alphabet_weights[brackets[stack[-1]]] <= alphabet_weights[filling_pattern_opener]:
        sequence += brackets[stack.pop()]
    sequence += (filling_pattern_opener * ((seq_len - len(stack) - len(sequence)) // 2)
                 + brackets[filling_pattern_opener] * ((seq_len - len(stack) - len(sequence)) // 2)
                 if seq_is_layered else
                 (filling_pattern_opener + brackets[filling_pattern_opener])
                 * ((seq_len - len(stack) - len(sequence)) // 2))
    sequence += "".join(map(lambda x: brackets[x], reversed(stack)))
    return sequence


if __name__ == "__main__":
    print(get_min_correct_bracket_sequence(int(input()), input(), input()))
