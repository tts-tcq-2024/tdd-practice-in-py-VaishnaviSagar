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
        self.negatives = []
        for num in number_list:
            if num:
                value = int(num)
                if value < 0:
                    self.negatives.append(value)
        if self.negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, self.negatives))}")

    def _sum_valid_numbers(self, number_list):
        total = 0
        for num in number_list:
            if num:
                value = int(num)
                if value <= 1000:
                    total += value
        return total
