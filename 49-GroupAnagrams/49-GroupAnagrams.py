# Last updated: 8/30/2025, 3:52:24 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            mp[tuple(count)].append(word)

        return list(mp.values())