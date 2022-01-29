#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import sys
import re
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def rearrange(arg):
    """Helps to rearrange the argument for
    console command use.
    """
    pro = re.compile(r'\b(\W+)+')
    pro2 = re.compile(r'(?<=(\(\")).*[^("\)]')
    result = pro.split(arg)

    if result is not None:
        clsName = result[0]
        command = result[2]

        result2 = pro2.search(arg)
        if result2 is not None:
            argv = clsName + " " + result2.group()
        else:
            argv = clsName
        return (argv, command)
    else:
        return (result, None)



class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

 # prompt for interactive/non-interactive section 
  prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
 # classes that can be created
    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }


    attr_types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def help_quit(self):
        '''prints the documentation for the command quit'''
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits Console"""
        print()
        return True

     def help_EOF(self):
        """ Prints the documentation for EOF """
        print("The EOF exits the program\n")

    def emptyline(self):
        """Overwrites the emptyline command\n"""
        pass

    def do_create(self, arg):
       """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
     if arg 
        if arg not in self.__classes:
         print("** class doesn't exist **")
     else:
                for keys in self.__classes:
                    if arg == keys:
                        arg = eval(arg)()
                        arg.save()
                        print(arg.id)
      else:
          print("** class name missing **")
          
     def help_create(self):
        """ prints Documentation for the create command """
        print("creates a new instance of the class passed as argument")
        print("[Usage]: create <className>\n")
     
    def do_show(self, arg):
          """Prints the string representation of an instance based on the class name and id usage
          """
       if arg:
            if len(arg.split()) > 1:

                arg1 = arg.split()[0]
                arg2 = arg.split()[1]
                argc = arg1 + "." + arg2
                if arg1 not in self.__classes:
                    print("** Class doesn't exist **")
                elif arg2:
                    ids = storage.all()
                    if argc in ids.keys():
                        print(ids[argc])
                    else:
                        print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** Class name missing **")
        
     def help_show(self):
        """ prints documentation for the show command """
        print("prints the string representation of an instance")
        print("[Usage]: show <className> <objectId>\n")

     def do_destroy(self, arg):
           """Deletes an instance based on the class name and id"""
        if arg:
            if len(arg.split()) > 1:

                arg1 = arg.split()[0]
                arg2 = arg.split()[1]
                argc = arg1 + "." + arg2
                if arg1 not in self.__classes:
                    print("** Class doesn't exist **")
                elif arg2:
                    ids = storage.all()
                    if argc in ids.keys():
                        del(ids[argc])
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** Class name missing **")

    def help_destroy(self):
        ''' prints documentaion for the destroy command '''
        print("Deletes an instance based on the class name and id")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, arg):
             """Prints all string representation of all instances based or not on the class name
             """
          if arg:
            if arg not in self.__classes:
                print("** class doesn't exist **")
            else:
                obj = storage.all()
                for val in obj.values():
                    print(val)
        else:
            obj = storage.all()
            for val in obj.values():
                print(val)

   def help_all(self):
        ''' prints documentaion for the all command '''
        print("Prints all string representation of all instances")
        print("based or not on the class name")
        print("[Usage]: all <className>\n")              

   def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change to the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if arg:
            ar = arg.split()
            length = len(ar)
            if length >= 4:
                clName = ar[0]
                if clName not in self.__classes:
                   print("** class doesn't exist **")
                else:
                    id = ar[1]
                    attr = ar[2]
                    attr_value = arg.split('"')[1]
                    class_tag = clName + "." + id
                    obj = storage.all()
                    if class_tag in obj.keys():
                        model_instance = obj[class_tag]
                        setattr(model_instance, attr, attr_value)
                        model_instance.save()
                    else:
                        print("** no instance found **")
            elif length == 3:
                print("** value missing **")
            elif length == 2:
                print("** attribute name missing **")
            elif length == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

     def help_update(self):
        """ prints Documentation for the update command """
        print("Updates an object's attributes")
        print("Usage: update <className> <id> <attName> <attVal>\n")
        
    def count_inst(self, arg):
        """This prints all string representation of the all instances
        based on or not the class name
        """
        if arg.split(".")[0] not in self.__list:
            print("** Class doesn't exist **")
        else:
            obj = storage.all()
            count = 0
            for key in obj.keys():
                if arg.split(".")[0] == key.split(".")[0]:
                    count = count + 1
            print(count)

    def help_count(self):
        """ prints the documentation of the count command"""
        print("Usage: count <class_name>")

    def do_all2(self, arg):
        """This prints all string representation of the all instances
        based on or not the class name
        """
        obj = storage.all()
        count = 0
        for key, val in obj.items():
            if arg.split(".")[0] == key.split(".")[0]:
                count = count + 1
                print(val)    

    def default(self, arg):
        """Let shell to use flags and short hand\n"""

        comm = {"show": "self.do_show",
                "create": "self.do_create",
                "destroy": "self.do_destroy",
                "update": "self.do_update"
                }

        if arg == 'q' or arg == 'x':
            self.do_quit(arg)
        elif re.search(r'\.', arg) is not None:
            if arg.split(".")[0] in self.__list \
                    and arg.split(".")[1] == "all()":
                self.do_all2(arg)
            elif arg.split(".")[1] == "count()":
                self.count_inst(arg)
            elif arg.split(".")[0] in self.__classes:
                newarg, command = rearrange(arg)
                if newarg is not None:
                    for key, val in comm.items():
                        if command == key:
                            eval(val)(newarg)
                else:
                    cmd.Cmd.default(self, arg)
            else:
                cmd.Cmd.default(self, arg)
        else:
            cmd.Cmd.default(self, arg)

     if __name__ == '__main__':
        HBNBCommand().cmdloop()
             
