class StringCalculator:
    def add(self, numbers):
        if numbers.startswith('//'):
            delimiter, numbers = numbers[2:].split('\n', 1)
        else:
            delimiter = ','

        number_list = numbers.split(delimiter)
        negatives = [int(num) for num in number_list if int(num) < 0]

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        return sum(int(num) for num in number_list if 0 <= int(num) <= 1000)
