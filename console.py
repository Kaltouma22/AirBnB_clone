#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        else:
            my_instance = BaseModel()
            my_instance.save()
            print(my_instance.id)

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        elif my_args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(my_args) == 1:
            print("** instance id missing **")
            return
        for key in storage.all():
            if storage.all()[key].id == my_args[1]:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, args):
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        elif my_args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(my_args) == 1:
            print("** instance id missing **")
            return
        else:
            instance_id = my_args[1]
            attribute_name = str(my_args[2])
            attribute_value = str(my_args[3])

            for key in storage.all():
                if key.split('.')[1] == instance_id:
                    instance = storage.all()[key]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
                    return

            print("** no instance found **")

    def do_all(self, args):
        my_args = args.split()
        class_name = my_args[0]
        if len(my_args) == 0 and class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            list_of_args = []
            for key in storage.all():
                list_of_args.append(str(storage.all()[key]))
            print(list_of_args)

    def do_EOF(self, arg):
        """Exit the program by typing EOF """
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
