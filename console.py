#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import string
import shlex

class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City", "Review", "Amenity",
               "Place"}

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, args):
        '''
            Create a new instance of class BaseModel and saves it
            to the JSON file.
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            for i in args[1:]:
                try:
                    key = i.split("=")[0]
                    value = i.split("=")[1]
                    if hasattr(new_instance, key) is True:
                        value = value.replace("_", " ")
                        try:
                            value = eval(value)
                        except:
                            pass
                        setattr(new_instance, key, value)
                except (ValueError, IndexError):
                    pass
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = line.split()  # Split the input line into arguments
        if len(args) == 0:  # No arguments provided
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:  # Check if class exists
            print("** class doesn't exist **")
            return
        if len(args) == 1:  # No instance ID provided
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():  # Check if instance exists
            print("** no instance found **")
            return
        # Print the instance if found
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()  # Split the input line into arguments
        if len(args) == 0:  # No arguments provided
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:  # Check if class exists
            print("** class doesn't exist **")
            return
        if len(args) == 1:  # No instance ID provided
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():  # Check if instance exists
            print("** no instance found **")
            return
        # Delete the instance if found
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representations of all instances,
        optionally filtered by class name.

         Args:
        line (str): Input line containing the class name (optional).
         """
        if line and line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instances = []  # List to hold string representations of instances
        for key, obj in storage.all().items():  # Iterate over all stored objs
            if not line or key.startswith(f"{line}."):
                instances.append(str(obj))

        print(instances)  # Print the list of string representations

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = tuple(line.split())
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
