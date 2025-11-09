# Last updated: 11/9/2025, 7:49:07 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26 

            for l in s:
                count[ord(l) - ord('a')] += 1

            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())
            