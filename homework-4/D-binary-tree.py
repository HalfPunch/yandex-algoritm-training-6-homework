import sys


def binary_tree_add(branch: dict, num: int) -> bool:
    if not branch:
        branch["value"] = num
        branch["left"] = dict()
        branch["right"] = dict()
        return True
    if branch["value"] == num:
        return False
    if num < branch["value"]:
        return binary_tree_add(branch["left"], num)
    else:
        return binary_tree_add(branch["right"], num)


def binary_tree_search(branch: dict, num: int) -> bool:
    if not branch:
        return False
    if branch["value"] == num:
        return True
    if num < branch["value"]:
        return binary_tree_search(branch["left"], num)
    else:
        return binary_tree_search(branch["right"], num)


def binary_tree_print(tree: dict, cur_depth: int) -> None:
    if tree["left"]:
        binary_tree_print(tree["left"], cur_depth + 1)
    print("."*cur_depth + str(tree["value"]))
    if tree["right"]:
        binary_tree_print(tree["right"], cur_depth + 1)


if __name__ == "__main__":
    binary_tree_root = dict()
    for request in map(str.split, sys.stdin.readlines()):
        if request[0] == "ADD":
            print("DONE" if binary_tree_add(binary_tree_root, int(request[1])) else "ALREADY")
        elif request[0] == "SEARCH":
            print("YES" if binary_tree_search(binary_tree_root, int(request[1])) else "NO")
        else:
            binary_tree_print(binary_tree_root, 0)
