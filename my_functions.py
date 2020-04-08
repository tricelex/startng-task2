import random
import string


def generate_password(fname, lname):
	letters = string.ascii_lowercase
	randomvars = ''.join(random.choice(letters) for i in range(5))
	password = fname[0:2] + lname[0:2] + randomvars
	return password


def validate_password(user_input_password):
	length = 7
	while len(user_input_password) < length:
		user_input_password = input(
			'Please Enter new password equal or greater than 7 characters: ')
	return user_input_password


def show_message(employee):
	print('')
	print("FirstName: " + employee['firstName'])
	print("LastName: " + employee['lastName'])
	print("Email: " + employee['email'])
	print("Password: " + employee['password'])
