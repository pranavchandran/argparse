import argparse

parser = argparse.ArgumentParser(description='Calculates the div a//b and a%b of two integers')

parser.add_argument('a',help='first integer',type=int)
parser.add_argument('b',help='second integer',type=int)

args = parser.parse_args()
a = args.a 
b = args.b
print(f'{a}//{b}={a//b},{a}%{b}={a%b}')
# args = parser.parse_args(['100','200'])

# print(args.a)
# print(args.b)

# to starting from the command line
# import sys
# args = parser.parse_args(sys.argv[1:])

# print(args.a,args.b)

# example6.py -h helps to see all

