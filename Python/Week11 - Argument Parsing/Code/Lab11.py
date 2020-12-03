#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(
    description="This is Mike Polselli's Script"
)
parser.add_argument(
    '-m',dest='BASIC',help='Enter some text'
)
parser.add_argument(
    '-i','--integer',dest='[an integer]',type=int,help='Enter a simple Integer'
)
parser.add_argument(
    '-d','--float',dest='[a float]',type=float,help='Enter a simple Float'
)
parser.add_argument(
    '-s', '--string', dest='[a string]', type=str, help='Enter a simple String'
)
parser.add_argument(
    '-l', dest='[strings]',default=[],nargs='+',help='Enter a list of strings (space delimited)'
)
parser.add_argument(
    '-t','--set-true',dest='bool_t',default=False,action='store_true',help='Toggle from default False to True'
)
parser.add_argument(
    '-f','--set-false',dest='bool_f',default=True,action='store_false',help='Toggle from default True to False'
)
parser.add_argument(
    '-v','--version',action='version',version='%(prog)s 1.0'
)
args = parser.parse_args()
