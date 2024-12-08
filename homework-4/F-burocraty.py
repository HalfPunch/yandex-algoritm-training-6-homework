import sys
sys.setrecursionlimit(1000000)


def mark_family_for_child_count(node_array: list, output_array: list, cur_node=0, parent=0) -> int:
    child_count = 1
    for child in node_array[cur_node]:
        if child != parent:
            child_count += mark_family_for_child_count(node_array, output_array, child, cur_node)
            output_array[cur_node] += output_array[child]
    output_array[cur_node] += child_count
    return child_count


if __name__ == "__main__":
    node_count = int(input())
    node_list = [set() for _ in range(node_count)]
    for node1, node2 in zip(range(1, node_count), list(map(lambda x: x-1, map(int, input().split())))):
        node_list[node2].add(node1)
        node_list[node1].add(node2)
    output_list = [0 for _ in range(node_count)]
    mark_family_for_child_count(node_list, output_list)
    print(*output_list)
