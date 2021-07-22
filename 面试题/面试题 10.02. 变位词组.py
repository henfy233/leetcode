# https: // leetcode-cn.com/problems/group-anagrams-lcci/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        flag = []
        book = []
        li = []
        for index, word in enumerate(strs):
            print(index, word)
            tmp = []
            if word == "":
                li = [26]
            for id, ch in enumerate(word):
                tmp.append(ord(ch)-97)
                li = sorted(tmp)
                # print('li', li)
            if li not in book:
                book.append(li)
                flag.append([word])
            else:
                id = book.index(li)
                # print(id)
                flag[id].append(word)
        # print(book)
        return flag
