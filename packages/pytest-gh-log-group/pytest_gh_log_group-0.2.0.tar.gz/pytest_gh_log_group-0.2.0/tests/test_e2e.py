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

    
@pytest.fixture(scope='function', params=[], ids=['p1', 'p2'])
def test_setup_with_parameters(request):
    print(f'test_setup_with_parameters {request.param}')
    yield
    print('after test_setup_with_parameters')


def test_sample1(session_setup, test_setup):
    print('test#1')


def test_sample2(session_setup, test_setup):
    print('test#2')


@pytest.mark.parametrize("param1",
                         argvalues=[1.1,])
def test_test_parameter(session_setup, param1):
    print('test#3 test_fixture_parameter')


@pytest.mark.parametrize("test_setup_with_parameters",
                         argvalues=[{'param1': 1.1, 'param2': 'parameter2 from test'}],
                         indirect=True, ids=['params'])
def test_fixture_parameter(session_setup, test_setup_with_parameters):
    print('test#4 test_fixture_parameter')


def test_fail():
    pytest.xfail(reason='testing failure')
    assert False, 'failed'
