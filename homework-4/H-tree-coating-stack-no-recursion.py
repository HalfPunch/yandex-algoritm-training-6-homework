import sys


def mark_nodes(dp_array: [], node_array: [], mark_hash: set):
    iter_call_stack = [0, dp_array[0][1] <= dp_array[0][0], iter(node_array[0])]
    while iter_call_stack:
        try:
            next_item = next(iter_call_stack[-1])
            if len(iter_call_stack) <= 3 or next_item != iter_call_stack[-6]:
                iter_call_stack.append(next_item)
                iter_call_stack.append(not iter_call_stack[-3] or dp_array[next_item][1] < dp_array[next_item][0])
                iter_call_stack.append(iter(node_array[next_item]))
        except StopIteration:
            iter_call_stack.pop()
            is_marked = iter_call_stack.pop()
            elem = iter_call_stack.pop() + 1
            if is_marked:
                mark_hash.add(elem)


def solve(dp_array: [], node_array: []) -> None:
    iter_call_stack = [0, iter(node_array[0])]
    while True:
        try:
            next_item = next(iter_call_stack[-1])
            if len(iter_call_stack) <= 2 or next_item != iter_call_stack[-4]:
                iter_call_stack.append(next_item)
                iter_call_stack.append(iter(node_array[next_item]))
        except StopIteration:
            iter_call_stack.pop()
            current_leaf = iter_call_stack.pop()
            if not iter_call_stack:
                break
            dp_array[iter_call_stack[-2]][1] += min(dp_array[current_leaf])
            dp_array[iter_call_stack[-2]][0] += dp_array[current_leaf][1]


if __name__ == "__main__":
    node_count = int(sys.stdin.readline())
    node_list = [set() for _ in range(node_count)]
    for data_id in range(node_count - 1):
        first, second = list(map(int, sys.stdin.readline().split()))
        first, second = first - 1, second - 1
        node_list[first].add(second)
        node_list[second].add(first)
    dp = [[0, value] for value in map(int, sys.stdin.readline().split())]
    if node_count == 1:
        print(dp[0][1], 1)
        print(1)
    else:
        mark_set = set()
        solve(dp, node_list)
        mark_nodes(dp, node_list, mark_set)
        print(min(dp[0]), len(mark_set))
        print(*sorted(mark_set))
