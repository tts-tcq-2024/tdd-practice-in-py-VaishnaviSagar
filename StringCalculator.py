class StringCalculator:
    def add(self, numbers):
        delimiter, numbers = self._extract_delimiter(numbers)
        number_list = self._split_numbers(numbers, delimiter)
        self._validate_numbers(number_list)
        return self._sum_valid_numbers(number_list)

    def _extract_delimiter(self, numbers):
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter = parts[0][2:]  # Skip the "//" part
            return delimiter, parts[1] if len(parts) > 1 else ''
        return ',', numbers

    def _split_numbers(self, numbers, delimiter):
        return numbers.split(delimiter)

    def _validate_numbers(self, number_list):
        negatives = [int(num) for num in number_list if num and int(num) < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    def _sum_valid_numbers(self, number_list):
        return sum(int(num) for num in number_list if num and int(num) <= 1000)
