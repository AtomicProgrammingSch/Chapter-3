
def find_sum(args):  # Function which finds the sum, function used to make the code expandable so you can find the sum of many lists
    sum = 0
    for number in args:
        sum += number
    return sum

finished = False

numbers = []  # List of the numbers entered
while finished is False:
    print("Please enter a number:")
    str_number = input()
    try:  # If a float (decimal number) is entered, the conversion will throw a ValueError
        number = int(str_number)
    except ValueError:  # catches the ValueError and converts the string into a float instead of an int
        number = float(str_number)
    numbers.append(number)  # Appends the number which was just inputted into the list
    while True:  # Indefinite loop, breakpoints have been added
        print("Would you like to enter another number? (y/n)")
        resp = input()
        if resp == "y":
            break
        elif resp == "n":
            sum = find_sum(numbers)
            print("The sum of the " + str(len(numbers)) + " numbers you entered is " + str(sum))
            finished = True
            break
