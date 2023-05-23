#!usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
  """Class HBNBCommand"""
  prompt = "(hbnb) "

  def do_quit(self, line):
    "Quit command to exit the program"
    return True

  def do_EOF(self, line):
    "EOF to exit the program"
    return True

  def emptyline(self):
    "Do nothing with empty line"
    pass

if __name__ == '__main__':
  HBNBCommand().cmdloop()