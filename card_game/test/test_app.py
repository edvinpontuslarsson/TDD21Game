import sys
import app


sys.path.insert(0, '../app')


def test_ping_should_pong():
    assert app.ping() == 'pong'
