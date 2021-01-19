from unittest.mock import patch

import python_test


def test_mock_random():
    with patch('python_test.random') as random_sample:
        random_sample.sample.return_value = [{'function': 'parse'}, {'function': 'copy'}, {'function': 'test'}]
        parse_commands, copy_commands, functional_commands, random_commands = python_test.main()
        assert len(random_commands) == 3
