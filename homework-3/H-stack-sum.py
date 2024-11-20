import re
if __name__ == "__main__":
    stack_prefix_sum, stack = [0], []
    for request in range(int(input())):
        request_list = re.findall(r"[+?-]|\d+", input())
        if request_list[0] == "-":
            print(stack.pop())
            stack_prefix_sum.pop()
        elif request_list[0] == "+":
            stack.append(int(request_list[1]))
            stack_prefix_sum.append(stack_prefix_sum[-1] + stack[-1])
        else:
            print(stack_prefix_sum[-1] - stack_prefix_sum[-1 - int(request_list[1])])
