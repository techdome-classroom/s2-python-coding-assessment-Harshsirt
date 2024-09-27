def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
  
    for char in s:
        if char in bracket_map:
           
            top_element = stack.pop() if stack else '#'
            
            
            if bracket_map[char] != top_element:
                return False
        else:
           
            stack.append(char)
    
   
    return not stack







    



  

