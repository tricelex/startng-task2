import random
import string


def generate_password(fname, lname):
	letters = string.ascii_lowercase
	randomvars = ''.join(random.choice(letters) for i in range(5))
	rand_password = fname[0:2] + lname[0:2] + randomvars
	return rand_password


def validate_password(my_password):
	new_user_input_password = ''
	length = 7
	while len(my_password) < length:
		new_user_input_password = input(
			'Please Enter new password equal or greater than 7 characters: ')
	return new_user_input_password


def show_message(new_employee):
	print('\nEmployee Information: ')
	print("FirstName: " + new_employee['firstName'])
	print("LastName: " + new_employee['lastName'])
	print("Email: " + new_employee['email'])
	print("Password: " + new_employee['password'])


is_running = True
all_employees = []

while is_running:
	first_name = input("Enter your first name: ")
	last_name = input("Enter your last name: ")
	email = input("Enter your email: ")
	password = generate_password(first_name, last_name)

	satisfied = input(f'Are you satisfied with "{password}" as your password..Enter Y/N: ')

	while satisfied != 'y' or 'n':
		if satisfied == 'y':
			employee = {'firstName': first_name, 'lastName': last_name, 'email': email,
						'password': password}
			all_employees.append(employee)
			show_message(employee)
			quit_program = input('\nEnter q to quit or any value to continue: ')
			if quit_program == 'q':
				is_running = False
			break
		elif satisfied == 'n':
			value = input('\nEnter new password equal or greater than 7 characters: ')
			user_input_password = validate_password(value)
			employee = {'firstName': first_name, 'lastName': last_name, 'email': email,
						'password': user_input_password}
			all_employees.append(employee)
			show_message(employee)
			quit_program = input('Enter q to quit or any value to continue: ')
			if quit_program == 'q':
				is_running = False
			break
		else:
			satisfied = input('Please Enter either Y or N: ')

for user in all_employees:
	print('')
	print(user)
