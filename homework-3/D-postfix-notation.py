OPERATIONS = {"+": lambda x: x.pop() + x.pop(),
              "-": lambda x: x.pop(-2) - x.pop(),
              "*": lambda x: x.pop() * x.pop()}


def postfix_eval(array: [str]) -> int:
    eval_stack = []
    for elem in array:
        if elem in OPERATIONS:
            eval_stack.append(OPERATIONS[elem](eval_stack))
        else:
            eval_stack.append(int(elem))
    return eval_stack.pop()


if __name__ == "__main__":
    print(postfix_eval(input().split()))
