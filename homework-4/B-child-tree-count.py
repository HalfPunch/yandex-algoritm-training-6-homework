from sys import setrecursionlimit
setrecursionlimit(100000)


def try_add_to_family(family: dict, new_member_name: str) -> bool:
    if new_member_name not in family:
        family[new_member_name] = {"name": new_member_name, "parent_of": dict(), "child_of": dict()}
        return True
    return False


def establish_family_link(child: dict, parent: dict) -> None:
    parent["parent_of"][child["name"]] = child
    child["child_of"][parent["name"]] = parent


def mark_family_for_child_count(family_member: dict) -> int:
    child_count = 0
    for child in family_member["parent_of"].values():
        child_count += mark_family_for_child_count(child)
    family_member["child_count"] = child_count
    return child_count + 1


def find_family_founder(family: dict) -> dict:
    for member in family.values():
        if not member["child_of"]:
            return member


if __name__ == "__main__":
    family_dict = {}
    for _ in range(int(input()) - 1):
        child_name, parent_name = input().split()
        try_add_to_family(family_dict, parent_name)
        try_add_to_family(family_dict, child_name)
        establish_family_link(family_dict[child_name], family_dict[parent_name])
    mark_family_for_child_count(find_family_founder(family_dict))
    for key in sorted(list(family_dict.keys())):
        print(key, family_dict[key]["child_count"])
