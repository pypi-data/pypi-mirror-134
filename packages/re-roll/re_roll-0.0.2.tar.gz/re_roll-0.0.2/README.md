# re-roll

Treat a directory as a collection of "random-encounter" tables for use as a DM, GM, or Whatever-M for any tabletop game.
Supports directories of arbitrary depth, as well as a very minimalist formatting code.

[![PyPi](https://img.shields.io/badge/PyPI-v0.0.1-blue.svg)](https://pypi.org/project/re-roll/)

## Install

```
python -m pip install re-roll
```

## Usage

Navigate to a directory containing an arbitrary number of subfolders, each containing any number of .txt files with
the description of a random encounter within.

Then  use the
```
re-roll
```
command to choose a random text file from within the directory.

For example, given the following directory structure:

* 5e
	* wilderness
		* wolves.txt
		* bandits.txt
		* druids.txt
	* urban
		* robbers.txt
		* sewer-ghouls.txt
		* thieves.txt

running **re-roll** from within **5e** will choose a text file from either wilderness or urban, while running
**re-roll** within either subdirectories will only choose files within their selected folders.

Example output from running the program from within the above subdirectory:
```
wilderness(1d2=1)>bandits.txt (1d3=2)

The players encounter a group of 1d4+2 bandits blocking the path.
They demand the players surrender all of their valuables...
```

Running the program with no arguments selects the current working directory (that is, the directory you are running the program) from as the
top-level directory to traverse.

You can provide another directory with the **-d** or **--dir** command line argument. For example:
```
re-roll --dir ./wilderness
```

would only roll from the wilderness directory, provided of course that you are in the 5e directory (since the '.' denotes 'current working directory')

## Formatting Output

This program features a very simple parser that can format the output of your random encounters. This can
be useful to highlight important text like dice rolls or monster names. This feature is only supported by
consoles that suport ANSI formatting escape sequences.

Text encased in a set of {curly brackets} becomes *italicized*, while text encased in [square brackets] is **emboldened**.

You can disable this feature by running the program with the **--no_escape** option.

## List Mode

Run the program with the **-l** or **--list** option to list all possible tables to roll from (i.e. all subfolders in the given, or
current working directory).

For example, running:
```
re-roll -l
```

in the above example would output:
```
wilderness : /home/blahblahblah/encounters/5e/wilderness
urban : /home/blahblahblah/encounters/5e/urban
```

Providing a directory with the **-d** or **--dir** option also modified which dir is listed.

## Specify a Table by Name

Using the names outputted by the **-l** or **--list** options, you can use the **-t** or **--table** option to to roll from a specific
table.

This is quicker than using the **--dir** option.

For example, compare:
```
re-roll -t ghosts
```

to:
```
re-roll --dir ./monsters/by-source/tob-ii/by-cr/cr4/undead/ghosts
```

## Quiet Mode
Normally, the output includes all the subfolders that were selected, as well as the number that was rolled to select them.

Sometiems you just don't want to include that superfluous detail. Use the **--quiet** option to only output the selected encounter.

