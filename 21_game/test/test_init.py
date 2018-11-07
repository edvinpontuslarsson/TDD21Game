import sys
import __init__


sys.path.insert(0, '../21_game/app')


def test_ping_should_pong():
    assert __init__.ping() == 'pong'
