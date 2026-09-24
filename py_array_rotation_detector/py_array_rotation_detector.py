def array_rotation_detector(arr1: list, arr2: list) -> bool:
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    if len_arr1 == 0 and len_arr2 == 0:
        return True
    elif len_arr1 != len_arr2:
        return False
    
    for i in range(len_arr1):
        cut = i
        first_part = arr1[cut:]
        second_part = arr1[:cut]
        comp_arr = first_part + second_part
        if comp_arr == arr2:
            return True
    
    return False

print(array_rotation_detector([1,2,1,3], [1,3,1,2]))