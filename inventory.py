#!/usr/bin/env python3
import csv

'''
def display_inventory(inventory):

    print('inventory: ')
    for key, value in inventory.items():
        print(value, key)
    print('Total number of items: %d' % sum(inventory.values()))
'''

def add_to_inventory(inventory, added_items):
    for i in range(0, len(added_items)):
        if added_items[i] not in inventory:
            inventory[added_items[i]] = 0
    for i in range(0, len(added_items)):
        for key in inventory:
            if key == added_items[i]:
                inventory[key] += 1
    return inventory


def print_table(inventory, order):
    ''' In this function create table and turn on sort or no.
        Width print table dependence of longest key
        Len Longest key count how much letter have string'''

    order = 'b'
    print('Inventory: ')
    list_len_key = []
    for key in inventory:
        list_len_key += [len(key)]
    longest_key = max(list_len_key)
    # print(longest_key)
    print('  count%sitem name' % (' '*(longest_key-5)))     # How much empty space, for longest key
    print('-----------------%s' % ('-'*(longest_key-6)))
    if order == 'a':
        for key, value in inventory.items():
            print('%7s' % value, key.rjust(5+(longest_key-2)))
        print('-----------------%s' % ('-'*(longest_key-6)))
        print('Total number of items: %d' % sum(inventory.values()))
    elif order == 'b':
        key_value = []
        for key, value in inventory.items():
            key_value += [(value, key)]
        key_value.sort(reverse=True)    # sort desc
        for value, key in key_value:
            print('%7s' % value, key.rjust(5+(longest_key-2)))
        print('-----------------%s' % ('-'*(longest_key-6)))
        print('Total number of items: %d' % sum(inventory.values()))
    elif order == 'c':
        key_value = []
        for key, value in inventory.items():
            key_value += [(value, key)]
        key_value.sort(reverse=False)   # sort asc
        for value, key in key_value:
            print('%7s' % value, key.rjust(5+(longest_key-2)))
        print('-----------------%s' % ('-'*(longest_key-6)))
        print('Total number of items: %d' % sum(inventory.values()))


def import_inventory(inventory, filename='test_inventory_export.csv'):
    file_csv = open(filename, 'r')
    reader = csv.reader(file_csv)
    new_file_reader = []
    for row in reader:
        new_file_reader += row
        add_to_inventory(inventory, new_file_reader)   # new parameter in function add_to_inventory


def export_inventory(inventory, filename='test_inventory_export.csv'):
    file_csv = open(filename, 'w')
    writer = csv.writer(file_csv)
    all_keys_values = []
    for key, values in inventory.items():
        all_keys_values += [key]*values
    all_keys_values
    all_keys_values_word = ','.join(all_keys_values) + '\n'
    file_csv.write(all_keys_values_word)


def main():
    inv = {}
    dragon_loot = []
    inv = add_to_inventory(inv, dragon_loot)
    # display_inventory(inv)
    import_inventory(inv)
    print_table(inv, 'order')
    export_inventory(inv)

main()
