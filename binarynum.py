binary_numbers = input("Enter comma-separated 4-digit binary numbers: ")
print(','.join([num for num in binary_numbers.split(',') if int(num, 2) % 5 == 0]))