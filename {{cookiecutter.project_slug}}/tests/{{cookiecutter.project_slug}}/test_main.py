from unittest import mock

import pytest

from {{cookiecutter.project_slug}} import __main__


@mock.patch("sys.argv", "")
def test_main():
    with pytest.raises(SystemExit) as e:
        __main__.main()

        assert e.type ==SystemExit
        assert e.value.code == 0
