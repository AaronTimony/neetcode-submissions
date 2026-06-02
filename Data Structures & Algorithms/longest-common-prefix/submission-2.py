class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        sample_word = strs[0]
        for i, char in enumerate(sample_word):
            for word in strs:
                if i >= len(word):
                    return longest 

                if word[i] != char:
                    return longest

            longest += char

        return longest

            


            