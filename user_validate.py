from random_password import generate_password, validate_password

# first_name = input("Enter your first name: ")
# print(first_name)

# last_name = input("Enter your last name: ")
# print(last_name)

# email = input("Enter your email: ")
# print(email)

first_name = 'john'
last_name = 'snow'
password = generate_password(first_name, last_name)

satisfied = input(f'Are you satisfied with "{password}" as your password..Enter Y/N: ')

while satisfied != 'y' or 'n':
	if satisfied == 'y':
		print('yes')  # TODO: print out all user information here
		break
	elif satisfied == 'n':
		value = input('Enter new password equal or greater than 7 characters: ')
		user_input_password = validate_password(value)
		break
	else:
		satisfied = input('Please Enter either Y or N: ')

print(user_input_password)