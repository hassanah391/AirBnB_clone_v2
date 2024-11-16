#!/usr/bin/python3
"""

Module console is an entry point for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    def do_EOF(self, arg):
        """Quit the cmd at EOF
        """
        return True
    def emptyline(self):
        pass
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
