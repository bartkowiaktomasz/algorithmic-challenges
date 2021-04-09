"""
Return the index of the first occurrence of needle in haystack, or `-1` if needle is
not part of haystack.
"""


class KMPSearch:
    @staticmethod
    def build_lps(p: str):
        lps_arr = [0 for _ in range(len(p))]
        i = 1
        len_lps = 0
        while i < len(p):
            if p[i] == p[len_lps]:
                len_lps += 1
                lps_arr[i] = len_lps
                i += 1
            else:
                if len_lps != 0:
                    len_lps = lps_arr[len_lps - 1]
                else:
                    lps_arr[i] = 0
                    i += 1
        return lps_arr

    @staticmethod
    def find(s: str, p: str):
        lps = KMPSearch.build_lps(p)
        i = 0
        j = 0
        while i < len(s):
            if j == len(p):
                return i - len(p)
            if s[i] == p[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        if j == len(p):
            return i - len(p)
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        else:
            return KMPSearch.find(haystack, needle)
