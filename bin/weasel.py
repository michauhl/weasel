#!/usr/bin/env python3

import argparse
import numpy as np
import os


"""

"""


################################################################################

def setup_argument_parser():
    """Setup argparse parser."""
    help_description = """
    Help description
    """
    # Define argument parser.
    p = argparse.ArgumentParser(add_help=False,
                                prog="weasel.py",
                                description=help_description,
                                formatter_class=argparse.MetavarTypeHelpFormatter)

    # Required arguments.
    p.add_argument("-h", "--help",
                   action="help",
                   help="Print help message")
    p.add_argument("--in",
                   dest="in_file",
                   type=str,
                   metavar='str',
                   required=True,
                   help="Input file")
    return p

################################################################################


if __name__ == '__main__':

    parser = setup_argument_parser()
    args = parser.parse_args()

    assert os.path.exists(args.in_file), "--in file \"%s\" not found" % (args.in_file)
