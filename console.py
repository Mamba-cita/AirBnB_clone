import cmd
import re
import shlex
import ast

class HBNBCommand(cmd.Cmd):


   def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True
   
   
