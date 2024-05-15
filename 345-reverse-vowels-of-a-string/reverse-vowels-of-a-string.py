class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['A','E','I','O','U','a','e','i','o','u']
        vowinstring = [x for x in s if x in vowels]
        
        
        new=''
        for x in s:
            if x in vowels:
                top= vowinstring.pop()
               
                new+=top
            else:
                new+=x
            
        return new
                
                

        

        
        