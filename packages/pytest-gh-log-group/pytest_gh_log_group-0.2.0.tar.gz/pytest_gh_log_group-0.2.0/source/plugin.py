"""
Pytest plugin for github action log grouping.
"""
import os
import pytest
from _pytest.config import _strtobool
from _pytest.config import Config
from _pytest.reports import TestReport
from _pytest.main import Session
from _pytest.config.argparsing import Parser
from .github import Github


TERMINAL_REPORT = None


def pytest_addoption(parser: Parser) -> None:
    """ Initialize argument parsing. """
    group = parser.getgroup("pytest_gh_log_group")
    group.addoption(
        "--gh_log_group",
        action="store_true",
        dest="gh_log_group",
        default=_strtobool(os.getenv('GITHUB_ACTIONS', "False")),
        help="Enable Github Actions log grouping",
    )


@pytest.hookimpl(trylast=True)
def pytest_configure(config: Config):
    """ Initilize Github command printer """
    pytest.grouping_session = create(config)


def create(config: Config) -> Github:
    """ Create object """
    if config.getoption("gh_log_group"):
        terminal_reporter = config.pluginmanager.getplugin("terminalreporter")
        return Github(reporter=terminal_reporter)
    return Github(reporter=None)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_collection(session: Session):  # pylint: disable=unused-argument
    """ Start files/folders collection"""
    pytest.grouping_session.start_github_group('collector')
    yield


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_collection_finish(session):  # pylint: disable=unused-argument
    """ Collection finish """
    yield
    pytest.grouping_session.end_github_group()

@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_sessionfinish(session):  # pylint: disable=unused-argument
    """ Session finish """
    yield
    pytest.grouping_session.end_github_group()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item) -> None:
    """
    Start group "TestName TEST"
    """
    pytest.grouping_session.start_github_group(item.name, prefix="TEST")
    yield


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_logreport(report: TestReport):  # pylint: disable=unused-argument
    """ end group between tests/setups/teardown phases"""
    yield
    pytest.grouping_session.end_github_group()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item) -> None:
    """
    Start group "TEST TestName SETUP"
    """
    pytest.grouping_session.start_github_group(item.name, prefix="TEST", postfix="SETUP")
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item) -> None:
    """
    Start group "TEST TestName TEARDOWN"
    """
    pytest.grouping_session.start_github_group(item.name, prefix="TEST", postfix="TEARDOWN")
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_fixture_setup(request, fixturedef) -> None:
    """
    Start group "FIXTURE FixtureName" or "PARAMETER parameter name"
    """
    fixture_type = f'FIXTURE ({fixturedef.scope})'
    request_param = request.param if hasattr(request, 'param') else ''
    fixture_name = f'{request.fixturename} {request_param}'.strip(' ')

    param_marks = list(filter(lambda m: m.name == 'parametrize',
                              request.node.own_markers))
    if any(param_marks):
        pmark = param_marks[0]
        if pmark is not None:
            # this "fixture" is a pytest parametrize mark
            # AND the parametrize mark is not targeting a fixture
            if request.fixturename in pmark.args[0].split(',') \
                    and not pmark.kwargs.get('indirect', False):
                fixture_type = 'PARAMETER'


    pytest.grouping_session.start_github_group(prefix=fixture_type,
                       name=fixture_name,
                       postfix='SETUP')

    # yield fixture to insert fixture_finalizer at the
    # end of finalizers list (--> executed first)
    yield

    def _fixture_finalizer():
        """
        Start group "FIXTURE FixtureName TEARDOWN
        """
        pytest.grouping_session.start_github_group(prefix=fixture_type, name=fixture_name,
                                                   postfix='TEARDOWN')

    fixturedef.addfinalizer(_fixture_finalizer)

    # insert "end group" finalizer to _finalizer list: index 0 (--> executed last)
    fixturedef._finalizers.insert(0, pytest.grouping_session.end_github_group) # pylint: disable=protected-access
