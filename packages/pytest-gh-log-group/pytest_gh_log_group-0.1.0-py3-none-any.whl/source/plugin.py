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
        default=_strtobool(os.getenv('GITHUB_ACTIONS')),
        help="Time in milliseconds when the print was invoked, "
             "relative to the time the fixture was created.",
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


@pytest.hookimpl(tryfirst=True)
def pytest_collection(session: Session):  # pylint: disable=unused-argument
    """ Start files/folders collection"""
    pytest.grouping_session.start_github_group('collector')


@pytest.hookimpl(trylast=True)
def pytest_collection_finish(session):  # pylint: disable=unused-argument
    """ Collection finish """
    pytest.grouping_session.end_github_group()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item) -> None:
    """
    Start group "TestName TEST"
    """
    pytest.grouping_session.start_github_group(item.name, prefix="TEST")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report: TestReport):  # pylint: disable=unused-argument
    """ end group between tests/setups/teardown phases"""
    pytest.grouping_session.end_github_group()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item) -> None:
    """
    Start group "TEST TestName SETUP"
    """
    pytest.grouping_session.start_github_group(item.name, prefix="TEST", postfix="SETUP")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item) -> None:
    """
    Start group "TEST TestName TEARDOWN"
    """
    pytest.grouping_session.write_line('')
    pytest.grouping_session.start_github_group(item.name, prefix="TEST", postfix="TEARDOWN")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_fixture_setup(request, fixturedef) -> None:
    """
    Start group "FIXTURE FixtureName"
    """
    fixture_type = f'FIXTURE ({fixturedef.scope})'
    fixture_name = request.fixturename
    request_param = request.param
    param_marks = list(filter(lambda m: m.name == 'parametrize',
                              request.node.own_markers))
    if any(param_marks):
        pmark = param_marks[0]
        if pmark is not None and fixture_name in pmark.args[0].split(','):
            # this "fixture" is a pytest parameterize mark
            fixture_type = 'PARAMETER'
            fixture_name = f'{fixture_name} {request_param}'

    pytest.grouping_session.start_github_group(prefix=fixture_type,
                       name=fixture_name,
                       postfix='SETUP')

    # yield fixture to insert fixture_finalizer at the
    # end of finalizers list (--> executed first)
    yield

    pytest.grouping_session.end_github_group()
