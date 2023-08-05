# Topydo - A todo.txt client written in Python.
# Copyright (C) 2014 - 2015 Bram Schoenmakers <me@bramschoenmakers.nl>
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

""" Entry file for the Python todo.txt CLI. """

import getopt
import sys

def usage():
    """ Prints the command-line usage of topydo. """

    print """\
Synopsis: topydo [-c <config>] [-d <archive>] [-t <todo.txt>] subcommand [help|args]
          topydo -h
          topydo -v

-c : Specify an alternative configuration file.
-d : Specify an alternative archive file (done.txt)
-h : This help text
-t : Specify an alternative todo file
-v : Print version and exit

Available commands:

* add
* append (app)
* del (rm)
* dep
* depri
* do
* edit
* ical
* ls
* listcon (lscon)
* listprojects (lsprj)
* postpone
* pri
* sort
* tag

Run `topydo help <subcommand>` for command-specific help.
"""

    sys.exit(0)

def write(p_file, p_string):
    """
    Write p_string to file p_file, trailed by a newline character.

    ANSI codes are removed when the file is not a TTY.
    """
    if not p_file.isatty():
        p_string = escape_ansi(p_string)

    if p_string:
        p_file.write(p_string + "\n")

def error(p_string):
    """ Writes an error on the standard error. """

    write(sys.stderr, p_string)

def version():
    """ Print the current version and exit. """
    from topydo.lib.Version import VERSION, LICENSE
    print "topydo {}\n".format(VERSION)
    print LICENSE
    sys.exit(0)

from topydo.lib.Config import config, ConfigError

# First thing is to poke the configuration and check whether it's sane
# The modules below may already read in configuration upon import, so
# make sure to bail out if the configuration is invalid.
try:
    config()
except ConfigError as config_error:
    error(str(config_error))
    sys.exit(1)

from topydo.lib.Commands import get_subcommand
from topydo.lib.ArchiveCommand import ArchiveCommand
from topydo.lib.SortCommand import SortCommand
from topydo.lib import TodoFile
from topydo.lib import TodoList
from topydo.lib import TodoListBase
from topydo.lib.Utils import escape_ansi

class CLIApplication(object):
    """
    Class that represents the Command Line Interface of Topydo.

    Handles input/output of the various subcommand.
    """
    def __init__(self):
        self.todolist = TodoList.TodoList([])

        self.config = config()
        self.path = self.config.todotxt()
        self.archive_path = self.config.archive()

    def _process_flags(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "c:d:ht:v")
        except getopt.GetoptError as e:
            error(str(e))
            sys.exit(1)

        alt_path = None
        alt_archive = None

        for opt, value in opts:
            if opt == "-c":
                self.config = config(value)
            elif opt == "-t":
                alt_path = value
            elif opt == "-d":
                alt_archive = value
            elif opt == "-v":
                version()
            else:
                usage()

        self.path = alt_path if alt_path else self.config.todotxt()
        self.archive_path = alt_archive \
            if alt_archive else self.config.archive()

        return args

    def _archive(self):
        """
        Performs an archive action on the todolist.

        This means that all completed tasks are moved to the archive file
        (defaults to done.txt).
        """
        archive_file = TodoFile.TodoFile(self.archive_path)
        archive = TodoListBase.TodoListBase(archive_file.read())

        if archive:
            command = ArchiveCommand(self.todolist, archive)
            command.execute()

            if archive.is_dirty():
                archive_file.write(str(archive))

    def _help(self, args):
        if args == None:
            pass # TODO
        else:
            pass # TODO

    def _execute(self, p_command, p_args):
        """
        Execute a subcommand with arguments. p_command is a class (not an
        object).
        """
        command = p_command(
            p_args,
            self.todolist,
            lambda o: write(sys.stdout, o),
            error,
            raw_input)

        return False if command.execute() == False else True

    def run(self):
        """ Main entry function. """
        args = self._process_flags()

        todofile = TodoFile.TodoFile(self.path)
        self.todolist = TodoList.TodoList(todofile.read())

        (subcommand, args) = get_subcommand(args)

        if subcommand == None:
            usage()

        if self._execute(subcommand, args) == False:
            sys.exit(1)

        if self.todolist.is_dirty():
            self._archive()

            if config().keep_sorted():
                self._execute(SortCommand, [])

            todofile.write(str(self.todolist))

def main():
    """ Main entry point of the CLI. """
    CLIApplication().run()

if __name__ == '__main__':
    main()
