def sort_dicts_by_key_ai(data, key_name):
    sorted_list = sorted(data, key=lambda d: d.get(key_name, None))
    return sorted_list
