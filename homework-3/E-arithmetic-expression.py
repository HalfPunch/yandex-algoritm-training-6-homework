import re

OPERATIONS = {"+": lambda x: x.pop() + x.pop(),
              "-": lambda x: x.pop(-2) - x.pop(),
              "*": lambda x: x.pop() * x.pop()}


def infix_to_postfix(infix_exp: []) -> []:
    postfix, stack = [], []
    for element in infix_exp:
        if element.isdigit():
            postfix.append(int(element))
        elif element in OPERATIONS:
            while stack and (element in {"-", "+"} and stack[-1] in OPERATIONS or element == "*" and stack[-1] == "*"):
                postfix.append(stack.pop())
            stack.append(element)
        elif element == "(":
            stack.append(element)
        else:
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
    while stack:
        postfix.append(stack.pop())
    return postfix


def solve_postfix(array: [str]) -> int:
    eval_stack = []
    for elem in array:
        if elem in OPERATIONS:
            eval_stack.append(OPERATIONS[elem](eval_stack))
        else:
            eval_stack.append(int(elem))
    return eval_stack.pop()


if __name__ == "__main__":
    input_expression = input()
    if re.findall(r"\( *\)|[+*\-] *[+*\-]|\d+ \d+|\( *[+*]|[+*\-] *\)|^ *[+*]|[+*-] *$|[^\d +*()\n-]|[^+ *(-] *\(", input_expression):
        print("WRONG")
    else:
        try:
            input_expression = re.sub(r"^ *-", "0-", re.sub(r"\( *-", "(0-", input_expression))
            print(solve_postfix(infix_to_postfix(re.findall(r"\d+|[+*()-]", input_expression))))
        except (ValueError, IndexError):
            print("WRONG")
