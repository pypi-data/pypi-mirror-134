# Copyright (C) 2019-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from contextlib import contextmanager
from enum import Enum
from shutil import get_terminal_size
from typing import Callable, Generator

import colorful as cf

TERMINAL_SIZE_FALLBACK = (80, 24)  # use a small standard size as fallback


class Signs(Enum):
    FAIL = '\N{HEAVY MULTIPLICATION X}'
    ERROR = '\N{MULTIPLICATION SIGN}'
    WARNING = '\N{WARNING SIGN}'
    OK = '\N{CHECK MARK}'
    INFO = '\N{INFORMATION SOURCE}'
    NONE = ' '

    def __str__(self):
        return f'{self.value}'


STATUS_LEN = 2


class Terminal:
    def __init__(self):
        self._indent = 0

    @staticmethod
    def get_width() -> int:
        """
        Get the width of the terminal window
        """
        width, _ = get_terminal_size(TERMINAL_SIZE_FALLBACK)
        return width

    def _print_status(
        self,
        message: str,
        status: Signs,
        color: Callable,
        style: Callable,
        *,
        new_line: bool = True,
        overwrite: bool = False,
    ) -> None:
        first_line = ''
        if overwrite:
            first_line = '\r'
        output = ''
        width = self.get_width()
        if status == Signs.NONE:
            first_line += '  '
        else:
            first_line += f'{color(status)} '
        if self._indent > 0:
            first_line += ' ' * self._indent
        usable_width = width - STATUS_LEN - self._indent
        while usable_width < len(message):
            part_line = ' ' * (self._indent + STATUS_LEN)
            part = message[:usable_width]
            message = message[usable_width:]
            output += f'{part_line}{part}\n'
        output += f'{first_line}{message}'
        if new_line:
            print(style(output))
        else:
            print(style(output), end='', flush=True)

    @contextmanager
    def indent(self, indentation: int = 4) -> Generator:
        current_indent = self._indent
        self.add_indent(indentation)

        yield self

        self._indent = current_indent

    def add_indent(self, indentation: int = 4) -> None:
        self._indent += indentation

    def reset_indent(self) -> None:
        self._indent = 0

    def print(self, *messages: str, style: Callable = cf.reset) -> None:
        message = ''.join(messages)
        self._print_status(message, Signs.NONE, cf.white, style)

    def print_overwrite(
        self, *messages: str, style: Callable = cf.reset, new_line: bool = False
    ) -> None:
        message = ''.join(messages)
        self._print_status(
            message,
            Signs.NONE,
            cf.white,
            style,
            new_line=new_line,
            overwrite=True,
        )

    def ok(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message, Signs.OK, cf.green, style)

    def fail(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message, Signs.FAIL, cf.red, style)

    def error(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message, Signs.ERROR, cf.red, style)

    def warning(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message, Signs.WARNING, cf.yellow, style)

    def info(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message, Signs.INFO, cf.cyan, style)

    def bold_info(self, message: str, style: Callable = cf.bold) -> None:
        self._print_status(message, Signs.INFO, cf.cyan, style)
