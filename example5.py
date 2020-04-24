import sys

keys = sys.argv[1::2]
values = sys.argv[2::2]

# print(keys)

# print(values)

# # using zip iterable
# print(list(zip(keys,values)))

args = {k:v for k,v in zip(keys,values)}

print(args)

first_name = args.get('--first-name',None)
last_name = args.get('--last-name',None)
yob = int(args.get('--yob',None))

print(first_name,last_name,'\n',yob)

# small doubt cleared **************************
# a = {'first':'pranav','second':'B gates'}

# print(a)

# year_20 = a.get('first')
# print(f'2020 {year_20}')

# **************************************************

