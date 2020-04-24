import argparse
import datetime

parser = argparse.ArgumentParser(description='Returns a string contains the name and ageof covid19.')

parser.add_argument('-f','--first',help='first name',type=str,required=False,dest='first_name')
parser.add_argument('-l','--last',help='last name',type=str,required=True,dest='last_name')

parser.add_argument('--yob',help='Year of Birth',type=int,required=True,dest='Birth_year')

args = parser.parse_args()

if args.first_name:
    names = [args.first_name]
else:
    names = []

names.append(args.last_name)
full_name = ' '.join(names)

# Current year taking format

current_year = datetime.datetime.utcnow().year

age = current_year - args.Birth_year

# print(args)

print(f'{full_name} is {age} years old.')