class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        # Check for custom delimiter
        if numbers.startswith('//'):
            delimiter, numbers = self._extract_delimiter(numbers)
        else:
            delimiter = ','
        
        # Replace new lines with the delimiter
        numbers = numbers.replace('\n', delimiter)
        
        # Split the numbers by the delimiter
        number_list = numbers.split(delimiter)
        
        # Validate and sum the numbers
        return self._sum_numbers(number_list, delimiter)

    def _extract_delimiter(self, numbers):
        # Extract the custom delimiter
        parts = numbers.split('\n', 1)
        delimiter = parts[0][2:]  # Skip the "//" part
        return delimiter, parts[1] if len(parts) > 1 else ''

    def _sum_numbers(self, number_list, delimiter):
        total = 0
        negatives = []

        for num in number_list:
            if num:  # Ignore empty strings
                value = int(num)
                if value < 0:
                    negatives.append(value)
                elif value <= 1000:
                    total += value

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        return total
