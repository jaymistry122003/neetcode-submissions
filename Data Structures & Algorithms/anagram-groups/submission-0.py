class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict= {}
        for text in strs:
            sorted_text = "".join(sorted(text))
            if sorted_text not in dict:
                dict[sorted_text]= [text]
            else:
                dict[sorted_text].append(text)
        return list(dict.values())
        
        

        