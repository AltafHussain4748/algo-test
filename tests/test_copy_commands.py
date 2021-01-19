import python_test


def test_copy_commands():
    parse_commands, copy_commands, functional_commands, random_commands = python_test.main()
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
