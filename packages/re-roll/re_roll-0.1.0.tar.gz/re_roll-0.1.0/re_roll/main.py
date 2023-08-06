# YES, I am aware that there is a multi-file solution. I don't care!

import os, argparse, random
from sys import argv, exit

from . import AFormat
from . import EncounterFolderEmptyError, EncounterParseError
from . import seperate_c_from_t, build_dict_of_tables, get_longest_string_len, validate_brackets, parse_encounter

# re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/11/22
# ----------------------------------
# file: re_roll_list.py
# List all the valid tables you can roll from in a directory. When ANSI is enabled (by default), "collections,"
# or folders that contain subfolders, are highlighted. "tables," or folders that contain no subfolders are outputted
# with the default terminal color. By default, "empty" tables are shown by the program, but you can disable this.

def create_group_string(dictionary, no_escape, width, print_mode):
    string = ""
    longest_string = get_longest_string_len(dictionary.keys())

    collections, tables = seperate_c_from_t(dictionary, print_mode)

    i = 0
    for name in sorted(collections):
        i += 1
        if not no_escape:
            string += AFormat.CYN
        string += name
        if not no_escape:
            string += AFormat.NORM
        if i % (width) == 0:
            string += '\n'
        else:
            for _ in range(0, longest_string - len(name)):
                string += ' '
            string += '\t'

    for name in sorted(tables):
        i += 1
        string += name
        if i % (width) == 0:
            string += '\n'
        else:
            for _ in range(0, longest_string - len(name)):
                string += ' '
            string += '\t'

    return string



def create_list_string(dictionary, no_escape, show_directory, print_mode):
    string = ""
    if show_directory:
        longest_string = get_longest_string_len(dictionary.keys())

    collections, tables = seperate_c_from_t(dictionary, print_mode)

    for name in sorted(collections):
        if not no_escape:
            string += AFormat.CYN
        string+= name
        if not no_escape:
            string += AFormat.NORM
        if show_directory:
            for _ in range(0, longest_string - len(name)):
                string += ' '
            string += '\t: '
            string += dictionary[name]
        string += '\n'

    for name in sorted(tables):
        string+= name
        if show_directory:
            for _ in range(0, longest_string - len(name)):
                string += ' '
            string += '\t: '
            string += dictionary[name]
        string += '\n'

    return string

def re_roll_ls(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default = None, help="the folder to roll from")
    parser.add_argument("-t", "--table", default = None, help= "specify a table by name.")
    parser.add_argument("--no_escape", action="store_true", help= "disable ANSI color codes.")
    parser.add_argument("-m", "--mode", choices=["group", "g", "list", "l"], default="group", help="determine if the possible tables are simply printed out one-by-one, or grouped together")
    parser.add_argument("-p", "--print_what", choices=["all", "a", "only_tables", "ot", "only_collections", "oc", "nothing"], default="all", help="specify what to print (only tables or only collections)")
    parser.add_argument("--width", type=int, default=4, help="change the number of columns that get printed before a new row is started in group mode")
    parser.add_argument("--show_directory", action="store_true", help="if enabled, the outputted list will include the directory of every table in list mode")
    parser.add_argument("--hide_empty", action="store_true", help="if enabled, all tables containing neither files nor directories will be hidden")
    args = parser.parse_args(args)

    directory = None
    if args.dir == None:
        directory = os.getcwd()
    else:
        directory = os.path.join(args.dir, "")
        if not os.path.isdir(directory):
            if args.print_what != "nothing":
                print("Error: The directory at " + directory + " could not be found.")
            exit(-1)

    if args.table != None:
        dictionary = build_dict_of_tables(directory)
        if args.table in dictionary:
            directory = os.path.join(dictionary[args.table], "")
        else:
            if args.print_what != "nothing":
                print("Error: " + args.table + " not found in the directory.\nTry running the program with the -l or --list command to see a list of available table names.")
            exit(-1)

    dictionary = build_dict_of_tables(directory, args.print_what, args.hide_empty)


    text = None
    if args.mode == "group" or args.mode == "g":
        text = create_group_string(dictionary, args.no_escape, args.width, args.print_what)
    else:
        text = create_list_string(dictionary, args.no_escape, args.show_directory, args.print_what)

    print(text)

# re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/11/22
# ----------------------------------
# file: re_roll.py
# A module that rolls from a random encounter table as part of the re-roll package. The module prints one random encounter to the command line.

def roll(directory, quiet_mode, no_ANSI_mode):
    random.seed()
    table = []

    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,entry)) and entry.endswith(".txt"):
            table.append(os.path.join(directory, entry))
        elif os.path.isdir(os.path.join(directory,entry)):
            table.append(os.path.join(os.path.join(directory,entry),""))


    if len(table) == 0:
        raise EncounterFolderEmptyError

    random.shuffle(table)
    random.seed()
    _roll = random.randint(0, len(table) - 1)
    selection = table[_roll]
    rollformat = None
    if no_ANSI_mode:
        rollformat = "1d" + str(len(table)) + "=" + str(_roll + 1)
    else:
        clr = None
        if _roll + 1 == 1:
            clr = AFormat.RED
        elif _roll + 1 == len(table):
            clr = AFormat.GRN
        else:
            clr = ''

        rollformat = AFormat.BOLD + AFormat.CYN + "1d" + str(len(table)) + "=" + clr + str(_roll + 1) + AFormat.NORM

    if selection.endswith('.txt'):
        if not quiet_mode:
            print(os.path.basename(selection) + "(" + rollformat + ")\n")
        return parse_encounter(selection, no_ANSI_mode)
    else:
        if not quiet_mode:
            print(os.path.basename(selection[:-1]) + "(" + rollformat + ")>", end="")
        return roll(selection, quiet_mode, no_ANSI_mode)

def re_roll_roll(args):


    parser = argparse.ArgumentParser(prog="re-roll roll")
    parser.add_argument("-d", "--dir", default = None, help="the folder to roll from")
    parser.add_argument("-t", "--table", default = None, help= "specify a table by name.")
    parser.add_argument("--quiet", action='store_true', help="the program will only print out the output of the random encounter, and no superfluous details")
    parser.add_argument("--no_escape", action='store_true', help="the program will not attempt to format the text using ANSI codes, if for some reason your output is broken because of ANSI")

    args = parser.parse_args(args)

    directory = None
    if args.dir == None:
        directory = os.getcwd()
    else:
        directory = os.path.join(args.dir, "")
        if not os.path.isdir(directory):
            print("Error: The directory at " + directory + " could not be found.")
            exit(-1)

    if args.table != None:
        dictionary = build_dict_of_tables(directory)
        if args.table in dictionary:
            directory = os.path.join(dictionary[args.table], "")
        else:
            print("Error: " + args.table + " not found in the directory.\nTry running the program with the -l or --list command to see a list of available table names.")
            exit(-1)

    text = None
    try:
        text = roll(directory, args.quiet, args.no_escape)
    except EncounterFolderEmptyError:
        print("Error: The encounter folder that was traversed to was empty. Fill it up with an encounter, other folders, or delete it.")
        exit(-1)
    except EncounterParseError:
        print("Error: The encounter parser had trouble reading a file. Check that the selected file has balanced {} and [] brackets.")
        exit(-1)

    print(text)

# Help me is a "built in" module that calls the help function of a module you request, so
# long as it is in the above modules dict.
def help_me(args):
    help_parser = argparse.ArgumentParser(prog="re-roll help")
    help_parser.add_argument('module', choices=valid_modules.modules.keys(), help="the module you would like to get help on")
    args = help_parser.parse_args(args)

    spoof_arg = [ '-h' ]

    valid_modules.modules[args.module](spoof_arg)
    exit(0)

# Here, we declare a dict of module names that map to entry point functions in other modules.
# This makes it incredibly trivial to extend this program with new modules, or to modify the
# functionality of the existing modules as long as we don't change the module's contract.
class valid_modules:
    modules =  {
        'list' : re_roll_ls,
        'roll' : re_roll_roll
    }

# re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/11/22
# ----------------------------------
# file: main.py
# A program that acts as a hub for the various modules associated with the re-roll package. You can call any of the
# supported modules as declared in the valid_modules class below, as well as a help module that calls the help command
# line option of any module you feed it.

# The main entry point of the program. Can choose between any modules in the above modules
# dict, as well as the built in help_me module.
def main():
    usage_message = (
        "usage: re-roll [-h] {help,list,roll}\n\n"
        "positional arguments:\n"
        "  {help,list,roll}\tthe module you would like to use\n\n"
        "options:\n"
        "  -h, --help\tshow this message and exit"
    )

    if argv == None:
        print(usage_message)

    if len(argv) == 1:
        print(usage_message)
        exit(0)

    which_module = [argv[1]]
    other_args = []

    for i in range(2, len(argv)):
        other_args.append(argv[i])

    modules_and_help = ["help"]
    for key in valid_modules.modules:
        modules_and_help.append(key)

    module_parser = argparse.ArgumentParser(prog="re-roll")
    module_parser.add_argument('module', choices=modules_and_help, help="the module you would like to use")
    module_parser.parse_args(which_module)
    args = module_parser.parse_args(which_module)

    # This is a bit of a tricky piece of code here, but it improves extensibility.
    # The values in the modules dict declared at the start of this file after imports all refer
    # to a method that acts as an entry point for a module.
    # Therefore, by accessing the key declared by args.module as parsed by argparse, which will always be in modules
    # since only valid modules are choices we can call the function it maps to.
    # The ternary operator (statement1 if boolean else statement2) is used to handle the one exception to this rule,
    # the case of the built in help module.
    # If this line still doesn't make sense, I'm sorry. Make a fork or something.
    valid_modules.modules[args.module](other_args) if args.module != "help" else help_me(other_args)

if __name__ == "__main__":
    main()
