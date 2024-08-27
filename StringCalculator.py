class StringCalculator:
    def add(self, numbers):
        delimiter, numbers = self._parse_delimiter(numbers)
        number_list = self._split_numbers(numbers, delimiter)
        self._check_negatives(number_list)
        return self._sum_numbers(number_list)

    def _parse_delimiter(self, numbers):
        if numbers.startswith('//'):
            delimiter, numbers = numbers[2:].split('\n', 1)
            return delimiter, numbers
        return ',', numbers

    def _split_numbers(self, numbers, delimiter):
        return numbers.split(delimiter)

    def _check_negatives(self, number_list):
        negatives = [num for num in number_list if int(num) < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(negatives)}")

    def _sum_numbers(self, number_list):
        return sum(int(num) for num in number_list if 0 <= int(num) <= 1000)
