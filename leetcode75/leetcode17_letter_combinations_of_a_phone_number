class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        numToLetters = {"2": ["a", "b", "c"], "3": ["d","e","f"], "4": ["g","h","i"], "5": ["j", "k", "l"], "6":["m", "n", "o"],
        "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        curr_subset = []

        def backtrack(i: int) -> None:
            if i == len(digits):
                new_str = ''.join(curr_subset.copy())
                res.append(new_str)
                return
            for letter in numToLetters[digits[i]]:
                curr_subset.append(letter)
                backtrack(i + 1)
                curr_subset.pop()

        backtrack(0)
        return res
    