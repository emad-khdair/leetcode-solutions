# Last updated: 11/9/2025, 7:18:10 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            a_key = ''.join(sorted(word))

            anagram_map[a_key].append(word)

        return list(anagram_map.values())