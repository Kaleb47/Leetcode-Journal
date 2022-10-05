class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        # first initialize the stack as an array
        stack = []
        for op in operations:
                if op == '+':
                    stack.append(stack[-1] + stack[-2])
                elif op == 'D':
                    stack.append(2 * stack[-1])
                elif op == "C":
                    stack.pop()
                else:
                    stack.append(int(op))
                    
        return sum(stack)
        
        #x = int[]
        
        # all calculations must fit in a 32-bit integer
        # c invalidates the previous scores
        # d double's the previous score
        # + adds the score
        
        #for i in operations[]:
            #if "c" in operations:
                #invalidates the previous score
               # self.operations.pop()
           # elif "+" in operations:
                # records a new score that is the sum of the previous scores
                # self.operations.push(# sum of the previous scores)
          #  elif "D" in operations:
                # self.operations.push(previous score * 2)
           # else:
                # return the sum of the list
               # return operations.sum()
