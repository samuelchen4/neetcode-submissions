class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0 
        frequency_s = {}
        frequency_t = {}
        have = 0
        need = 0

        result = ""

        # fill the frequency of t
        for c in range(len(t)):
            if frequency_t.get(t[c]):
                frequency_t[t[c]] += 1
            else:
                frequency_t[t[c]] = 1
                need += 1

        while r < len(s):
            head = s[r]
            if frequency_s.get(head):
                frequency_s[head] += 1
            else:
                frequency_s[head] = 1

            if head in frequency_t and frequency_s[head] == frequency_t[head]:
                have += 1
            while have == need:
                tail = s[l]
                if not result or r - l + 1 < len(result):
                    result = s[l:r + 1]
                frequency_s[tail] -= 1
                
                if tail in frequency_t and frequency_s[tail] < frequency_t[tail]:
                    have -= 1
                l += 1
            
            r += 1
        return result

