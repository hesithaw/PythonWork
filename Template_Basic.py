#!/usr/bin/python

import sys
import os
import argparse

# Define Common System Variables
NEEDED_URL = "https://www.facebook.com/"

def things_you_want_to_do(args):
	 print("URL : {0}".format(args.url)); 

def init_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1",        dest="argument_1", 			help=" First Argument  ")
    parser.add_argument("--arg2",        dest="argument_2",             help=" Second Argument ")
    parser.add_argument("--arg3",        dest="argument_3",            	help=" Third Argument ")      
    return parser
    
def parse_arguments(parser):
    args = parser.parse_args()
    args.url = NEEDED_URL
	
    return args       
    
def main():
    parser = init_arguments()
    args = parse_arguments(parser)    
    things_you_want_to_do(args)
if __name__ == "__main__":
    main()    