import sys
sys.setrecursionlimit(100000)


def try_add_to_family(family: dict, new_member_name: str) -> bool:
    if new_member_name not in family:
        family[new_member_name] = {"name": new_member_name, "parent_of": dict(), "child_of": dict()}
        return True
    return False


def establish_family_link(child: dict, parent: dict) -> None:
    parent["parent_of"][child["name"]] = child
    child["child_of"][parent["name"]] = parent


def find_family_founder(family: dict) -> dict:
    for member in family.values():
        if not member["child_of"]:
            return member


def find_lca_member_name(member_1: dict, member_2: dict) -> str:
    while member_1 is not member_2:
        if member_1["depth"] >= member_2["depth"]:
            member_1 = member_1["child_of"][list(member_1["child_of"].keys())[0]]
        else:
            member_2 = member_2["child_of"][list(member_2["child_of"].keys())[0]]
    return member_1["name"]


def mark_family_for_depth(family_member: dict, current_depth: int) -> None:
    family_member["depth"] = current_depth
    for child in family_member["parent_of"].values():
        mark_family_for_depth(child, current_depth + 1)


if __name__ == "__main__":
    family_dict = {}
    for _ in range(int(input()) - 1):
        child_name, parent_name = sys.stdin.readline().split()
        try_add_to_family(family_dict, parent_name)
        try_add_to_family(family_dict, child_name)
        establish_family_link(family_dict[child_name], family_dict[parent_name])
    mark_family_for_depth(find_family_founder(family_dict), 0)
    for request in map(str.split, sys.stdin.readlines()):
        first_member, second_member = request
        print(find_lca_member_name(family_dict[first_member], family_dict[second_member]))
