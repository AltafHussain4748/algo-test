from unittest.mock import patch

import python_test


def test_none_value():
    with patch('python_test.json') as data:
        data.loads.return_value = None
        try:
            python_test.main()
            assert False
        except TypeError:
            assert True
