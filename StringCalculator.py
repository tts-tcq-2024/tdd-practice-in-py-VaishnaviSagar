import re

def add(numbers):
    if not numbers:
        return 0

    # Check for custom delimiter
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    
    # Split numbers by commas and newlines
    number_list = re.split(r'[,\n]', numbers)
    
    total = 0
    for number in number_list:
        if number:  # Ensure the number is not empty
            num = int(number)
            if num <= 1000:  # Ignore numbers greater than 1000
                total += num

    return total

