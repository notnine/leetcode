#
# @lc app=leetcode id=2002 lang=python3
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#

# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(mask):
            # build our masked substrings
            word = []
            b = 1
            for pos in range(len(s)):
                if b & mask:
                    word.append(s[pos])
                b = b << 1
            word = ''.join(word)

            # palindrome check
            l, r = 0, len(word) - 1
            while l <= r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        # find all masks that produce palindromes
        pali_masks = []
        n = len(s)
        for i in range(2 ** n):
            if is_palindrome(i):
                pali_masks.append(i)
            
        # from those masks, find all disjoint ones
        best = 0
        for i in range(len(pali_masks)):
            for j in range(i + 1, len(pali_masks)):
                mask1, mask2 = pali_masks[i], pali_masks[j]
                if mask1 & mask2 == 0:
                    best = max(best, mask1.bit_count() * mask2.bit_count())

        return best


    def maxProduct_archive(self, s: str) -> int:
        # find the 2 longest disjoint subsequences

        # intuition: brute force would be to find all subsequences, for each subsequence, find its longest disjoint subsequent, keep track of the pair of longest disjoint subsequences seen so far

        # hint: generate all possible pairs of disjoint subsequences

        # bit manip
        # generate all possible masks, generate all possible combinations b/w all masks -> all possible pairs of disjoint subsequences
        # for each pair do palindrome check

        def is_palindrome(word):
            l, r = 0, len(word) - 1
            while l <= r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True


        # generate all possible masks
        n = len(s)
        best = 0
        for i in range(2**n):
            mask1 = i
            for j in range(2**n):
                mask2 = j
                # disjoint check
                if mask1 & mask2 == 0:
                    # build our masked substrings
                    str1 = []
                    b = 1
                    for pos1 in range(len(s)):
                        if b & mask1:
                            str1.append(s[pos1])
                        b = b << 1
                    str2 = []
                    b = 1
                    for pos2 in range(len(s)):
                        if b & mask2:
                            str2.append(s[pos2])
                        b = b << 1
                    str1, str2 = ''.join(str1), ''.join(str2)

                    if is_palindrome(str1) and is_palindrome(str2):
                        best = max(best, len(str1) * len(str2))
        
        return best

# @lc code=end

