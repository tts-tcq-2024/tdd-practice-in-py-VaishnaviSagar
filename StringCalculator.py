class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        delimiter, numbers = self._get_delimiter_and_numbers(numbers)
        numbers = self._replace_newlines(numbers, delimiter)
        number_list = self._split_numbers(numbers, delimiter)
        self._validate_numbers(number_list)
        
        return self._sum_valid_numbers(number_list)

    def _get_delimiter_and_numbers(self, numbers):
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter = parts[0][2:]  # Skip the "//" part
            return delimiter, parts[1] if len(parts) > 1 else ''
        return ',', numbers

    def _replace_newlines(self, numbers, delimiter):
        return numbers.replace('\n', delimiter)

    def _split_numbers(self, numbers, delimiter):
        return numbers.split(delimiter)

    def _validate_numbers(self, number_list):
        self.negatives = []
        for num in number_list:
            if num and int(num) < 0:
                self.negatives.append(int(num))
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
