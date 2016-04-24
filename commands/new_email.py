from classes import *
from helper_functions import *

def method(servers_and_threads):
    """
    The most common reason to add your own command is to make a shortcut to do multiple commands.
    To run another command, type "command.Command.run_command(servers_and_threads, <command_name>)" below.
    Remember to pass in the dictionary servers_and_threads! All commands depend on it, and have it passed to them.
    If you want to write your own code that interacts with the spammer, you will have to understand how the spammer works and
    what the different functions do. All the code is modularized and somewhat commented, so it should not be too difficult. Classes are in
    the classes package, and helper functions are in the helper_functions package.
    """
    """Enter your code below here"""

command_object = command.Command("new_email", "Set up a new spam email", method)
