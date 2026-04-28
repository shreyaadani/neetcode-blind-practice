class Solution:
    def compress(self, chars: List[str]) -> int:
      i = 0
      w = 0
      while i < len(chars):
        char = chars[i]
        count = 0
        
        # count the group
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1
        
        # write character
        chars[w]= char
        w+=1

        if count > 1:
            for c in str(count):
                chars[w] = c
                w+=1
                
        
        
    
      return w
