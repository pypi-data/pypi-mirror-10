#!/usr/bin/env python

'''metameta 0.0.0.20 - meta-transcriptome/genome mapping analysis toolkit

Usage:

    metameta <tool> [arguments for tool]

Synopsis:

    metameta is a toolkit with a number of programs useful for analyzing
    meta-transcriptome/genome data that has been mapped to a reference.
    It is contains a number of generally useful bioinformatic scripts.
    Type "metameta --docs" for full documentation.

Options:

    Toolkit (options from metameta, no tool specified/needed):
    
        --help             This help
        --version          Print toolkit version and exits
        --docs             Show full manual

    General Tool Options (options shared by most or all tools):
    
        no arguments       Gives tool help and exits
        --help             Gives tool help and exits
        --version          Prints tool version and exits
        --verify           Verify relevant files before executing
        --log_file         Write output to the log file

    Verbosity Settings (all tools):

        none: Fatal errors only
        -v: Fatal errors and important information only
        -vv: Detailed information on everything the program is doing,
             best reserved for debugging purposes
        Note: any numbers of "v"s may be specified but anything greater than
        -vv will be identical to -vv.  

Tools:

    annotate_clusters:

            Compares a statistics file from filter_fastr to a GFF file
            to annotate clusters.

    create_table:

            Takes multiple annotated stats files and compiles them into
            a table.

    filter_fastr:

            Isolates clusters from a FASTR file, seperates them by size,
            and outputs a statistics file.

    generate_fastr:

            Generates a FASTR file containing per base read depth data
            of a given FASTA or FASTQ file.

    metameta_utilities:

            A file containing a variety of modules useful to many scripts in
            metameta.
'''

__version__ = '0.0.0.20'

import argparse
import subprocess
import sys

def tool_check(desired_tool):
    '''Checks if given tool is valid and prints a list of toosl if not'''
    
    tools = [
        'annotate_clusters',
        'create_table',
        'filter_fastr',
        'generate_fastr',
        'metameta_utilities'
        ]
    for tool in tools:
        if desired_tool == tool:
            return desired_tool
    print('No such tool: ' + desired_tool)
    print('Available tools:')
    for tool in tools:
        print(tool)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description = __doc__,
                                        formatter_class = argparse.\
                                        RawDescriptionHelpFormatter)
    parser.add_argument('tool',
                        type = tool_check,
                        default = None,
                        nargs = '?',
                        help = 'tool to run')
    parser.add_argument('arguments',
                        nargs = argparse.REMAINDER,
                        help = 'arguments to pass to tool')
    parser.add_argument('--docs',
                        help = 'prints documentation and exits',
                        action = 'store_true')
    parser.add_argument('--version',
                        help = 'prints toolkit version and exits',
                        action = 'store_true')
    args = parser.parse_args()

    if args.version:
        print(__version__)
    elif args.docs:
        subprocess.call(['less', '../Documentation.txt'])
    elif args.tool == None:
        print(__doc__)
    else:
        script = 'bin/' + args.tool + '.py ' + arguments
        subprocess.call(['python', script])
    
if __name__ == '__main__':
    main()
    sys.exit(0)
