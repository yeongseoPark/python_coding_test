# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 1:
            return strs[0]

        minlen = len(min(strs,key=len))

        if minlen == 0:
            return ""
        
        newstrs = [i[:minlen] for i in strs]
        
        pre_len = []
        for i in newstrs:
            tmp = newstrs[:]
            tmp.remove(i)
            for k in tmp:
                comm = 0
                for j in range(minlen):
                    if i[j] == k[j]:
                        comm += 1
                    elif i[j] != k[j]:
                        pre_len.append(comm)
                        break

                    if j == minlen-1:
                        pre_len.append(comm)
        
        print(pre_len)
        if min(pre_len) == 0:
            return ""
        else:
            return newstrs[0][:min(pre_len)]

        
print(Solution().longestCommonPrefix(["a","ab","abac","adfsdfsd"]))