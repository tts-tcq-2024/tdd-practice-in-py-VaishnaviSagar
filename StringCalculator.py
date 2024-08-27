class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        delimiter, numbers = self._extract_delimiter(numbers)
        return self._sum_valid_numbers(numbers.split(delimiter))

    def _extract_delimiter(self, numbers):
        if numbers.startswith('//'):
            delimiter = numbers.split('\n', 1)[0][2:]  # Extract custom delimiter
            return delimiter, numbers.split('\n', 1)[1] if len(numbers.split('\n', 1)) > 1 else ''
        return ',', numbers

    def _sum_valid_numbers(self, number_list):
        total = 0
        negatives = []
        for num in number_list:
            total, negatives = self._process_number(num, total, negatives)
        self._check_negatives(negatives)
        return total

    def _process_number(self, num, total, negatives):
        if num:
            value = int(num)
            if value < 0:
                negatives.append(value)
            elif value <= 1000:
                total += value
        return total, negatives

    def _check_negatives(self, negatives):
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
