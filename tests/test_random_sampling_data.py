import python_test


def test_functional_commands():
    parse_commands, copy_commands, functional_commands, random_commands = python_test.main()
    assert len(random_commands) == 2
