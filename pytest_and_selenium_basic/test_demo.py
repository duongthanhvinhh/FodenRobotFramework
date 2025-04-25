# With pytest, any test file should start with `test_` or end with `_test`
# With pytest, the class name should start with Test, like TestDemo
# With pytest, any method should start with `test`
import sys

import pytest


@pytest.mark.smoke
def test_greeting():
    print("Hello friends")

@pytest.mark.smoke
def test_final_price():
    print(7)

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_print_full_name(setup_and_teardown):
    print("Duong Thanh Vinh")


@pytest.mark.xfail
# @pytest.mark.skip
def test_assert_two_messages():
    first_msg = "Foden"
    second_msg = "Vinh"
    assert first_msg == second_msg

@pytest.fixture()
def setup_and_teardown():
    print("Hello guys, welcome to pytest!")
    yield
    print("Goodbye, see you later")