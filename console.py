#!/usr/bin/python3
"""
command line console
"""
import cmd
import json
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """console class"""
    intro = "Welcome to Chisom's shell. Type help or ? to list commands.\n"
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quits the console"""
        return True
    
    def do_EOF(self, arg):
        """at EOF, quit console"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
