#!/usr/bin/python3
"""The entry point of the command interpreter"""

import cmd
from signal import signal, SIGINT
from sys import exit


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, *args):
        """Exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def handler(signal_received, frame):
        """Handle the SIGINT or CTRL-C signal"""
        print("^C")
        exit(0)


if __name__ == '__main__':
    signal(SIGINT, HBNBCommand.handler)
    HBNBCommand().cmdloop()
