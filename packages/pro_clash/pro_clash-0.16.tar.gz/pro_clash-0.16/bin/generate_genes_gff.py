#!/usr/bin/env python

"""
Generate a genes gff file using EcoCyc data given as flat-files
"""

import sys
import argparse

from pro_clash import ecocyc_parser

def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object, replace the description
    parser = argparse.ArgumentParser(
        description='Generate EcoCyc genes gff file')
    parser.add_argument(
        'ec_dir',
        help='EcoCyc flat-files directory.')

    settings = parser.parse_args(argv)

    return settings

def main(argv=None):
    settings = process_command_line(argv)
    ecocyc_parser.generate_gff_file(sys.stdout, settings.ec_dir)
    # application code here, like:
    # run(settings, args)
    return 0        # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)
