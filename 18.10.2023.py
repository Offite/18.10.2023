# Задание №1

# def de_none(lst):
#     result = []
#     for elem in lst:
#         if elem is not None:
#             result.append(elem)
#     return result

# Задание №2

# def list_insert(ref_list, start, num, rep):
#     if start > len(ref_list):
#         return -1
#     else :
#         return ref_list[:start] + [num for _ in range(rep)] + ref_list[start:]

# Задание №3

def get_elem(d, k):
    if k in d:
        return d[k]
    else:
        return None