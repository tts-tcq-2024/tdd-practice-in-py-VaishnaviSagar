class StringCalculator:
    def add(self, numbers):
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
            if num:
                value = int(num)
                if value < 0:
                    negatives.append(value)
                elif value <= 1000:
                    total += value
        
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        return total
