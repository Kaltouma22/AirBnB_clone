#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """Exit the program by typing EOF (Ctrl+D on Linux, Ctrl+Z on windows)"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
