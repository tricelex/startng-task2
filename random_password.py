import random
import string


def generate_password(fname, lname):
	letters = string.ascii_lowercase
	randomvars = ''.join(random.choice(letters) for i in range(5))
	password = fname[0:2] + lname[0:2] + randomvars
	return password
