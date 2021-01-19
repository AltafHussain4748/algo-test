import python_test


def test_parse_commands():
    parse_commands, copy_commands, functional_commands, random_commands = python_test.main()
    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
