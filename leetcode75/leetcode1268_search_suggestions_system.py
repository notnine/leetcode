class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        n = len(searchWord)
        l, r = 0, len(products) - 1

        for i in range(n): # searchWord[i]
            c = searchWord[i]

            # increment l while products[l] is invalid
            while l <= r and (i >= len(products[l]) or products[l][i] != c):
                l += 1
            while l <= r and (i >= len(products[r]) or products[r][i] != c):
                r -= 1
            
            # append to res a list of at most 3 valid words
            curr = []
            for i in range(min(3, r - l + 1)):
                curr.append(products[l+i])
            res.append(curr.copy())

        return res