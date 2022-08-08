#!/usr/bin/python3
"""The entry point of the command interpreter"""

import cmd
from signal import signal, SIGINT
from sys import exit
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

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

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg in HBNBCommand.classes.keys():
            instance = HBNBCommand.classes[arg]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif (len(args) == 1 and args in HBNBCommand.classes.keys()):
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            keys = args[0] + '.' + args[1]
            if keys in instances:
                print(instances[keys])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    signal(SIGINT, HBNBCommand.handler)
    HBNBCommand().cmdloop()
