class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        final=[]
        products.sort()
        for i in range(len(searchWord)):
            search_str=searchWord[:i+1]
            temp=[]
            n=len(search_str)
            for i in range(len(products)):
                if search_str == products[i][:n]:
                    temp.append(products[i])
                if len(temp)==3:
                    break
            final.append(temp)
        return final