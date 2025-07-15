class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        vowels=0
        consonants=0
        for c in word:
            if c.lower() in 'aeiou':
                vowels=vowels+1
            elif c not in '1234567890':
                consonants+=1
        if vowels==0 or consonants==0:
            return False
        
        return True
            

            
