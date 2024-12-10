class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[]
        stack=[]
        for i in range(len(speed)):
            pair.append([position[i],speed[i]])
        pair=sorted(pair)[::-1]
        for x,y in pair:
            time=(target-x)/y
            stack.append(time)
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

