#给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。
def strStr(haystack,needle):
    len1=len(needle)
    if len1==0:
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len1]==needle:
            return i
    return -1