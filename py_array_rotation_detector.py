def array_rotation_detector(arr1: list, arr2: list) -> bool:
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    if len_arr1 == 0 and len_arr2 == 0:
        return True
    elif len_arr1 != len_arr2:
        return False

    nb_modulo = len_arr1

    for i in range(len_arr1):
        val = arr1[i]
        id_arr1 = arr1.index(val)
        next_id_arr1 = (id_arr1 + 1) % nb_modulo
        id_arr2 = arr2.index(val)
        next_id_arr2 = (id_arr2 + 1 )% nb_modulo
        if arr1[next_id_arr1] != arr2[next_id_arr2]:
            return False
    
    return True

print(array_rotation_detector([1, 2, 3], [3, 2, 1]))