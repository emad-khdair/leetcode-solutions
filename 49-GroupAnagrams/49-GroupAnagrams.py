# Last updated: 8/30/2025, 3:37:02 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord('a')] += 1

            hash_map[tuple(count)].append(word)

        return list(hash_map.values())