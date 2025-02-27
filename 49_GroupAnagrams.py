from collections import Counter, defaultdict
from typing import List

from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())


if __name__=="__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution=Solution()
    result=solution.groupAnagrams(strs)
    print(result)