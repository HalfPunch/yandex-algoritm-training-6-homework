import sys
sys.setrecursionlimit(100000)


def mark_and_count_for_children(node_array: list, output_array: list, current_node: int, parent=0) -> int:
    child_count = 1
    for child in node_array[current_node]:
        if child != parent:
            child_count += mark_and_count_for_children(node_array, output_array, child, current_node)
    output_array[current_node] = child_count
    return child_count


if __name__ == "__main__":
    list_length = int(input())
    node_list = [[] for _ in range(list_length)]
    output_list = [0 for _ in range(list_length)]
    for _ in range(list_length - 1):
        first_node, second_node = map(int, sys.stdin.readline().split())
        node_list[first_node - 1].append(second_node - 1)
        node_list[second_node - 1].append(first_node - 1)
    mark_and_count_for_children(node_list, output_list, 0)
    print(*output_list)
