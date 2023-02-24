class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        words_list=list()
        for word in s:
            words_list.append(word[::-1])
        return " ".join(words_list)