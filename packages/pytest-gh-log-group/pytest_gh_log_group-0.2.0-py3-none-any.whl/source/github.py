""" Github log commands """
from _pytest.terminal import TerminalReporter


class Github:
    """ Github cli command handler """
    def __init__(self, reporter: TerminalReporter):
        """ Constructor for Github """
        self._reporter = reporter

        # GitHub doesn't support nested grouping so this ensures we do not have any.
        self._active_group = None

    def write_command(self, command: str, value: str = "") -> None:
        """ Github command prints"""
        self.write_line(f'::{command}::{value}')

    def write_line(self, data: str):
        """ write line using reporter """
        if self._reporter:
            self._reporter.ensure_newline()
            self._reporter.write_line(data, flush=True)


    def start_github_group(self, name: str, prefix="", postfix="") -> None:
        """
        Starts a log group in Github Actions Log
        """
        self.end_github_group()  # GitHub doesn't support nested grouping
        value = f'{prefix} {name} {postfix}'.strip(" ")
        self.write_command('group', value)
        self._active_group = value

    def end_github_group(self) -> None:
        """
        Ends a log group in Github Actions Log
        """
        if not self._active_group:
            # GitHub doesn't support nested grouping
            return
        if self._reporter:
            self._reporter.line('')
        self.write_command('endgroup')
        self._active_group = None
