print('Mini Calculator')
#user input
num1 = float(input('Enter first number here:'))
num2 = float(input('Enter second number here:'))
#list of operation to do
print('press 1 for addition \npress 2 for subtration \npress 3 for division \npress 4 for multiplication')

choice = int(input('Enter your choice from 1-4:'))
#conditional statement
if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 / num2)
elif choice == 4:
    print(num1 * num2)
else:
    print('Invalid Input')