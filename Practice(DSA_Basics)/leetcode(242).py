# LeetCode — Problem 242: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        sd=[]
        td=[]
        # Step 1: Create a list of unique characters
        for n in s:
            if n not in sd:
                sd.append(n)
        for m in t:
            if m not in td:
                td.append(m)                

        # Step 2: Iterate through unique characters
        for i in sd:
            if i not in td:
                return False

        # Step 3: Compare their frequencies in s and t
        for i in sd:
            for j in td:
                if sd[i]==td[j]:
                    if sd.count(sd[i])==td.count(td[j]):
                        return True


        # Step 4: Return True if all frequencies match