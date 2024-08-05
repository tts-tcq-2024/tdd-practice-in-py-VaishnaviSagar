import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ","
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    
    total = sum(int(num) for num in re.split(f'[{delimiter}\n]', numbers) if int(num) <= 1000)
    
    return total
