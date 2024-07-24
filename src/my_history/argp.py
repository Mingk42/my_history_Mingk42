import argparse

def argp():
    parser=argparse.ArgumentParser(description="history search program")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d",help="mh -d <>")
    group.add_argument("-t",help="mh -t <>")
    group.add_argument("-s",help="mh -s <>")

argp()
