import json
import random


def main() -> (dict, dict, dict, dict,):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    parse_commands = []

    # optimized using list comprehension
    [parse_commands.append(row.copy()) for row in data if 'function' in row and row['function'] == 'parse']

    print(f"parse_commands: {parse_commands}")

    # NOTE: Get all the copy commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    copy_commands = []

    # list comprehension for optimization of code
    [copy_commands.append(row.copy()) for row in data if 'function' in row and row['function'] == 'copy']
    print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = []

    # optimized code
    parse_counter = 0
    copy_counter = 0
    merged_dict = parse_commands + copy_commands

    for row in merged_dict:
        new_row = row.copy()
        if row['function'] == 'parse':
            parse_counter += 1
            new_row.update({'_list': 'parse'})
            new_row.update({'_counter': parse_counter})
        elif row['function'] == 'copy':
            copy_counter += 1
            new_row.update({'_list': 'copy'})
            new_row.update({'_counter': copy_counter})
        functional_commands.append(new_row)
    print("functional commands", functional_commands)

    # NOTE: Get random sampling of data
    random_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [
        {'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1},
        {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
