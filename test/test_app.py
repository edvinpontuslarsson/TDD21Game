import os
import sys

currentWorkingDirectory = os.getcwd()
sys.path.append(currentWorkingDirectory + '/card_game/')

import app


# TODO: use unittest instead
def test_ping_should_pong():
    assert app.ping() == 'pong'

