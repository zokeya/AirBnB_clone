#!usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
  """Class HBNBCommand"""
  prompt = "(hbnb) "

  def do_quit(self, line):
    "exit the program"
    return True

  def do_EOF(self, line):
    "exit the program"
    return True

if __name__ == '__main__':
  HBNBCommand().cmdloop()