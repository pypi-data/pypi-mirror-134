import pytest


@pytest.fixture(scope='session', params=[""])
def session_setup():
    print('session_setup')
    yield
    print('after session_setup')


@pytest.fixture(scope='function', params=[""])
def test_setup():
    print('test_setup')
    yield
    print('after test_setup')


def test_sample1(session_setup, test_setup):
    print('test#1')


def test_sample2(session_setup, test_setup):
    print('test#2')


def test_fail():
    pytest.xfail(reason='testing failure')
    assert False, 'failed'
