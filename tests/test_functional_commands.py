import python_test


def test_functional_commands():
    parse_commands, copy_commands, functional_commands, random_commands = python_test.main()
    assert functional_commands == [
        {'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1},
        {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
