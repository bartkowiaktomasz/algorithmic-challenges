from typing import List
from collections import defaultdict
from heapq import heappush, heappop

import logging

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(endWord) != len(beginWord):
            # Optimisation - if word has wrong length, skip it
            return 0
        if endWord not in wordList:
            # Optimisation
            return 0
        if beginWord == endWord:
            return 1
        adjacency_list = self.buildAdjacencyList([beginWord] + wordList)
        forward_set = set([beginWord])
        backward_set = set([endWord])
        visited = set()
        step = 1
        direction = 1
        while forward_set or backward_set:
            current_set = forward_set if direction == 1 else backward_set
            opposite_set = backward_set if direction == 1 else forward_set
            temp_set = set()
            for node in current_set:
                visited.add(node)
                for neighbour in adjacency_list[node]:
                    if neighbour in visited:
                        continue
                    else:
                        if neighbour in opposite_set:
                            return step + 1
                        else:
                            temp_set.add(neighbour)
            step += 1
            direction *= -1
            if current_set is forward_set:
                forward_set = temp_set
            else:
                backward_set = temp_set
        return 0
    
    def buildAdjacencyList(self, wordList: List[str]):
        ALPHABET_FIRST = ord('a')
        ALPHABET_SIZE = 25
        # First word is the beginWord
        word_len = len(wordList[0])
        adjacency_list = defaultdict(set)
        word_set = set(wordList)
        for i in range(len(wordList)):
            # Optimisation - if word has wrong length, skip it
            if len(wordList[i]) != word_len:
                continue
            for j in range(len(wordList[i])):
                edited_word_list = list(wordList[i])
                for k in range(ALPHABET_FIRST, ALPHABET_FIRST + ALPHABET_SIZE + 1):
                    edited_word_list[j] = chr(k)
                    edited_word = "".join(edited_word_list)
                    if edited_word in word_set and edited_word != wordList[i]:
                        adjacency_list[wordList[i]].add(edited_word)
                        adjacency_list[edited_word].add(wordList[i])
        return adjacency_list


sol = Solution()
beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog"]

print(
    sol.ladderLength(beginWord, endWord, wordList)
)