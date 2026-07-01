class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        final=[]
        products.sort()
        m=len(products)
        for i in range(len(searchWord)):
            search_str=searchWord[:i+1]
            temp=[]
            n=len(search_str)
            for i in range(m):
                if search_str == products[i][:n]:
                    temp.append(products[i])
                if len(temp)==3:
                    break
            final.append(temp)
        return final