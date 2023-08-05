#!/usr/bin/python
# re-roll.py
# A python program that traverses a directory and selects a random encounter. Recursively follows directories so that you can
# group related Random Encounters as folders. Alternatively, you can create a .idx  file that tabulates a directory and allows you to
# traverse by file name
import argparse
import os
from sys import argv, exit
import random


SEPERATING_CHAR = '\\' if os.name == "nt" else '/'

# A class that contains some ANSI escape sequences, for easier reading when used in code.
class aformat:
    NORM = '\033[0m'
    BOLD = '\033[1m'
    ITAL = '\033[3m'
    NOT_BOLD = '\033[22m'
    NOT_ITAL = '\033[23m'
    RED = '\033[31m'
    GRN = '\033[32m'
    CYN = '\033[32m'

class EncounterFolderEmptyError(Exception):
    def __init__(self, message="The encounter folder was empty."):
        super().__init__(message)

class EncounterParseError(Exception):
    def __init__(self, message="There was an error parsing the file."):
        super().__init__(message)


def build_dict_of_tables(directory):
    dictionary = {}
    for list_root, list_dirs, list_files in os.walk(directory):
        for list_dir in list_dirs:
            alias = os.path.basename(list_dir)
            levels = os.path.join(list_root,list_dir).split(SEPERATING_CHAR)
            idx = len(levels) - 3
            while alias in dictionary:
                alias = levels[idx] + "/" + alias
                idx -= 1

            dictionary[alias] = os.path.join(list_root,list_dir)
    return dictionary

def validate_brackets(text):
    PAIRINGS = {
        '{' : '}',
        '[' : ']',
    }


    stack = []
    for s in text:
        if s in PAIRINGS:
            stack.append(s)
            continue
        if s not in PAIRINGS.values():
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:
            return False
        if s != PAIRINGS[expected_opening_symbol]:
            return False

    return len(stack) == 0

def parse_encounter(path_to_file, ns):
    text = None
    with open(path_to_file) as f:
        text = f.read()
        if not ns:
            if not validate_brackets(text):
                raise EncounterParseError()

            text = text.replace('[', aformat.BOLD).replace(']', aformat.NOT_BOLD).replace('{', aformat.ITAL).replace('}', aformat.NOT_ITAL)
            text += aformat.NORM

    return text

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
            clr = aformat.RED
        elif _roll + 1 == len(table):
            clr = aformat.GRN
        else:
            clr = ''

        rollformat = aformat.BOLD + aformat.CYN + "1d" + str(len(table)) + "=" + clr + str(_roll + 1) + aformat.NORM

    if selection.endswith('.txt'):
        if not quiet_mode:
            print(os.path.basename(selection) + "(" + rollformat + ")\n")
        return parse_encounter(selection, no_ANSI_mode)
    else:
        if not quiet_mode:
            print(os.path.basename(selection[:-1]) + "(" + rollformat + ")>", end="")
        return roll(selection, quiet_mode, no_ANSI_mode)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default = None, help="the folder to roll from")
    parser.add_argument('-l', '--list', action='store_true', help="list all of the possible tables to roll from")
    parser.add_argument("-t", "--table", default = None, help= "specify a table by name.")
    parser.add_argument("--quiet", action='store_true', help="the program will only print out the output of the random encounter, and no superfluous details")
    parser.add_argument("--no_escape", action='store_true', help="the program will not attempt to format the text using ANSI codes, if for some reason your output is broken because of ANSI.")

    args = parser.parse_args()

    directory = None
    if args.dir == None:
        directory = os.getcwd()
    else:
        directory = os.path.join(args.dir, "")
        if not os.path.isdir(directory):
            print("Error: The directory at " + directory + " could not be found.")
            exit(-1)

    if args.list:
        dictionary = build_dict_of_tables(directory)

        for list_name in dictionary:
            print(list_name)
        exit(0)

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

if __name__ == "__main__":
    main()

