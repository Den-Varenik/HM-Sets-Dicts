def arr_key(comp_dict: dict, second_key: str) -> list:
    arr = []
    for key in comp_dict:
        arr.append(comp_dict[key][second_key])
    return arr


def sort_by_keys(workers: list, keys: list) -> list:
    if not keys[0].isdigit():
        import re
        for i in range(len(keys)):
            keys[i] = re.findall(r'(\d+)', keys[i])
            keys[i] = int(keys[i][0])
    else:
        keys = [int(i) for i in keys]

    for i in range(len(keys)-1):
        for j in range(len(keys)-1-i):
            if keys[j] > keys[j+1]:
                keys[j], keys[j+1] = keys[j+1], keys[j]
                workers[j], workers[j+1] = workers[j+1], workers[j]
    return workers
