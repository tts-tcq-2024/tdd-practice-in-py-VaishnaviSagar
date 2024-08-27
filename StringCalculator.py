class StringCalculator:
    def add(self, numbers):
        delimiter, numbers = self._extract_delimiter(numbers)
        number_list = self._split_numbers(numbers, delimiter)
        return self._sum_valid_numbers(number_list)

    def _extract_delimiter(self, numbers):
        return (numbers.split('\n', 1)[0][2:], numbers.split('\n', 1)[1]) if numbers.startswith('//') else (',', numbers)

    def _split_numbers(self, numbers, delimiter):
        return numbers.split(delimiter)

    def _sum_valid_numbers(self, number_list):
        total = 0
        for num in number_list:
            total += self._process_number(num)
        return total

    def _process_number(self, num):
        if num:
            value = int(num)
            if value < 0:
                raise ValueError(f"negatives not allowed: {value}")
            return value if value <= 1000 else 0
        return 0
