class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if target is None or source is None:# or len(source) < len(target):
            return -1 
	# here, empty string and null are two different types of input and needs to be considered separately.
        
    
        for i in range(len(source) - len(target) + 1):
            if source[i:i+len(target)] == target:
                return i
        
        return -1
