from collections import defaultdict


def store_checkout(inventory_tuple_list, item_purchase_list):
    dictionary = defaultdict(int)
    total_cost = 0
    for inventory_item in inventory_tuple_list:
        dictionary[inventory_item[0]] = inventory_item[1]
    for purchase_item in item_purchase_list:
        total_cost += dictionary[purchase_item]
    return total_cost


def highest_frequency_count(item_list):
    dictionary = {}
    count = 0
    for item in item_list:
        dictionary[item] = dictionary.get(item, 0) + 1
        if dictionary[item] >= count:
            count = dictionary[item]
    return count
