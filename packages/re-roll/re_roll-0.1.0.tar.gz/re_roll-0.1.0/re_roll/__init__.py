 # re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/12/22
# ----------------------------------
# file: EncounterFolderEmptyError.py
# Provides exceptions for the re-roll package.

class EncounterFolderEmptyError(Exception):
    def __init__(self, message="The encounter folder was empty."):
        super().__init__(message)


# re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/12/22
# ----------------------------------
# file: EncounterParseError.py
# Provides exceptions for the re-roll package.

class EncounterParseError(Exception):
    def __init__(self, message="There was an error parsing the file."):
        super().__init__(message)

# re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/11/22
# ----------------------------------
# file: aformat.py
# ANSI sequences are enumerated as variables in this class for easy readability.

class AFormat:
    NORM = '\033[0m'
    BOLD = '\033[1m'
    ITAL = '\033[3m'
    NOT_BOLD = '\033[22m'
    NOT_ITAL = '\033[23m'
    RED = '\033[31m'
    GRN = '\033[32m'
    CYN = '\033[38;5;45m'


# re-roll
# ----------------------------------
# author: Anon TG
# version 0.1.0
# last modification: 01/11/22
# ----------------------------------
# file: re_roll_utils.py
# Provides utility functions and classes for the re-roll package.
# - seperate_c_from_t() : Given a directory and a print mode, a pair containing (collections, tables) is returned
# - get_longest_string_len() : Given a list of strings, return the length of the longest string
# - build_dict_of_tables() Given a path to a directory, a print mode, and a boolean "hide empty" value, builds a dict of valid tables in a directory.
# - validate_brackets() : Given a string, ensure that all occurrances of [] and {} brackets are balanced (for use with ANSI output)
# - parse_encounter() : Given a path to a file and a no_escape setting, parses the contents of the file (adding ANSI output where requested) and returns the text

# NOTICE: When I get the time, much of this will be refactored. Functions that are only useful in certain modules will be removed from here and
# placed into the module they fit best.

from os import listdir, path, walk, name

#from .re_roll_except import EncounterParseError
#from .re_roll_aformat import AFormat

# seperate_c_from_t() : Given a directory and a print mode, a pair containing (collections, tables) is returned
def seperate_c_from_t(dictionary, print_mode="a"):
    if print_mode == "only_tables" or print_mode == "ot":
        return ({}, dictionary)
    if print_mode == "only_collections" or print_mode == "oc":
        return (dictionary, {})

    collections = {}
    tables = {}

    for key in dictionary.keys():
        is_table = True
        for entry in listdir(dictionary[key]):
            if path.isdir(path.join(dictionary[key], entry)):
                collections[key] = dictionary[key]
                is_table = False
                break
        if is_table:
            tables[key] = dictionary[key]

    return (collections, tables)

# get_longest_string_len() : Given a list of strings, return the length of the longest string
def get_longest_string_len(strings):
    longest_len = 0
    for string in strings:
        if len(string) > longest_len:
            longest_len = len(string)

    return longest_len

# build_dict_of_tables() Given a path to a directory, a print mode, and a boolean "hide empty" value, builds a dict of valid tables in a directory.
def build_dict_of_tables(directory, print_mode="a", hide_empty=False):
    SEPERATING_CHAR = '\\' if name == "nt" else '/'
    dictionary = {}
    if print_mode != "nothing":
        for list_root, list_dirs, list_files in walk(directory):
            for list_dir in list_dirs:
                if hide_empty:
                    if len(listdir(path.join(list_root,list_dir))) == 0:
                        break
                jump_out = False
                if print_mode == "only_tables" or print_mode == "ot":
                    for entry in listdir(path.join(list_root,list_dir)):
                        d = path.join(list_root, list_dir)
                        if path.isdir(path.join(d,entry)):
                            jump_out = True
                            break
                elif print_mode == "only_collections" or print_mode == "oc":
                    mini_jump = True
                    for entry in listdir(path.join(list_root, list_dir)):
                        d = path.join(list_root, list_dir)
                        if path.isdir(path.join(d,entry)):
                            mini_jump = False
                            break
                    jump_out = mini_jump

                if jump_out:
                    continue

                alias = path.basename(list_dir)
                levels = path.join(list_root,list_dir).split(SEPERATING_CHAR)
                idx = len(levels) - 3
                while alias in dictionary:
                    alias = levels[idx] + "/" + alias
                    idx -= 1

                dictionary[alias] = path.join(list_root,list_dir)
    return dictionary

# validate_brackets() : Given a string, ensure that all occurrances of [] and {} brackets are balanced (for use with ANSI output)
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

# parse_encounter() : Given a path to a file and a no_escape setting, parses the contents of the file (adding ANSI output where requested) and returns the text
def parse_encounter(path_to_file, ne=False):
    text = None
    with open(path_to_file) as f:
        text = f.read()
        if not ne:
            if not validate_brackets(text):
                raise re_roll_except.EncounterParseError()

            text = text.replace('[', AFormat.BOLD).replace(']', AFormat.NOT_BOLD).replace('{', AFormat.ITAL).replace('}', AFormat.NOT_ITAL)
            text += AFormat.NORM

    return text

from .main import *



__all__ = [
    "EncounterFolderEmptyError",
    "EncounterParseError",
    "AFormat",
    "seperate_c_from_t",
    "get_longest_string_len",
    "build_dict_of_tables",
    "validate_brackets",
    "parse_encounter",
    "create_group_string",
    "create_list_string",
    "re_roll_ls",
    "roll",
    "re_roll_roll",
    "valid_modules",
    "help_me",
    "main"
]
