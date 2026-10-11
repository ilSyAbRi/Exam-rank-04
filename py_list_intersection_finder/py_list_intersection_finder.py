def appear_in_all_lists(element: int, lists: list[list[int]]) -> bool:
    for lst in lists:
        if element not in lst:
            return False
    return True

def list_intersection_finder(lists: list[list[int]]) -> list[int]:

    if lists == []:
        return []

    result = set()

    for element in lists[0]:
        check = appear_in_all_lists(element, lists)
        if check:
            result.add(element)
    result = sorted(result,reverse=False)
    return result
print(list_intersection_finder([]))