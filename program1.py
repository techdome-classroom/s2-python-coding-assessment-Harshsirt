def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Traverse the string
    for char in s:
        if char in bracket_map:
            # Pop from stack if stack is not empty, otherwise assign dummy value '#'
            top_element = stack.pop() if stack else '#'
            
            
            if bracket_map[char] != top_element:
                return False
        else:
           
            stack.append(char)
    
   
    return not stack







    



  

