from sys import setrecursionlimit
setrecursionlimit(10000)


def factorial_tree(left_num: int, right_num: int, module: int) -> int:
    if left_num > right_num:
        return 1
    if left_num == right_num:
        return left_num % module
    if right_num - left_num == 1:
        return ((left_num % module) * (right_num % module)) % module
    median = (left_num + right_num) // 2
    return (factorial_tree(left_num, median, module) * factorial_tree(median + 1, right_num, module)) % module


def get_graph_branch_variety(bird_array: list, bird: int, parent: int, module: int):
    graph_variations = 1
    next_branch = {bird}
    while next_branch:
        bird = next_branch.pop()
        deadend_elements = 0
        for child_id in bird_array[bird][1].difference({parent}):
            if bird_array[child_id][0]:
                raise ValueError
            bird_array[child_id][0] = True
            if len(bird_array[child_id][1]) == 1:
                deadend_elements += 1
            else:
                if next_branch:
                    raise ValueError
                else:
                    next_branch.add(child_id)
        graph_variations *= factorial_tree(1, deadend_elements, module)
        graph_variations %= module
        parent = bird
    return graph_variations


def get_graph_root_variety(bird_array: list, bird: int, module: int):
    graph_variations, deadend_elements, parent_bird = 1, 0, -1
    linked_elements = set()
    if len(bird_array[bird][1]) == 1:
        bird = next(iter(bird_array[bird][1]))
        bird_array[bird][0] = True
    for child_id in bird_array[bird][1]:
        bird_array[child_id][0] = True
        if len(bird_array[child_id][1]) == 1:
            deadend_elements += 1
        else:
            if len(linked_elements) > 1:
                raise ValueError
            linked_elements.add(child_id)
    graph_variations *= (4 if len(linked_elements) else 2) * (factorial_tree(1, deadend_elements, module))
    for branch_starter in linked_elements:
        graph_variations *= get_graph_branch_variety(bird_array, branch_starter, bird, module)
        graph_variations %= module
    return graph_variations


if __name__ == "__main__":
    bird_count, bird_link_count, mod = list(map(int, input().split()))
    total_variations = 1
    single_birds = 0
    graph_count = 0
    bird_list = [[False, set()] for _ in range(bird_count)]
    for _ in range(bird_link_count):
        first_bird, second_bird = list(map(int, input().split()))
        bird_list[first_bird - 1][1].add(second_bird - 1)
        bird_list[second_bird - 1][1].add(first_bird - 1)
    bird_id = 0
    try:
        while bird_id != bird_count:
            if bird_list[bird_id][0]:
                bird_id += 1
                continue
            elif not bird_list[bird_id][1]:
                single_birds += 1
            else:
                total_variations *= get_graph_root_variety(bird_list, bird_id, mod)
                total_variations %= mod
                graph_count += 1
            bird_id += 1
        total_variations *= factorial_tree(bird_count - single_birds + 2, bird_count + 1, mod)
        total_variations *= factorial_tree(1, graph_count, mod)
        total_variations %= mod
        print(total_variations)
    except ValueError:
        print(0)
