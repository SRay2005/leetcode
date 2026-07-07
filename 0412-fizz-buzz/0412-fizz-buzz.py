class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output=["1"]
        for i in range(2,n+1):
            if i%3==0 and i%5==0:
                output.append("FizzBuzz")
            
            elif i%3==0:
                output.append("Fizz")

            elif i%5==0:
                output.append("Buzz")

            else:
                output.append(str(i))

        return output