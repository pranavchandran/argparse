import argparse

parser = argparse.ArgumentParser(description='prints the squares of a list of numbersand the cubes of another list of numbers.')

parser.add_argument('--sq',help='list of numbers to square',nargs='*',type=float)
parser.add_argument('--cu',help='list of numbers to cube',nargs='+',type=float,required=True,dest='cubes')

args = parser.parse_args()

if args.sq:
    squares = [n ** 2 for n in args.sq]
    print(f'squares : {squares}')

cubes = [n ** 3 for n in args.cubes]
print(f'cubes : {cubes}')


