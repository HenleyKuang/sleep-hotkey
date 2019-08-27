import keyboard
import pytest
import time

from unittest.mock import patch

from sleep_hotkey.sleep_hotkey import sleep


def test_calling_sleep():
    """
    Test no errors simply calling sleep
    """
    try:
        sleep(1)
    except Exception as e:
        pytest.fail("Exception raised: %s" % e)


def test_sleep_and_press_hotkey():
    """
    Test hotkey stops sleeping
    """
    with patch('keyboard.is_pressed') as mock_is_pressed:
        mock_is_pressed.return_value = True
        start_time = time.time()
        sleep(10, exit_key='esc')
        end_time = time.time()
        elapsed_time = start_time - end_time
        if elapsed_time > 5:
            pytest.fail("Fail to end sleep with artificial keypress trigger")
