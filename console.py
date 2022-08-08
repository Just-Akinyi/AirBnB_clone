#!/usr/bin/python3
"""The entry point of the command interpreter"""

import cmd
import shlex
from signal import signal, SIGINT
from sys import exit
import models
from models.base_model import BaseModel
from models import storage
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
        elif len(args) == 1 and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in HBNBCommand.classes.keys():
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            keys = args[0] + '.' + args[1]
            if keys in instances:
                print(instances[keys])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        className = line.split()

        if len(className) == 0:
            print("** class name missing **")
            return
        elif className[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(className) == 1:
            print("** instance id missing **")
        else:
            instances = className[0] + "." + className[1]
            if instances in models.storage.all():
                del models.storage.all()[instances]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, classNam):
        """Print a string of an instance based on class name"""
        args = classNam.split(" ")
        if args[0] == "" or args[0] in HBNBCommand.classes:
            string = []
            objs = storage.all()
            for key in objs.keys():
                if args == [''] or key.split(".")[0] == args[0]:
                    string.append(str(objs[key]))
            print(string)
        else:
            print("** class doesn't exist **")

    def do_update(self, className):
        """Updates an instance based on the class name"""

        className = shlex.split(className)

        if len(className) == 0:
            print("** class name missing **")
            return
        if className[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist *+")
            return
        if len(className) == 1:
            print("** instance id missing **")
            return
        args = className[0] + '.' + className[1]
        if args not in models.storage.all():
            print("** no instance found **")
            return
        if len(className) == 2:
            print("** attribute name missing **")
            return
        if len(className) == 3:
            print("** value missing **")
            return
        attr = className[2]
        value = className[3]
        objs = storage.all()
        id = className[0] + "." + className[1]
        objs[id][attr] = value
        models.storage.update_obejts(objs)


if __name__ == '__main__':
    signal(SIGINT, HBNBCommand.handler)
    HBNBCommand().cmdloop()
