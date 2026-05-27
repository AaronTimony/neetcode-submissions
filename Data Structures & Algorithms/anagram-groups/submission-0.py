class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for letter in string:
                new = ord(letter) - ord('a')
                count[new] += 1

            matches[tuple(count)].append(string)

        return list(matches.values())
            
