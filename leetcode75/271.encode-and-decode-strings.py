class Solution:

    def encode(self, strs: List[str]) -> str:
        # we will build our str, so that we will first have the lens of each str followed by our seperator ':'
        res = ''
        s_lens = [str(len(s)) for s in strs]
        res = ':'.join(s_lens) + ';' + ''.join(strs)
        return res
        
    def decode(self, s: str) -> List[str]:
        # iterate s twice, first to retrieve s_lens, and second to rebuild strs
        s_lens = []
        i = 0

        while i < len(s) and s[i] != ';':
            curr_len = ''
            if i > 0:
                i += 1
            while i < len(s) and s[i] != ':' and s[i] != ';':
                curr_len += s[i]
                i += 1
            s_lens.append(curr_len)
        
        # now i should be at ';'
        res = []
        i += 1
        for s_len in s_lens:
            res.append(s[i:i+int(s_len)])
            i += int(s_len)
        
        return res