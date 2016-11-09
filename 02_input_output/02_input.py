# Python Toolkit
# input_output/input

# We can get user input using the input function
person = input('Enter your name: ')
print('Hello', person)

# Bear in mind the type of the value is *always* a string
# To work with numbers you need to cast the value to a numeric type
age = input('Enter your age: ')
age = int(age)
print('In 10 years you will be', age + 10)
