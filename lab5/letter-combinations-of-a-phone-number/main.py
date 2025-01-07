class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(k^n),
        # k - maximum number of characters per digit
        # n - the number of digits in the input string
        # So, the time complexity is somewhere between O(3^n) and O(4^n) in this case
        if digits is None or len(digits) == 0:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        # Queue for all possible combinations
        combinations_queue = deque()

        # Add all characters for the first digit
        for char in digit_to_char[digits[0]]:
            combinations_queue.append(char)

        # For each digit, except the first
        for digit in digits[1:]:
            # For each combination
            for _ in range(len(combinations_queue)):
                # Delete the current combination and append it with all possible characters
                current_combination = combinations_queue.popleft()
                for char in digit_to_char[digit]:
                    combinations_queue.append(current_combination + char)

        # Return queue as list
        return list(combinations_queue)