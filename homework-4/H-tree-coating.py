import sys
sys.setrecursionlimit(500001)


def mark_nodes_up(dp_array: [], node_array: [], mark_hash: set, node=0, parent=-1):
    mark_hash.add(node + 1)
    for child in node_array[node]:
        if child == parent:
            continue
        if dp_array[child][0] < dp_array[child][1]:
            mark_nodes_down(dp_array, node_array, mark_hash, child, node)
        else:
            mark_nodes_up(dp_array, node_array, mark_hash, child, node)


def mark_nodes_down(dp_array: [], node_array: [], mark_hash: [], node=0, parent=-1):
    for child in node_array[node]:
        if child == parent:
            continue
        mark_nodes_up(dp_array, node_array, mark_hash, child, node)


def solve(dp_array: [], node_array: [], node=0, parent=-1) -> None:
    for child in node_array[node]:
        if child == parent:
            continue
        solve(dp_array, node_list, child, node)
        dp_array[node][1] += min(dp_array[child])
        dp_array[node][0] += dp_array[child][1]


if __name__ == "__main__":
    node_count = int(sys.stdin.readline())
    node_list = [[] for _ in range(node_count)]
    for data_id in range(node_count - 1):
        first, second = list(map(int, sys.stdin.readline().split()))
        first, second = first - 1, second - 1
        node_list[first].append(second)
        node_list[second].append(first)
    dp = [[0, value] for value in map(int, sys.stdin.readline().split())]
    if node_count == 1:
        print(dp[0][1], 1)
        print(1)
    else:
        mark_set = set()
        solve(dp, node_list)
        if dp[0][0] < dp[0][1]:
            mark_nodes_down(dp, node_list, mark_set)
        else:
            mark_nodes_up(dp, node_list, mark_set)
        print(min(dp[0]), len(mark_set))
        print(*sorted(mark_set))
